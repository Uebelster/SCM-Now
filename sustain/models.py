from django.conf import settings
from django.db import migrations, models
from django.utils import timezone

# Create your models here.

class account(models.Model):
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    createdon = models.DateTimeField(default=timezone.now)
    inactive = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    taxid = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to ='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name

class accountbusinesstype(models.Model):
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    createdon = models.DateTimeField(default=timezone.now)
    inactive = models.BooleanField(default=False)
    name = models.CharField(max_length=200) #default auf businestypename
    accountfrom = models.ForeignKey('sustain.account',on_delete=models.CASCADE, related_name='businesstypesfrom')
    accountto = models.ForeignKey('sustain.account',on_delete=models.CASCADE, related_name='businesstypesto')
    businesstype = models.ForeignKey('sustain.businesstype',on_delete=models.CASCADE, related_name='accountbusinesstypes')
    
    def __str__(self):
        return self.name

class businesstype(models.Model):
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    createdon = models.DateTimeField(default=timezone.now)
    inactive = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class report(models.Model):
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    createdon = models.DateTimeField(default=timezone.now)
    inactive = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    account =  models.ForeignKey('sustain.account',on_delete=models.CASCADE, related_name='reports') #standard vom ersteller oder so
    reporttype = models.ForeignKey('sustain.reporttype',on_delete=models.CASCADE, related_name='reports')

    def __str__(self):
        return self.name

class reporttype(models.Model):
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    createdon = models.DateTimeField(default=timezone.now)
    inactive = models.BooleanField(default=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class participant(models.Model):
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    createdon = models.DateTimeField(default=timezone.now)
    inactive = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    report = models.ForeignKey('sustain.report',on_delete=models.CASCADE, related_name='participants')
    account =  models.ForeignKey('sustain.account',on_delete=models.CASCADE, related_name='participants')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class article(models.Model):
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    createdon = models.DateTimeField(default=timezone.now)
    inactive = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    report = models.ForeignKey('sustain.report',on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.name

class commentsintern(models.Model):
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    createdon = models.DateTimeField(default=timezone.now)
    inactive = models.BooleanField(default=False)
    description = models.TextField()
    article = models.ForeignKey('sustain.article',on_delete=models.CASCADE, related_name='internalcomments')

    def __str__(self):
        return self.name

class commentsextern(models.Model):
    createdon = models.DateTimeField(default=timezone.now)
    inactive = models.BooleanField(default=False)
    createdby_unauth = models.CharField(max_length=200)
    description = models.TextField()
    article = models.ForeignKey('sustain.article',on_delete=models.CASCADE, related_name='externalcomments')

    def __str__(self):
        return self.name

class commentreview(models.Model):
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    createdon = models.DateTimeField(default=timezone.now)
    inactive = models.BooleanField(default=False)
    RATING_CHOICES = (
        ('P','Positiv'),
        ('N','Negativ'),
    )
    positive = models.CharField(max_length=1, choices=RATING_CHOICES,blank=True, null=True)
    commentsintern = models.ForeignKey('sustain.commentsintern',on_delete=models.CASCADE, related_name='ratings',blank=True, null=True)
    commentsextern = models.ForeignKey('sustain.commentsextern',on_delete=models.CASCADE, related_name='ratings',blank=True, null=True)

    def __str__(self):
        return self.name