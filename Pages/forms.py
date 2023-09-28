from .models import Comment, Review_post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review_post
        fields = ('title', 'game', 'content', 'rating')