from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('account_list/',views.account_list,name='account_list'),
    path('about/',views.about,name='about'),
    path('articledetail/<int:pk>/',views.article_detail,name='article_detail'),
    path('articledetail/edit/<int:pk>/',views.article_edit, name='article_edit'),
    path('accountdetail/<int:pk>/',views.account_detail, name='account_detail'),
    path('accountdetail/edit/<int:pk>/',views.account_edit, name='account_edit'),
    path('accountbusinesstype/edit/<int:pk>/',views.accountbusinesstype_edit, name='accountbusinesstype_edit'),
    path('accountdetail/<int:pk>/accountbusinesstype_new/',views.accountbusinesstype_new, name='accountbusinesstype_new'),
    path('accountdetail/<int:pk>/report_new/',views.account_report_new, name='account_report_new'),
    path('reportdetail/<int:pk>/',views.report_detail, name='report_detail'),
    path('participant/edit/<int:pk>/',views.participant_edit, name='participant_edit'),
    path('account_new/',views.account_new, name='account_new'),
    path('report_new/',views.report_new, name='report_new'),
    path('reportdetail/edit/<int:pk>/',views.report_edit, name='report_edit'),
    path('reportdetail/<int:pk>/participant_new/',views.participant_new, name='participant_new'),
    path('article_new/',views.article_new, name='article_new'),
    path('mywork/<int:pk>/',views.mywork, name='mywork'),
    path('commentintern/<int:pk>/up',views.commentsintern_up, name='commentsintern_up'),
    path('commentintern/<int:pk>/down',views.commentsintern_down, name='commentsintern_down'),
    path('commentextern/<int:pk>/up',views.commentsextern_up, name='commentsextern_up'),
    path('commentextern/<int:pk>/down',views.commentsextern_down, name='commentsextern_down'),
    path('articledetail/<int:pk>/commentintern/new',views.commentintern_new, name='commentintern_new'),
    path('articledetail/<int:pk>/commentextern/new',views.commentextern_new, name='commentextern_new'),
    
]