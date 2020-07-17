from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('indiatoday_scrape/', views.indiatoday_scrape, name="indiatodayscrape"),
    path('news/indiatoday', views.news_list_indiatoday, name="indiatoday"),
    path('dainikjagran_scrape/', views.dainikjagran_scrape, name="dainikjagranscrape"),
    path('news/dainikjagran', views.news_list_dainikjagran, name="dainikjagran"),
    path('hindustantimes_scrape/', views.hindustantimes_scrape, name="hindustantimesscrape"),
    path('news/hindustantimes', views.news_list_hindustantimes, name="hindustantimes"),

]