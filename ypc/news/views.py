from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import News
from .forms import NewsForm
from el_pagination.decorators import page_template

# Create your views here.
@page_template('news/news_list.html')  # just add this decorator
def news_list(request, template='news/news.html', extra_context=None) :
	news = News.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	context = {
		'news' : news,
	}
	if extra_context is not None:
		context.update(extra_context)
	return render(request, template, context)

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
