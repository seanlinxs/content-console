from django import forms


class PageImageForm(forms.Form):
    name = forms.CharField()
    image = forms.FileField(label='Select an image file')


class NewsForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    image = forms.FileField(label='Select an image file')