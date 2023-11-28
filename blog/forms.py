# 3RD PARTY IMPORTS
from django import forms
# LOCAL IMPORTS
from . models import Comment


class CommentForm(forms.ModelForm):
    """
    A class for the comment field which
    will display on the view for the user.
    """
    class Meta:
        model = Comment
        fields = ('body',)
