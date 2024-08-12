from django import forms
from .models import Post
from datetime import datetime

class postForm(forms.Form):
    title= forms.CharField(label='title', max_length=100, required= True)
    body = forms.CharField(label='body', max_length=1000, widget=forms.Textarea)

    def save(self):
        model = Post(
            title = self.cleaned_data['title'],
            body = self.cleaned_data['body'],
            created_At=datetime.now()
        )
        model.save()

class postModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'file', 'url']
