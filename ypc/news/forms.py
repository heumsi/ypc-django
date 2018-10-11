from django import forms
from .models import News
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class NewsForm(forms.ModelForm):
	cover_image = forms.FileField(required=False)

	class Meta:
		model = News
		fields = ('title', 'published_date', 'description', 'text', 'cover_image', 'attachment')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'team_name': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
			'cover_image': forms.FileInput(attrs={'class': 'form-control-file'}),
			'attachment': forms.FileInput(attrs={'class': 'form-control-file'}),
			'text': SummernoteWidget()
		}
