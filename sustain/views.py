from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import article, account,commentsextern, commentsintern, commentreview
from django.contrib.auth.decorators import login_required

# Create your views here.

def article_list(request):
    articles = article.objects.filter(inactive=False)
    return render(request, 'sustain/article_list.html', {'articles':articles})

def account_detail(request, pk):
    accounts = get_object_or_404(account, pk=pk)
    return render(request, 'sustain/accountdetail.html', {'account':accounts})

def article_detail(request, pk):
    articles = get_object_or_404(article, pk=pk)
    count_ratingposint = commentreview.objects.filter(positive="P", inactive=False,commentsintern=1).count()
    count_ratingnegint = commentreview.objects.filter(positive="N", inactive=False,commentsintern=1).count()
    count_ratingposext = commentreview.objects.filter(positive="P", inactive=False,commentsextern=1).count()
    count_ratingnegext = commentreview.objects.filter(positive="N", inactive=False,commentsextern=1).count()
    return render(request, 'sustain/articledetail.html', {'article':articles,'count_ratingposint':count_ratingposint,'count_ratingnegint':count_ratingnegint,'count_ratingposext':count_ratingposext,'count_ratingnegext':count_ratingnegext})