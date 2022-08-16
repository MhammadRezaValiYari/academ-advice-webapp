from django.conf.urls import url
from registration import views


app_name = "registration"

urlpatterns = [

    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^change_password/$', views.change_password, name='change_password'),


]
