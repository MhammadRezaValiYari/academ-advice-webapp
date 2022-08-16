
from django.conf.urls import url
from dashboard.views import DashboardView

app_name = "dashboard"

urlpatterns = [
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),

]
