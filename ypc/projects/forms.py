from django import forms
from .models import Project
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ProjectForm(forms.ModelForm):
	# cover_image = forms.FileField(required=False)
	# attachment = forms.FileField(required=False)

	class Meta:
		model = Project
		fields = ('title', 'team_name', 'description', 'text', 'cover_image', 'attachment')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'team_name': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			'cover_image': forms.FileInput(attrs={'class': 'form-control-file'}),
			'attachment': forms.FileInput(attrs={'class': 'form-control-file'}),
			'text': SummernoteWidget()
		}
