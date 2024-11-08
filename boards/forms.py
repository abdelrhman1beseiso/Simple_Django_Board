from django import forms
from .models import Topic ,Post


class NewTopicForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows':5,'placeholder':'What is on your mind?'}
    ),max_length=3000,
                              help_text='the max length of the text is 3000')

    class Meta:
        model = Topic
        fields = ['subject','message']


class PostForm(forms.ModelForm):
    class Meta:
        message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Type your reply here...'}),
        label='Your Reply'
    )
        model = Post
        fields = ['message',]
