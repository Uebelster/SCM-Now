from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('articledetail/<int:pk>/',views.article_detail,name='article_detail'),
    path('accountdetail/<int:pk>/',views.account_detail, name='account_detail'),
]