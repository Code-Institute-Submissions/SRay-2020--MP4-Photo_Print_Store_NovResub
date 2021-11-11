""" This sets the form parameters for Blog app"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """ A form which contains fields for comments """
    class Meta:
        """ This class defines meta behaviour of above class """
        model = Comment
        fields = ('name', 'email', 'body')
