from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import article, account,commentsextern, commentsintern, commentreview,report,participant,accountbusinesstype
from django.contrib.auth.decorators import login_required
from .forms import CreateCommentInt,CreateCommentExt,CreateAccount,CreateReport,CreateArticle,CreateParticipant

# Create your views here.

def article_list(request):
    accounts = account.objects.filter(inactive=False)
    articles = article.objects.filter(inactive=False)
    return render(request, 'sustain/article_list.html', {'articles':articles,'accounts':accounts})

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

@login_required
def account_new(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.createdby = request.user
            account.save()
            url = "/accountdetail/" + str(account.pk)
            return redirect(url, pk=account.pk )
    else:
        form = CreateAccount()
    return render(request, 'sustain/account_new.html', {'form': form})

@login_required
def report_new(request):
    if request.method == "POST":
        form = CreateReport(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.createdby = request.user
            report.save()
            url = "/reportdetail/" + str(report.pk)
            return redirect(url, pk=report.pk )
    else:
        form = CreateReport()
    return render(request, 'sustain/report_new.html', {'form': form})

@login_required
def article_new(request):
    if request.method == "POST":
        form = CreateArticle(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.createdby = request.user
            article.save()
            url = "/articledetail/" + str(article.pk)
            return redirect(url, pk=article.pk )
    else:
        form = CreateArticle()
    return render(request, 'sustain/article_new.html', {'form': form})

@login_required
def report_detail(request, pk):
    reports = get_object_or_404(report,pk=pk)
    return render(request, 'sustain/reportdetail.html', {'report':reports})

def account_list(request):
    accounts = account.objects.filter(inactive=False)
    return render(request, 'sustain/account_list.html', {'accounts':accounts})

def about(request):
    return render(request, 'sustain/about.html', {})

def mywork(request, pk):
    accounts = account.objects.filter(inactive=False,createdby=pk)
    reports = report.objects.filter(inactive=False,createdby=pk)
    articles = article.objects.filter(inactive=False,createdby=pk)
    return render(request, 'sustain/mywork.html', {'accounts':accounts,'reports':reports,'articles':articles})

@login_required
def participant_new(request, pk):
    if request.method == "POST":
        form = CreateParticipant(request.POST)
        reports = get_object_or_404(report, pk=pk)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.createdby = request.user
            participant.report = reports
            participant.save()
            url = "/reportdetail/" + str(pk)
            return redirect(url, pk=reports.pk )
    else:
        form = CreateParticipant()
    return render(request, 'sustain/participant_new.html', {'form': form})