from django import forms


class PostCommentForm(forms.Form):
    text = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    website = forms.CharField(required=False)