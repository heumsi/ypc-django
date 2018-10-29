from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Project
from .forms import ProjectForm
from el_pagination.decorators import page_template


# Create your views here.
@page_template('projects/projects_list.html')  # just add this decorator
def project_list(request, template='projects/projects.html', extra_context=None) :
	projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	context = {
		'projects' : projects,
		# 'row' : 1;
	}
	if extra_context is not None:
		context.update(extra_context)
		# context['row'] += 1;
	return render(request, template, context)

def project_detail(request, pk) :
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def project_new(request) :
	if request.method == "POST" :
		form = ProjectForm(request.POST, request.FILES)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('projects:project_detail', pk=post.pk)

	else :
		form = ProjectForm()
	return render(request, 'projects/project_edit.html', {'form': form})

def project_edit(request, pk) :
	post = get_object_or_404(Project, pk=pk)
	if request.method == "POST" :
		form = ProjectForm(request.POST, request.FILES, instance=post)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('projects:project_detail', pk=post.pk)
	else:
		form = ProjectForm(instance=post)
	return render(request, 'projects/project_edit.html', {'form': form})

def project_remove(request, pk) :
	post = get_object_or_404(Project, pk=pk)
	post.delete()

	return redirect('projects:project_list')
