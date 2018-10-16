from django import forms
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _


class CreatePostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Введи текст',
            'class': 'form-control'
        }),
    )
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autofocus': True,
            'placeholder': 'Введи текст'
        }),
    )

    class Meta:
        model = Post
        fields = ('text', 'title')


class CreateCommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'placeholder': 'Введи текст',
            'class': 'form-control'
        }),
        label=_('Ваш коментар:')
    )

    class Meta:
        model = Comment
        fields = ('text',)

