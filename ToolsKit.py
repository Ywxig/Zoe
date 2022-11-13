import requests
from bs4 import BeautifulSoup
import random
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

def emodji(classemogi):
    
    if classemogi == 'class_sleep':
        arr = ['😴', '💤']
        j = len(arr)
        j = j - 1
        r1 = random.randint(0, j)
        AWAITE = arr[r1]
        return str(AWAITE)

    if classemogi == 'class_bad':
        arr = ['😥', '😢', '😭', '😿', '😪', '😔']
        j = len(arr)
        j = j - 1
        r1 = random.randint(0, j)
        AWAITE = arr[r1]
        return AWAITE

    if classemogi == 'class_heppy':
        arr = ['😀', '😃', '😄', '😁', '😆', '😅', '🤣', '😂', '🙂', '🙃', '😉', '😹', '😸', '😺']
        j = len(arr)
        j = j - 1
        r1 = random.randint(0, j)
        AWAITE = arr[r1]
        return str(AWAITE)     

    if classemogi == 'class_cool':
        arr = ['😎', '🔥', '😼']
        j = len(arr)
        j = j - 1
        r1 = random.randint(0, j)
        AWAITE = arr[r1]
        return AWAITE 

    if classemogi == 'class_working':
        arr = ['💻', '🖥', '🤓']  
        j = len(arr)
        j = j - 1
        r1 = random.randint(0, j)
        AWAITE = arr[r1]
        return AWAITE 
    
    if classemogi == 'class_love':
        arr = ['🥰', '😍', '😘', '💕', '💞', '💘', '💋', '😻']
        j = len(arr)
        j = j - 1
        r1 = random.randint(0, j)
        AWAITE = arr[r1]
        return AWAITE        

    if classemogi == 'class_game':
        arr = ['🥇', '🕹', '🎰', '🏆', '🎮', '🎲']
        j = len(arr)
        j = j - 1
        r1 = random.randint(0, j)
        AWAITE = arr[r1]
        return AWAITE

class Search:

    def PornHub(List):

        task = '+'.join(List)
        s = 'https://rt.pornhub.com/video/search?search=' + task
        return s

    def Youtube(List):

        task = '+'.join(List)
        s = 'https://www.youtube.com/results?search_query=' + task
        return s

    def Googol(List):

        task = '+'.join(List)
        s = 'https://www.google.com/search?q=' + task
        return s

    def Yandex( List):
        task = '%20'.join(List)
        s = 'https://yandex.ru/yandsearch?clid=202826&text=' + task
        return s

class Rooport():

    def TitleRooport(Title):
        file = open('rooport.txt', 'w')
        file.write(str( '-{'+ Title + '}-' +'\n|Доклад о внутрених системах и данных| \n |Доклад затрагивает только систему сервера и некоторые данные других пользывотелей(ели такие есть)|' + '\n'))
       

    def complitRooport( URL_FAIL, Rooports):
        file = open(URL_FAIL, 'r')
        roop = file.read()
        file = open('rooport.txt', 'a')
        file.write(str(roop) + ' -- ' + str(Rooports) + '\n')

class Progect():

    def Read():
        f = open('Progect.txt', 'r')
        text = f.read()
        return text

    def New(Name):
        f = open('Progect.txt', 'a')
        f.write('_|_' + str(Name))

class Parser:

    def Joke():
        URL = 'https://rt.pornhub.com/'
        HEDERS = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
            }

        response = requests.get(URL, HEDERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('div', class_ = '')
        comps = []
        v_l = []

        for item in items:
            comps.append({'link': item.find('div', class_ = 'quote')})
        for comp in comps:
            v_l.append(comp['link'])

        j = len(v_l)
        r = random.randint(0, j)
        
        print(v_l[r])


    def Porn():
        URL = 'https://rt.pornhub.com/'
        HEDERS = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
            }

        response = requests.get(URL, HEDERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('div', class_ = 'thumbnail-info-wrapper clearfix')
        comps = []
        v_l = []

        for item in items:
            comps.append({'link': item.find('a', class_ = '').get('href')})
        for comp in comps:
            v_l.append(comp['link'])

        j = len(v_l)
        r = random.randint(0, j)
        
        print(v_l[r])


    def Kino():
        URL = 'https://www.kinopoisk.ru/lists/top250/?tab=all'
        HEDERS = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
            }

        response = requests.get(URL, HEDERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('div', class_ = 'selection-film-item-meta selection-film-item-meta_theme_desktop')
        comps = []
        v_l = []

        for item in items:
            comps.append({'link': item.find('a', class_ = 'selection-film-item-meta__link').get('href')})
        for comp in comps:
            v_l.append(comp['link'])

        j = len(v_l)
        r = random.randint(0, j)
        
        return'https://www.kinopoisk.ru' + v_l[r]

    def StopGameRuAndroid():
        URL = 'https://stopgame.ru/games/Android'
        HEDERS = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
            }

        response = requests.get(URL, HEDERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('div', class_ = 'item game-summary game-summary-horiz')
        comps = []
        v_l = []

        for item in items:
            comps.append({'link': item.find('a', class_ = '').get('href')})
        for comp in comps:
            v_l.append(comp['link'])

        j = len(v_l)
        r = random.randint(0, j)
        
        return 'https://stopgame.ru' + v_l[r]

    def StopGameRu():
        URL = 'https://stopgame.ru/games/Android'
        HEDERS = {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
            }

        response = requests.get(URL, HEDERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.findAll('div', class_ = 'item game-summary game-summary-horiz')
        comps = []
        v_l = []

        for item in items:
            comps.append({'link': item.find('a', class_ = '').get('href')})
        for comp in comps:
            v_l.append(comp['link'])
    

        j = len(v_l)
        r = random.randint(0, j)
        
        return 'https://stopgame.ru' + v_l[r]

class WaterMap:
    def Air():
        owm = OWM('88c77e859289463928b17b24f2f7ea99')
        mgr = owm.weather_manager()

        # Search for current weather in London (Great Britain) and get details
        observation = mgr.weather_at_place('Молдова')
        w = observation.weather
        w2 = w.temperature('celsius')['temp']
        print(w)

    def Status():
        owm = OWM('88c77e859289463928b17b24f2f7ea99')
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place('Молдова')
        w = observation.weather
        w2 = w.temperature('celsius')['temp']
        print(w)
        print(w2)
        return "В даный момент " + str(w.status)
            
    def Temp():
        owm = OWM('88c77e859289463928b17b24f2f7ea99')
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place('Молдова')
        w = observation.weather
        w2 = w.temperature('celsius')['temp']
        print(w)
        print(w2)
        return "В даный момент " + str(w.temperature('celsius')['temp']) + '°'
            
    def All():
        owm = OWM('88c77e859289463928b17b24f2f7ea99')
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place('Молдова')
        w = observation.weather
        w2 = w.temperature('celsius')['temp']
        print(w)
        print(w2)
        return "В даный момент температура " + str(w.temperature('celsius')['temp']) + '°' + '\n' + "В даный момент статус " + str(w.status) + '\n' + "В даный момент скорость ветра " + str(w.wind()['speed'])  + 'm/s' + '\n' + "В даный момент влажность " + str(w.humidity)+ '%'

    def Wther():
        owm = OWM('88c77e859289463928b17b24f2f7ea99')
        mgr = owm.weather_manager()
    
        observation = mgr.weather_at_place('Молдова')
        w = observation.weather
        w2 = w.temperature('celsius')['temp']
        print(w)
        print(w2)
        return "В даный момент " + str(w.humidity)+ '%'

def image():
    file = open('Img.txt', 'r')
    text = file.read()

    img = text.split('#')
    j = len(img)
    k = j - 1
    r = random.randint(0, k)
    return str(img[r])

