from django import forms
from django.utils.translation import gettext_lazy as _

from .models import commentsintern,commentsextern,account,report,article,participant,accountbusinesstype

class CommentInt(forms.ModelForm):
    class Meta:
         model = commentsintern
         fields = ('description',)
         labels = {
             'description': _('Kommentar'),
         }

class CommentExt(forms.ModelForm):
    class Meta:
         model = commentsextern
         fields = ('createdby_unauth','description',)
         labels = {
             'createdby_unauth': _('Name des Erstellers'),
             'description': _('Kommentar'),
         }

class Account(forms.ModelForm):
    class Meta:
         model = account
         fields = ('name','description','taxid','logo','inactive',)
         labels = {
            'name': _('Unternehmensname'),
            'description': _('Beschreibung'),
            'taxid': _('Umsatzsteuer ID'),
            'logo': _('Firmenlogo'),
            'reporttype': _('Berichtstyp'),
            'inactive': _('Inaktiv'),
         }

class Report(forms.ModelForm):
    class Meta:
         model = report
         fields = ('name','description','reporttype','account','inactive',)
         labels = {
            'name': _('Berichtsthema'),
            'description': _('Beschreibung'),
            'reporttype': _('Berichtstyp'),
            'account': _('Unternehmen'),
            'inactive': _('Inaktiv'),
         }

class AccountReport(forms.ModelForm):
    class Meta:
         model = report
         fields = ('name','description','reporttype','inactive',)
         labels = {
            'name': _('Berichtsthema'),
            'description': _('Beschreibung'),
            'reporttype': _('Berichtstyp'),
            'inactive': _('Inaktiv'),
         }

class Article(forms.ModelForm):
    class Meta:
         model = article
         fields = ('name','description','report','picture','inactive',)
         labels = {
             'name': _('Artikelthema'),
             'description': _('Beschreibung'),
             'report': _('Zugehöriger Bericht'),
             'picture': _('Deckblatt/Bild'),
             'inactive': _('Inaktiv'),
         }

class Participant(forms.ModelForm):
    class Meta:
        model = participant
        fields = ('account','name','description','approved','inactive',)
        labels = {
            'account': _('Teilnehmendes Unternehmen'),
            'name': _('Funktion'),
            'description': _('Beschreibung'),
            'approved': _('Bestätigt'),
            'inactive': _('Inaktiv'),
         }

class AccountBusinessTypes(forms.ModelForm):
    class Meta:
        model = accountbusinesstype
        fields = ('accountto','businesstype','inactive',)
        labels = {
            'accountto': _('Unternehmen'),
            'businesstype': _('Geschäftsbeziehung'),
            'inactive': _('Inaktiv'),
         }