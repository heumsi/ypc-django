from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from news.models import News
from django.utils import timezone

def index(request) :
	projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
	news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
	return render(request, 'index.html', {'projects': projects, 'news': news})

def about(request) :
	return render(request, 'about.html')
