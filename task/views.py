from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView, FormView, UpdateView, DeleteView
from task.models import Task, Description,cs499Item
from django.core.urlresolvers import reverse
from django.contrib import auth
from .forms import ContactForm, MyRegistrationForm, ArticleForm, PictureForm, PinterestItem, CourseForm
from .models import Article,Course
from django.contrib import messages
import time, os
from django.conf import settings
from django.core.mail import send_mail,send_mass_mail


class TaskUpdate(UpdateView):
    model = Task
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = ''


class CourseUpdate(UpdateView):
    model = Course
    fields = ['courseid', 'homework', 'url', 'material', 'finish']
    template_name_suffix = '_update_form'
    success_url = '../courses'


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name_suffix = '_update_form'
    success_url = '../joanofarc'


class TaskDelete(DeleteView):
    model = Task
    success_url = ''

class ContactView(FormView):
    template_name = 'task/contact.html'
    form_class = ContactForm
    success_url = ''

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

class ListTasksView(ListView):
    model = Task
    queryset = Task.objects.all()

class TaskCreate(CreateView):
    model = Task
    fields = ['name']  #list of field need to fill in

    success_url = '../tasks'




class ListDescriptionView(ListView):
    model = Description

    def get_queryset(self):
        self.task = get_object_or_404(Task, name=self.args[0])
        context = Description.objects.filter(taskName=self.task)
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(ListTasksView,self).get_context_data(kwargs)
    #     context['name'] = Task.objects.filter(name=kwargs)
    #     return context
#
#
# from haystack.query import SearchQuerySet
#
# def search_titles(request):
#     tasks = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text'), '')
#
#     return render_to_response('ajax_search.html', {'tasks', tasks})
#
class ListArticles(ListView):
    model = Article
    queryset = Article.objects.all()

def article(request, article_id = 1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id)})

def cs499item(request, article_id = 1):
    return render_to_response('cs499item.html', {'article': cs499Item.objects.get(id=article_id)})

def pinterest(request):
    pictures = PinterestItem.objects.all()
    return render_to_response('pinterest.html',
                             locals(),context_instance=RequestContext(request))

def Renew(request):
    courses = Course.objects.all()
    for course in courses:
        course.finish = False
        course.save()
    return HttpResponseRedirect('/courses')



def Courses(request):
    full_name = request.user.username
    courses = Course.objects.filter(finish=False, username=full_name).order_by('due_date')
    if request.POST:
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "You Course was added")
            return render_to_response('courses.html', locals(), context_instance=RequestContext(request))
    else:
        form = CourseForm()
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('courses.html', locals(), context_instance=RequestContext(request))



def testvideo(request):
    full_name = request.user.username
    return render_to_response('task/testvideo.html', locals(), context_instance=RequestContext(request))

def index(request):
    full_name =request.user.username
    return render_to_response('task/index.html', locals(), context_instance=RequestContext(request))

def joanofarc(request):
    full_name = request.user.username
    articles = Article.objects.all()
    return render_to_response('task/HIS101/joanofarc.html', locals(), context_instance=RequestContext(request))


def team(request):
    full_name = request.user.username
    return render_to_response('task/team.html', locals(), context_instance=RequestContext(request))


def search_titles1(request):
    full_name = request.user.username
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    articles = Article.objects.filter(title_contains=search_text)
    return render_to_response('ajax_search.html', locals(), context_instance=RequestContext(request))


def search_titles(request):
    full_name = request.user.username
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    cs499items = cs499Item.objects.filter(title_contains=search_text)
    return render_to_response('ajax_search.html', locals(), context_instance=RequestContext(request))


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    full_name = request.user.username
    return render_to_response('loggedin.html',
                             locals(),context_instance=RequestContext(request))


def profile(request):
    full_name = request.user.username
    email = request.user.email
    return render_to_response('profile.html',
                             locals(),context_instance=RequestContext(request))



def invalid_login(request):
    full_name = request.user.username
    return render_to_response('invalid_login.html', locals(), context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register_user(request):
    full_name = request.user.username
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        else:
            return render_to_response('register.html', locals(), context_instance=RequestContext(request))
    else:
        form = MyRegistrationForm()
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('register.html', locals(), context_instance=RequestContext(request))

def register_success(request):
    full_name = request.user.username
    return render_to_response('register_success.html', locals(), context_instance=RequestContext(request))

def create(request):
    full_name = request.user.username
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "You Article was added")
            return HttpResponseRedirect('/all')
    else:
        form = ArticleForm()
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('create_article.html', locals(), context_instance=RequestContext(request))




def create_picture(request):
    full_name = request.user.username
    if request.POST:
        form = PictureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "You Picture was added")
            return HttpResponseRedirect('/pinterest')
    else:
        form = PictureForm()
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('create_picture.html', locals(), context_instance=RequestContext(request))

def like_article(request, article_id):
    full_name = request.user.username
    if article_id:
        a = cs499Item.objects.get(id=article_id)
        a.likes += 1
        a.save()
    return HttpResponseRedirect('../../get/%s' % article_id)

def like_article_his101(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        a.likes += 1
        a.save()
    return HttpResponseRedirect('../../getarticle/%s' % article_id)




'''
read stopswords return a set
'''
def readstopwords():
    stopwords = set()
    path = os.path.abspath('/Users/Xiaomin/Desktop/testproject/task/stopwords.txt')
    data = open(path, 'r')
    while True:
        str = data.readline()
        if (len(str) > 0):
            stopwords.add(str)
        else:
            break
    return stopwords



'''
TODO recommendations algorithm
'''
def getcs499Items():
    from haystack.query import SearchQuerySet
    from haystack.inputs import AltParser
    query = 'A study of smoothing methods for language models applied to ad hoc information retrieval'

    min_score = 0.5
    stopwords = readstopwords()

    words = query.split()
    clean_query = []
    for word in words:
        if word in stopwords:
            pass
        else:
            clean_query.append(word)

    str_query = ' '.join(clean_query)
    altsqs = SearchQuerySet().filter(content=AltParser('dismax', str_query, qf='qf=title^20.0 authors^2 abstract^2', mm=1))
    rs = []
    for item in altsqs:
        if item.score > min_score:
            rs.append(item)
    return rs



    # field = 'Information Theory'
    # result = cs499Item.objects.filter(category__icontains=field)
    # return result

    # from haystack.views import SearchView
    # sv = SearchView()
    # sv.build_form('information')
    # result = sv.get_results()
    # print("results=",len(result))
    # from django.test.client import RequestFactory
    # from haystack.views import SearchView
    # request = RequestFactory.get('/search/?q=information')


    #
    # from haystack.views import SearchView
    # import urllib2
    # url = '/search/?q=information'
    # request = urllib2.Request(url)
    # #request.add_header("Content-Type", "application/json") #
    # sv = SearchView(request)
    # sv.build_form()
    # result = sv.get_results()
    #
    #
    # # sv = SearchView(request)
    # # sv.build_form()
    # # result = sv.get_results()
    # print("result=",len(result))
    # return result

def getRecommendation():
    return ['xxu46@illinois.edu']

def send_email(request):
        items = getcs499Items()
        subject = 'no subject'
        messages =''
        i = 1

        for item in items:
            paper = 'Here is the ' + str(i) + ' paper\n\n'
            paper += 'This is link for detail information '+ str(item.urllink) + '\n'
            paper += 'The pdf link is here '+str(item.pdflink)+'\n'
            paper += 'The title:' + str(item.title) + '\n'
            safe_str = str(item.authors).encode('ascii', 'ignore')
            paper += 'The authors: ' +  str(item.authors) + '\n'
            paper += 'The subject: ' + str(item.subjects) + '\n'
            paper += 'The abstract:\n '+ str(item.abstract)+ '\n'
            paper += 'The date: ' + str(item.date) + '\n\n\n\n\n\n'
            messages += paper
            #subject = 'recommendation for recent paper from ' #+ str(item.category) + 'field'
            i += 1

        send_mail(subject, messages, settings.EMAIL_HOST_USER,  ['xxu46@illinois.edu'], fail_silently=False)

        #send_mail(subject, messages, settings.EMAIL_HOST_USER, getRecommendation, fail_silently=False)
        #
        # connection = SMTPConnection(username=auth_user, password=auth_password, fail_silently=fail_silently)
        # email = EmailMessage(subject, message, from_email, recipient_list, connection=connection, encoding='utf8').send()
        #

        return render_to_response('register_success.html')






def autoGenerateQueries():
    pass

def GetEmailList():
    pass

from datetime import date
from haystack.views import SearchView
from haystack.forms import ModelSearchForm, FacetedSearchForm
from haystack.query import EmptySearchQuerySet
class MySearchView(SearchView):
    """My custom search view."""

    # def get_queryset(self):
    #     queryset = super(MySearchView, self).get_queryset()
    #     # further filter queryset based on some set of criteria
    #     return queryset.filter(pub_date__gte=date(2015, 1, 1))
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super(MySearchView, self).get_context_data(*args, **kwargs)
    #     # do something
    #     return context

    # def basic_search(request, template='search/search.html', load_all=True, form_class=ModelSearchForm, searchqueryset=None, context_class=RequestContext, extra_context=None, results_per_page=None):
    #     query = ''
    #     results = EmptySearchQuerySet()
    #     if request.GET.get('q'):
    #         form = form_class(request.GET, searchqueryset=searchqueryset, load_all=load_all)
    #         if form.is_valid():
    #             query = form.cleaned_data['q']
    #             results = form.search()
    #     else:
    #         form = form_class(searchqueryset=searchqueryset, load_all=load_all)


    def get_results(self):
        """
        Fetches the results via the form.
        Returns an empty list if there's no query to search with.
        """
        results =  self.form.search()
        print("results",len(results))

        items = getcs499Items()
        subject = ''
        messages =''
        i = 1
        for item in items:
            paper = 'Here is the ' + str(i) + ' paper\n\n'
            paper += 'This is link for detail information '+ str(item.urllink) + '\n'
            paper += 'The pdf link is here '+str(item.pdflink)+'\n'
            paper += 'The title:' + str(item.title) + '\n'
            #safe_str = str(item.authors).encode('ascii', 'ignore')
            #paper += 'The authors: ' +   str(item.authors) + '\n'
            paper += 'The subject: ' + str(item.subjects) + '\n'
            paper += 'The abstract:\n '+ str(item.abstract)+ '\n'
            paper += 'The date: ' + str(item.date) + '\n\n\n\n\n\n'
            messages += paper
            subject = 'recommendation for recent paper from ' + str(item.category) + 'field'
            i += 1
        send_mail(subject, messages, settings.EMAIL_HOST_USER,  ['xxu46@illinois.edu'], fail_silently=False)
        #
        # connection = SMTPConnection(username=auth_user, password=auth_password, fail_silently=fail_silently)
        # email = EmailMessage(subject, message, from_email, recipient_list, connection=connection, encoding='utf8').send()
        return results










'''
I think the only way to improve the results is to know
1. add more records to database(already solved by automatically insert records into db)
2. collect keywords from professors
3. use keywords to do query on whoosh.
4. return back the results to users.
'''