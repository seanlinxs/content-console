from django import forms


class PageImageUploadForm(forms.Form):
	image = forms.FileField(label='Select an image file')


class NewsForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    image = forms.FileField(label='Select an image file')