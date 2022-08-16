from django.conf.urls import url
from articles import views


app_name = "articles"

urlpatterns = [
    url(r'^articles/$', views.articles, name='articles'),


]
