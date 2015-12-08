from django import forms


class PageImageUploadForm(forms.Form):
	image = forms.FileField(label='Select a image file')