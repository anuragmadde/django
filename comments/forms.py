from django import forms
# from pagedown.widgets import PagedownWidget


class CommentForm(forms.Form):
	content_type=forms.CharField(widget=forms.HiddenInput)
	object_id=forms.IntegerField(widget=forms.HiddenInput)
	content=forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))