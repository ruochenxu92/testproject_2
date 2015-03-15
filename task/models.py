import django
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
import datetime

from django.utils import timezone


class Task (models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Description(models.Model):
    taskName = models.ForeignKey(Task, blank=True)
    content = models.TextField()

    def __unicode__(self):
        return self.taskName

class Article(models.Model):
    title = models.CharField(max_length=40, blank=True)
    body = models.TextField(blank=True)
    pub_date = models.DateTimeField("date published",blank=True)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Message(models.Model):
    sendto = models.CharField(max_length=255, default='friend1')
    subject = models.CharField(max_length=40, default="No Subject")
    body = models.TextField(default='')
    attachment = models.FileField(upload_to=None, max_length=100, default=None, blank=True)
    time = models.DateTimeField(default=timezone.now())
    username = models.CharField(max_length=255, default='xxu46')

    def __unicode__(self):
        return self.sendto



class Course(models.Model):
    #user = models.ForeignKey(User)
    courseid =  models.CharField(max_length=255, default='CS410')
    homework =  models.CharField(max_length=255, default='hw3')
    url = models.CharField(max_length=255, default='https://wiki.cites.illinois.edu/wiki/display/timanpub/CS410S15+Schedule')
    material = models.CharField(max_length=255, default='Your Material Link')
    due_date = models.CharField(max_length=255, default='Monday')
    finish = models.BooleanField(default=False)
    sememster = models.CharField(max_length=255, default='Spring 2015')
    username = models.CharField(max_length=255, default='xxu46')

    def __unicode__(self):
        return self.courseid

class PinterestItem(models.Model):
    title = models.CharField(max_length=100, default='')
    filename = models.CharField(max_length=255, default='')
    course = models.CharField(max_length=255, default='ST400')

from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    #user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=32)


'''
Start my real project models,@TODO need modify the specific in the Field()
class Article(models.Model):
    STATUS = Choices('draft', 'published')
    # ...
    status = StatusField()
'''

# class Field(models.Model):
#     name = models.CharField(max_length=80)
#
#     def __unicode__(self):
#         return smart_unicode(self.name)
#
#     class Meta:
#         ordering = ('name',)
#
# class Interest(models.Model):
#     name = models.CharField(max_length=80)
#     field = models.CharField
#
#     def __unicode__(self):
#         return smart_unicode(self.name)
#
#     class Meta:
#         ordering = ('name',)
#
# class Author(models.Model):
#     name = models.CharField(max_length=80)
#     institutions = models.CharField(max_length=80,null=True, blank=True)
#     field = models.ForeignKey(Field, blank=True)
#     interest = models.ManyToManyField(Interest, blank=True)
#     authorUrl = models.CharField(max_length=200,null = True,blank=True)
#
#     def __unicode__(self):
#         return smart_unicode(self.name)
#
#     class Meta:
#         ordering = ('field',)
#
# class Paper(models.Model):
#     title = models.CharField(max_length=80)
#     content = models.TextField(blank=True)
#     author = models.ManyToManyField(Author, blank=True)
#     pub_date = models.DateTimeField(blank=True, null=True)# auto_now=False, auto_now_add=False
#     citedTimes = models.IntegerField(blank=True, default=0)
#     paperUrl = models.CharField(max_length=200, null=True, blank=True)
#
#     def __unicode__(self):
#         return smart_unicode(self.title)
#
#     class Meta:
#         ordering = ('title',)
# # from task.models import Field, Interest, Author, Paper
# # f = Field.objects.filter(pk=1)[0]
# # i = Interest.objects.filter(pk=1)[0]
# # author = Author(name='Manoj Prabhakaran',institutions='Computer Science, University of Illinois Urbana-Champaign',field=f,authorUrl='http://web.engr.illinois.edu/~mmp/')


class Page(models.Model):
    title = models.CharField(max_length=80,blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    pubDate = models.DateTimeField(blank=True, null=True)# auto_now=False, auto_now_add=False
    citedTimes = models.IntegerField(default=0)
    paperUrl = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=80,null = True,blank=True)
    institution = models.CharField(max_length=80,null=True, blank=True)
    field = models.CharField(max_length=80, null=True, blank=True)
    interest = models.CharField(max_length=80, null = True,blank=True)
    authorUrl = models.CharField(max_length=200, null = True,blank=True)

    def __unicode__(self):
        return smart_unicode(self.title)

    class Meta:
        ordering = ('author',)


class cs499Item(models.Model):
    urllink = models.CharField(max_length=80,  default='')
    pdflink = models.CharField(max_length=80,  default='')
    title = models.CharField(max_length=80,    default='')
    authors = models.CharField(max_length=80,  default='')
    subjects = models.CharField(max_length=80, default='')
    abstract = models.TextField(default='')
    date = models.DateTimeField(blank=True, null=True)# auto_now=False, auto_now_add=False
    category = models.CharField(max_length=200, default='')
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return smart_unicode(self.title)

    def get_absolute_url(self):
        return '/get/%i/' % self.id

    class Meta:
        ordering = ('date',)


class Scholar(models.Model):
    name = models.CharField(max_length=80)
    institutions = models.CharField(max_length=80,null=True, blank=True)
    paper_title = models.CharField(max_length=255)
    field = models.CharField(max_length=200, default='Computer Science')
    interest = models.CharField(max_length=100)
    author_url = models.CharField(max_length=200,default='')
    pub_date = models.CharField(max_length=4)
    cite = models.ForeignKey(cs499Item, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.name)

    class Meta:
        ordering = ('field',)

class Faculty(models.Model):
    name = models.CharField(max_length=80, default='')
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')

    field = models.CharField(max_length=200, default='Computer Science')
    institution = models.CharField(max_length=100, default='University of Illinios at Urbana-Champaign')

    def __unicode__(self):
        return smart_unicode(self.name)

    class Meta:
        ordering = ('field',)

