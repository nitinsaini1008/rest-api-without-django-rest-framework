from django import forms
from .models import About

class form_about(forms.ModelForm):
	class Meta:
		model=About
		fields='__all__'