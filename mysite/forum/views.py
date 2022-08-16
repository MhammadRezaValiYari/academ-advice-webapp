from audioop import reverse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def home(request):
    forums = forum.objects.all()
    count = forums.count()
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'main/home.html', context)


def messagDone(request):
    return render(request, 'main/messageDon.html')


def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum:messagDone')
    context = {'form': form}
    return render(request, 'main/addInForum.html', context)


def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('forum:messagDone'))
    context = {'form': form}
    return render(request, 'main/addInDiscussion.html', context)
