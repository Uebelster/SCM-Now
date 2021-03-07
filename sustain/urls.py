from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('articledetail/<int:pk>/',views.article_detail,name='article_detail'),
    path('accountdetail/<int:pk>/',views.account_detail, name='account_detail'),
    path('commentintern/<int:pk>/up',views.commentsintern_up, name='commentsintern_up'),
    path('commentintern/<int:pk>/down',views.commentsintern_down, name='commentsintern_down'),
    path('commentextern/<int:pk>/up',views.commentsextern_up, name='commentsextern_up'),
    path('commentextern/<int:pk>/down',views.commentsextern_down, name='commentsextern_down'),
    path('articledetail/<int:pk>/commentintern/new',views.commentintern_new, name='commentintern_new'),
    path('articledetail/<int:pk>/commentextern/new',views.commentextern_new, name='commentextern_new'),
    
]