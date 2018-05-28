from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import News
from .forms import NewsForm

# Create your views here.
def news_list(request) :
	# news = News.objects
	# print("#########", news)
	# if(  )
	news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'news/news.html', {'news' : news})

def news_detail(request, pk) :
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})

def news_new(request) :
	if request.method == "POST" :
		form = NewsForm(request.POST, request.FILES)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('news:news_detail', pk=post.pk)

	else :
		form = NewsForm()
	return render(request, 'news/news_edit.html', {'form': form})

def news_edit(request, pk) :
	post = get_object_or_404(News, pk=pk)
	if request.method == "POST" :
		form = NewsForm(request.POST, instance=post)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('news:news_detail', pk=post.pk)
	else:
		form = NewsForm(instance=post)
	return render(request, 'news/news_edit.html', {'form': form})

def news_remove(request, pk) :
	post = get_object_or_404(News, pk=pk)
	post.delete()

	return redirect('news:news_list')
