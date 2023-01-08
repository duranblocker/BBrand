from django import forms
from .models import Svg


class SvgUpdateForm(forms.ModelForm):
	class Meta:
		model = Svg
		fields = ['title','wallType','wallRefNum','path','width','height']

class SvgPathCreateLineForm(form.ModelForm):
	class Meta
		model = SvgPath
		fields = ['title','PathRefNum','pathType','startx','endy']


