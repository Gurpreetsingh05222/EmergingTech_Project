from django import forms
from .models import Post, ContactUs

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','author','content']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'postcontent'})
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'phone', 'message']