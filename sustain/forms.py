from django import forms

from .models import commentsintern,commentsextern,account,report,article,participant

class CreateCommentInt(forms.ModelForm):
    class Meta:
         model = commentsintern
         fields = ('description',)

class CreateCommentExt(forms.ModelForm):
    class Meta:
         model = commentsextern
         fields = ('createdby_unauth','description',)

class CreateAccount(forms.ModelForm):
    class Meta:
         model = account
         fields = ('name','description','taxid','logo',)

class CreateReport(forms.ModelForm):
    class Meta:
         model = report
         fields = ('name','description','reporttype','account',)

class CreateArticle(forms.ModelForm):
    class Meta:
         model = article
         fields = ('name','description','report',)

class CreateParticipant(forms.ModelForm):
    class Meta:
        model = participant
        fields = ('account','name','description','approved',)