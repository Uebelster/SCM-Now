from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import article, account,commentsextern, commentsintern, commentreview
from django.contrib.auth.decorators import login_required
from .forms import CreateCommentInt,CreateCommentExt

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

@login_required
def commentsintern_up(request, pk):
    commentsint = get_object_or_404(commentsintern, pk=pk)
    commentrev = commentreview(commentsintern = commentsint,positive = "P",createdby = request.user)
    commentrev.save()
    articlepk = str(commentsint.article.pk)
    url = "/articledetail/" + articlepk
    return redirect(url, pk=commentsint.article )

@login_required
def commentsintern_down(request, pk):
    commentsint = get_object_or_404(commentsintern, pk=pk)
    commentrev = commentreview(commentsintern = commentsint,positive = "N",createdby = request.user)
    commentrev.save()
    articlepk = str(commentsint.article.pk)
    url = "/articledetail/" + articlepk
    return redirect(url, pk=commentsint.article )

@login_required
def commentsextern_up(request, pk):
    commentsext = get_object_or_404(commentsextern, pk=pk)
    commentrev = commentreview(commentsextern = commentsext,positive = "P",createdby = request.user)
    commentrev.save()
    articlepk = str(commentsext.article.pk)
    url = "/articledetail/" + articlepk
    return redirect(url, pk=commentsext.article )

@login_required
def commentsextern_down(request, pk):
    commentsext = get_object_or_404(commentsextern, pk=pk)
    commentrev = commentreview(commentsextern = commentsext,positive = "N",createdby = request.user)
    commentrev.save()
    articlepk = str(commentsext.article.pk)
    url = "/articledetail/" + articlepk
    return redirect(url, pk=commentsext.article )

@login_required
def commentintern_new(request, pk):
    if request.method == "POST":
        form = CreateCommentInt(request.POST)
        articles = get_object_or_404(article, pk=pk)
        if form.is_valid():
            commentsintern = form.save(commit=False)
            commentsintern.createdby = request.user
            commentsintern.article = articles
            commentsintern.save()
            url = "/articledetail/" + str(pk)
            return redirect(url, pk=commentsintern.article.pk )
    else:
        form = CreateCommentInt()
    return render(request, 'sustain/commentint.html', {'form': form})

@login_required
def commentextern_new(request, pk):
    if request.method == "POST":
        form = CreateCommentExt(request.POST)
        articles = get_object_or_404(article, pk=pk)
        if form.is_valid():
            commentsextern = form.save(commit=False)
            commentsextern.article = articles
            commentsextern.save()
            url = "/articledetail/" + str(pk)
            return redirect(url, pk=commentsextern.article.pk )
    else:
        form = CreateCommentExt()
    return render(request, 'sustain/commentext.html', {'form': form})