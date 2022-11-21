from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


# Create your views here.
# @login_required
# def main(request):
#     return render(request, 'index.html')

@login_required
def get_news(request):
    news = []
    base_url = "https://www.pravda.com.ua/news/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class="container_sub_news_list_wrapper mode1"] div[class="article_news_list"]')
    # print(content)
    for el in content:
        result = {}
        result['time'] = el.find('div', {'class': 'article_time'}).text
        result['title'] = el.find('div', {'class': 'article_header'}).text
        # news['link'] = el.find_next('a').get('href')
        news.append(result)
        # print(news)
    return render(request, 'scrape.html', {'news': news})


@login_required
def get_sport_news(request):
    sport_news = []
    base_url = "https://sport.ua/uk/uk"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', class_='news-items').find_all('div', class_='item')
    # print(content)
    for el in content:
        result = {}
        result['time'] = el.find('span', class_='item-date').text.strip()
        result['sport'] = el.find('span', class_='item-sport').text.casefold()
        result['news'] = el.find('div', {'class': 'item-title'}).text.strip()
        sport_news.append(result)
        # print(sport_news)
    return render(request, 'scrape_sport.html', {'sport_news': sport_news})


@login_required
def get_currency(request):
    currency = []
    date_now = datetime.now().strftime('%Y-%m-%d')
    base_url = 'https://minfin.com.ua/ua/currency/banks/usd/'
    response = requests.get(base_url + date_now + '/')
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('tbody', class_='list').find_all('tr')
    # print(content)
    for el in content:
        result = {}
        result['bank'] = el.find('a', {'class': 'mfm-black-link'}).text.strip()
        result['buy'] = el.find('td', {'class': 'responsive-hide mfm-text-right mfm-pr0'}).text.strip()
        if len(result['buy']) == 0:
            result['buy'] = '0.000'
        result['sale'] = el.find('td', {'class': 'responsive-hide mfm-text-left mfm-pl0'}).text.strip()
        if len(result['sale']) == 0:
            result['sale'] = '0.000'
        result['date'] = el.find('td', {'class': 'respons-collapsed mfcur-table-refreshtime'}).text.strip()

        currency.append(result)
    return render(request, 'scrape_currency.html', {'currency': currency})


@login_required
def get_it(request):
    it = []
    base_url = 'https://focus.ua/uk/technologies/list'
    urls = ['/', '?page=2', '?page=3', '?page=4', '?page=5', '?page=6', '?page=7', '?page=8', '?page=9']
    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('div[class="c-card-list__main"]')
        # print(content)
        for el in content:
            result = {}
            result['title'] = el.find('a', {'class': 'c-card-list__link'}).text.strip()
            result['time'] = el.find('time', {'class': 'c-card-list__date'}).text.strip()
            it.append(result)
        # print(result)
    return render(request, 'scrape_it.html', {'it': it})


@login_required
def get_fashion(request):
    fashion = []
    base_url = "https://life.nv.ua/ukr/krasota-i-moda.html"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class="row atom-list"] div[class="atom atom-style col-sm-6 col-lg-4"]')
    # print(content)
    for el in content:
        result = {}
        result['tag'] = el.find('span', {'class': 'atom-additional-category keep-mob'}).text.strip()
        result['time'] = el.find('span', {'class': 'atom-additional-pub-date'}).text.strip()
        result['title'] = el.find('div', {'class': 'text'}).text.replace(u'\xa0', u' ')
        fashion.append(result)
        # print(result)
    return render(request, 'fashion.html', {'fashion': fashion})


@login_required
def get_books(request):
    books = []
    base_url = "https://www.goodreads.com/list/show/2681.Time_Magazine_s_All_Time_100_Novels"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('table[class="tableList js-dataTooltip"] tr')
    # print(content)
    for el in content:
        result = {}
        result['number'] = el.find('td', {'class': 'number'}).text.strip()
        result['author'] = el.find('a', {'class': 'authorName'}).text.strip()
        result['title'] = el.find('a', {'class': 'bookTitle'}).text.strip()
        result['rating'] = el.find('span', {'class': 'minirating'}).text.strip()
        books.append(result)
        # print(result)
    return render(request, 'books.html', {'books': books})
