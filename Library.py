# Библиотека!

import requests
from bs4 import BeautifulSoup
import random

pars = ['Парс', "Парсс", "Pars", "Parss"]
mang = ['Манга', 'манга', 'Manga', 'manga']
mangapop = ['mangapop', 'мангапоп']
IT = ['Айти', 'айти', 'it', 'It']
python = ['Python', 'python', 'пайтон', 'Пайтон']
js = ['JavaScript', 'JS', 'js', 'javascript']
css = ['Css', 'css', 'CSS']
html = ['HTML', 'Html', 'html']
ch = ['c#', 'C#']
cpp = ['C++', 'c++']
java = ['Java', 'java']

search = ['Найди', 'найди']
l1 = ['lib1', 'Библиотека1', 'Библиотека', 'библиотека']
l2 = ['lib2', 'Библиотека2', 'библиотека2']

def manga():
    URL = 'https://mangapoisk.ru/manga?sortBy=-year'
    HEDERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

    response = requests.get(URL, HEDERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'post-description')
    comps = []
    v_l = []

    for item in items:
        comps.append({'link': item.find('a', class_ = 'card-about').get('href')})
    for comp in comps:
        v_l.append(comp['link'])

    j = len(v_l)
    r = random.randint(0, j)
    
    print(v_l[r])
    qqq = 'https://mangapoisk.ru' + v_l[r]
    return qqq

def manpop():
    URL = 'https://mangapoisk.ru/manga?sortBy=popular'
    HEDERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

    response = requests.get(URL, HEDERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'post-description')
    comps = []
    v_l = []

    for item in items:
        comps.append({'link': item.find('a', class_ = 'card-about').get('href')})
    for comp in comps:
        v_l.append(comp['link'])

    j = len(v_l)
    r = random.randint(0, j)
    
    print(v_l[r])
    qqq = 'https://mangapoisk.ru' + v_l[r]
    return qqq

def it():
    URL = 'https://booksonline.com.ua/search.php?s=%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5&lang='
    HEDERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

    response = requests.get(URL, HEDERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'block_button')
    comps = []
    v_l = []

    for item in items:
        comps.append({'link': item.find('a', class_ = 'but_reed').get('href')})
    for comp in comps:
        v_l.append(comp['link'])


    j = len(v_l)
    r = random.randint(0, j)
    
    print(v_l[r])
    qqq = 'https://booksonline.com.ua/' + v_l[r]
    return qqq

def it2():
    URL = 'https://avidreaders.ru/genre/programmirovanie/'
    HEDERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

    response = requests.get(URL, HEDERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'book_name')
    comps = []
    v_l = []

    for item in items:
        comps.append({'link': item.find('a', class_ = '').get('href')})
    for comp in comps:
        v_l.append(comp['link'])


    j = len(v_l)
    r = random.randint(0, j)
    
    print(v_l[r])
    qqq = v_l[r]
    return qqq

def Python():
    URL = 'https://avidreaders.ru/s/Python/'
    HEDERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

    response = requests.get(URL, HEDERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'book_name')
    comps = []
    v_l = []

    for item in items:
        comps.append({'link': item.find('a', class_ = '').get('href')})
    for comp in comps:
        v_l.append(comp['link'])


    j = len(v_l)
    r = random.randint(0, j)
    
    print(v_l[r])
    qqq = v_l[r]
    return qqq

def JS():
    URL = 'https://avidreaders.ru/s/JavaScript'
    HEDERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

    response = requests.get(URL, HEDERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'book_name')
    comps = []
    v_l = []

    for item in items:
        comps.append({'link': item.find('a', class_ = '').get('href')})
    for comp in comps:
        v_l.append(comp['link'])


    j = len(v_l)
    r = random.randint(0, j)
    
    print(v_l[r])
    qqq = v_l[r]
    return qqq

def Java():
    URL = 'https://avidreaders.ru/s/Java'
    HEDERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

    response = requests.get(URL, HEDERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'book_name')
    comps = []
    v_l = []

    for item in items:
        comps.append({'link': item.find('a', class_ = '').get('href')})
    for comp in comps:
        v_l.append(comp['link'])


    j = len(v_l)
    r = random.randint(0, j)
    
    print(v_l[r])
    qqq = v_l[r]
    return qqq

def HTML():
    URL = 'https://avidreaders.ru/s/HTML'
    HEDERS = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

    response = requests.get(URL, HEDERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'book_name')
    comps = []
    v_l = []

    for item in items:
        comps.append({'link': item.find('a', class_ = '').get('href')})
    for comp in comps:
        v_l.append(comp['link'])


    j = len(v_l)
    r = random.randint(0, j)
    
    print(v_l[r])
    qqq = v_l[r]
    return qqq

def lib1(t):
    task = ' '.join(t)
    url = 'https://avidreaders.ru/s/' + task
    return url

def lib2(t):
    task = ' '.join(t)
    url = 'https://booksonline.com.ua/search.php?s=' + task
    return url

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == message.content:
            ms = message.content
            ms_l = ms.split()
            for i in ms_l:
                
                if i in pars:
                    for j in ms_l:
                        if j in mang:
                            await message.channel.send(manga())
                            
                        if j in mangapop:
                            await message.channel.send(manpop())

                        if j in IT:
                            await message.channel.send(it2())

                        if j in python:
                            await message.channel.send(Python())

                        if j in java:
                            await message.channel.send(Java())

                        if j in js:
                            await message.channel.send(JS())

                        if j in html:
                            await message.channel.send(HTML())

                if i in search:
                    for j in ms_l:
                        if j in l1:
                            del ms_l[0]
                            del ms_l[0]
                            del ms_l[0]
                            print(ms_l)
                            await message.channel.send(lib1(ms_l))
                                
                        if j in l2:
                            del ms_l[0]
                            del ms_l[0]
                            del ms_l[0]
                            print(ms_l)
                            await message.channel.send(lib2(ms_l))
                                
client = MyClient()
client.run('ODk1MzM3MzU0NTE1MDY2OTUw.YV3F4w.56lzZ-ZABw1FnlD3p7-RtMib89M')




