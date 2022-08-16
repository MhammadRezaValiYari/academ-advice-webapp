
from django.conf.urls import url
from base.views import HomeView, AboutView, ExpriensView


app_name = "base"

urlpatterns = [
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^expriens/$', ExpriensView.as_view(), name='expriens'),
]
