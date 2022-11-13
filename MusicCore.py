import requests
from bs4 import BeautifulSoup
import random
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import random

def music(Author):
    Arr = ['Го, послушаем музыку ', 'Вот ', 'Музыка: ']
    r = random.randint(0, 2)
    Awite = Arr[r] + str(Author)
    return Awite


def UWMM(Author):
    Arr = ['Вот мой альбом ', 'Хочешь послушать мою музыку ', 'На мой альбом ']
    r = random.randint(0, 2)
    Awite = Arr[r] + str(Author)
    return Awite

class MyLib():

    def GetAlbum(Name):
        file = open(str(Name) + 'txt', 'r')
        Content = file.read()
        Albums = Content.split('%20')
        return Albums

    def AddAlbem(Name, Album):        
        file = open(str(Name) + 'txt', 'a')
        file.write(str(Album))