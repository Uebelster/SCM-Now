from django import forms

from .models import commentsintern,commentsextern

class CreateCommentInt(forms.ModelForm):
    class Meta:
         model = commentsintern
         fields = ('description',)

class CreateCommentExt(forms.ModelForm):
    class Meta:
         model = commentsextern
         fields = ('createdby_unauth','description',)