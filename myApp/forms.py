from django import forms
from myApp.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post', 'post_type')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Activity'}),
            'post': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description of the Activity'}),
            'post_type': forms.Select(attrs={'class': 'form-control'}),
        }