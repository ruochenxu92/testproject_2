from django.conf.urls import patterns, include, url
from django.contrib import admin
from task import views
import haystack
from task.views import MySearchView

urlpatterns = patterns('',
    #url(r'^$', views.ListTasksView.as_view()),
    url(r'^tasks/$', views.ListTasksView.as_view()),
    url(r'^tasksUpdate/(?P<pk>[\w-]+)$', views.TaskUpdate.as_view()),
    url(r'^tasksDelete/(?P<pk>[\w-]+)$', views.TaskDelete.as_view()),
    url(r'^tasksCreate/$', views.TaskCreate.as_view()),
    url(r'^tasksContact/$', views.ContactView.as_view()),
    (r'^descriptions/([\w-]+)/$', views.ListDescriptionView.as_view()),
    (r'^$','task.views.index' ),
    (r'^search/', include('haystack.urls')),
    (r'^joanofarc/$','task.views.joanofarc' ),
    (r'^team/$','task.views.team' ),
    url(r'^mysearchview/$', MySearchView(), name='search_view'),
    url(r'^accounts/register/$', 'task.views.register_user'),
    url(r'^video/$', 'task.views.testvideo'),
    url(r'^accounts/register_success/$', 'task.views.register_success'),
    url(r'^accounts/login/$', 'task.views.login'),
    url(r'^accounts/auth/$', 'task.views.auth_view'),
    url(r'^accounts/logout/$', 'task.views.logout'),
    url(r'^accounts/loggedin/$', 'task.views.loggedin'),
    url(r'^accounts/invalid/$', 'task.views.invalid_login'),
    url(r'^all/$', views.ListArticles.as_view()),
    url(r'^his101paper/$', 'task.views.his101paper'),
    url(r'^create/$', 'task.views.create'),
    url(r'^get/(?P<article_id>\d+)/$', 'task.views.cs499item'),
    url(r'^getarticle/(?P<article_id>\d+)/$', 'task.views.article'),
    url(r'^send_email/$', 'task.views.send_email'),
    url(r'^like/(?P<article_id>\d+)/$', 'task.views.like_article'),
    url(r'^likearticle/(?P<article_id>\d+)/$', 'task.views.like_article_his101'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... the rest of your URLconf here ...

urlpatterns += staticfiles_urlpatterns()




from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
                            url(r'^static/(?P<path>.*)$', 'serve'),
    )


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
#
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls.static import static
# urlpatterns += staticfiles_urlpatterns()
# #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
