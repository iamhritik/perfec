from django import forms
from django.forms import ModelForm
from prefik.models import Blog

class Blogform(ModelForm):
	class Meta:
		model = Blog
		fields = '__all__'
		widgets = {
			'title' : forms.TextInput(attrs={'id':'title','placeholder':'Please enter your title','autocomplete':'off'}),
			'content' : forms.Textarea(attrs={'rows':10,'cols':40,'id':'content','placeholder':'Add your content here ...','autocomplete':'off'}),
			'category' : forms.SelectMultiple(attrs={'id':'category'}),
			'author' : forms.TextInput(attrs={'id':'author','placeholder':'Please enter your author','autocomplete':'off',}),
			'image' : forms.FileInput(attrs={'id':'image'}),

		}

