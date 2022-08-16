from importlib.resources import path
from urllib import response
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render
from articles.models import Article
import os

# Create your views here.


def articles(request):
    show_model = Article.objects.all()
    return render(request, 'main/articles.html', {"Article": show_model})


def download(request, path):

    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application"/Article)
            response['Content_Disposition'] = 'inline;filename' + \
                os.path.basename(file_path)
            return response
    raise Http404
