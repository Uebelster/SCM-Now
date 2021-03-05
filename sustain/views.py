from django.shortcuts import render
from django.utils import timezone
from .models import article

# Create your views here.

def article_list(request):
    articles = article.objects.filter(inactivce=False)
    return render(request, 'sustain/article_list.html', {'articles':articles})