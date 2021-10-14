from django import forms
from.models import Comment, Image

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner', 'likes', 'pub_date']
# class NewCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         exclude = ['postde', 'owner', 'pub_date']  
  