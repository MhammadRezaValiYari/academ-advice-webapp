import imp
from unicodedata import name
from django.conf.urls import url
from forum import views


app_name = "forum"

urlpatterns = [

    url(r'^forum/$', views.home, name='forum'),
    url(r'^addInForum/$', views.addInForum, name='addInForum'),
    url(r'^addInDiscussion/$', views.addInDiscussion, name='addInDiscussion'),
    url(r'^messagDone/$', views.messagDone, name="messagDone")
]
