# import needs modouls

from django.views.generic import TemplateView
from .models import *

# Create your views here.


class HomeView(TemplateView):
    template_name = 'main/index.html'


class AboutView(TemplateView):
    template_name = 'main/about.html'


class ExpriensView(TemplateView):
    template_name = 'main/expriens.html'
