import urllib.request
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from .models import *
import sqlite3




def index(request):

    return render(request,'index.html')

def news_list_indiatoday(request):
    headlines1 = IndiaTodayNews.objects.all()[:]
    context = {
        'object_list': headlines1,
    }
    return render(request, "news/indiatoday/indiatoday.html", context)

def news_list_dainikjagran(request):
    headlines2 = DainikJagranNews.objects.all()[:]
    context = {
        'object_list': headlines2,
    }
    return render(request, "news/dainikjagran/dainikjagran.html", context)



def news_list_hindustantimes(request):
    headlines3 = HindustanTimesNews.objects.all()[:]
    context = {
        'object_list': headlines3,
    }
    return render(request, "news/hindustantimes/hindustantimes.html", context)




def indiatoday_scrape(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute('DELETE FROM NewsRenderApp_indiatodaynews')
    conn.commit()
    res = urllib.request.urlopen("https://www.indiatoday.in/top-stories").read()

    soup = BeautifulSoup(res, "html.parser")

    news_box = soup.find('div', {'class': 'view-content'})
    all_news = news_box.find_all('h2')
    all_news_link = news_box.find_all('a')
    all_news_image = news_box.find_all('img')

    for i in range(len(all_news)):
        title = (str(all_news[i].get('title')))
        link = (str("https://www.indiatoday.in" + str(all_news_link[i].get('href'))))
        image = (str(all_news_image[i].get('src')))
        new_headline = IndiaTodayNews()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image
        new_headline.save()

    return redirect("../")

def dainikjagran_scrape(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute('DELETE FROM NewsRenderApp_dainikjagrannews')
    conn.commit()
    res = urllib.request.urlopen(f"https://english.jagran.com/latest-news").read()

    soup = BeautifulSoup(res, "html.parser")

    news_box = soup.find('ul', {'class': 'topicList'})
    all_news_link = news_box.find_all('a')
    all_news_image = news_box.find_all('img')

    for i in range(len(all_news_link)):
        title = (str(all_news_image[i].get('alt')))
        link = (str("https://english.jagran.com" + str(all_news_link[i].get('href'))))
        image = (str(all_news_image[i].get('data-src')))
        new_headline = DainikJagranNews()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image
        new_headline.save()

    return redirect("../")

def hindustantimes_scrape(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute('DELETE FROM NewsRenderApp_hindustantimesnews')
    conn.commit()
    req = urllib.request.Request(f"https://www.hindustantimes.com/latest-news",
                                 headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req).read()

    soup = BeautifulSoup(res, "html.parser")

    news_box = soup.find('ul', {'class': 'latest-news-bx more-latest-news more-separate'})

    all_news = news_box.find_all('a',{'class':'zoo-image'})
    all_news_image = news_box.find_all('img')

    for i in range(len(all_news_image)):
        title = (str(all_news[i].get('title')))
        link = (str(all_news[i].get('href')))
        image = (str(all_news_image[i].get('src')))
        new_headline = HindustanTimesNews()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image
        new_headline.save()

    return redirect("../")


