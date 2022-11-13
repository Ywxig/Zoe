from ast import Await
import VFND
import random
import requests
from bs4 import BeautifulSoup

DoList = ['Сиотрю фильм', 'Читаю книгу', 'Смотрю новости', 'Изучаю новые материалы']
AllGood = ['У меня всё хорошо', 'Я чествую себя хорошо']
AllNormal = ['Всё норм', 'Я ок']
AllBad = ['Не хочю говорить', 'Я обижена']
Yas = ['Ага', 'Угу', 'Очень круто', 'Круто', 'OwO', 'UwU']
ItCoolL = ['Очень круто', 'Это круто', 'Это очень круто'] 
Ok = ['Ок', 'Хорошо']
You = ['ты', 'вы']
CoolNastroyL = ['Я за тебя рада! ', 'Это очень хорошо! ', 'Красава! ', 'Заибись ', 'Это очень классно ', 'Я очень рада ']
CoolNastroyLTo = ['У меня, тоже хорошое настроение ', 'У гениев мысли сходятся ', 'Я тоже круто себя чбвствую! ']
BadNastroyL = ['Не надо печялится', 'Не переживай я с тобой', 'Всё будет хорошо', 'Мы выдержем всё в месте']
BadNastroyLTo = ['У меня тоже плохое настроение', 'Как я тебя понимаю', 'Печялька']
Go = ["го", "Го", "Давай", "давай"]
LoveL = ['Я тебя тоже сильно люблю ', 'Ты, мой любимый лисик ', 'Я тебя обожаю! ', '']
GoShooll = ['Классно, удачи там', 'Удачи тебе, получи хорошую оценку', 'жду тебя после 2 чесов']
ToDoCreatL = ['Я запомнила ', 'Я записала ', 'Я забила стрелу ', 'Ок, заметка сделана']
GoodPointl = ['Вау ты отличьник, ', 'Хорошоя работа, ', 'Вот это супер, ', 'Так держать, ', "Прям как у меня, "]
GoodPointll = ['вернёшся домой с меня пиво', 'только не остонавливойся!', 'не смей завтра получить плохую оценку']
BadPointl = ['Это печально', 'Очень плохо', 'Да это провал', 'Кажется нам надрали задницу', "Блин!"]
NormalPointl = ['Не плохо', 'В следующий раз будь внимательние', 'Не так ужасно как могло быть', 'Я немного растроено', 'Ты мог бы и лудше справится']
TeatrL = ['Не хочю в театр', 'Я туда не пойду', 'Нет, лудше в лес', 'Что мне там делать?', "Неееа"]
ForestL = ['Да давай', 'Хмхихи, я согласна', 'Окей', 'Не буду против', "Хорошо"]
KinoL = ['Да давай', 'О, давай посмотрим ужастик', 'Да пошли на комедию', 'Нет возражений', "Хорошо"]
KoncertL= ['Не хочю', 'Я туда не пойду', 'Нет, кого там слушать?', 'Что мне там делать?', "Неееа"]
Rokmusicl = ['Да давай', 'Будет круто', 'Почимуб и нет', 'Класс, я иду', "Хорошо!!!"]
ExcursiunL = ['Ладно', 'Ок', 'Хорошо', 'Куда угодно я с тобой', 'Отличьно']
Pecnicl = ['Ладно', 'Ок', 'Хорошо', 'Куда угодно я с тобой', 'Отличьно']
WalkL = ['Хочещь погулять?', 'Дай 10 минут собратся', 'Окей, пошли', 'Давай я пойду', 'Давай в месте!']

class GoInto():
    def Teatr(Author):
        Awaite = TeatrL[RAND(4)]
        return Awaite

    def Forest(Author):
        Awaite = ForestL[RAND(4)]
        return Awaite

    def Kino(Author):
        Awaite = KinoL[RAND(4)]
        return Awaite

    def Koncert(Author):
        Awaite = KoncertL[RAND(4)]
        return Awaite

    def Rokmusic(Author):
        Awaite = Rokmusicl[RAND(4)]
        return Awaite

    def Excursiun(Author):
        Awaite = ExcursiunL[RAND(4)]
        return Awaite

    def Pecnic(Author):
        Awaite = Pecnicl[RAND(4)]
        return Awaite

    def Walk(Author):
        Awaite = WalkL[RAND(4)]
        return Awaite


def NormalPoint(Author):
    Awaite = str(Author) + ' ' + NormalPointl[RAND(4)]
    return Awaite

def BadPoint(Author):
    Awaite = str(Author) + ' ' + BadPointl[RAND(4)]
    return Awaite

def GoodPoint(Author):
    Awaite = str(Author) + ' ' + GoodPointl[RAND(4)] + ' ' +  GoodPointll[RAND(2)]
    return Awaite

def ToDoCreat(Author):
     Awaite = ToDoCreatL[RAND(3)] + ' ' + str(Author)
     return Awaite

def RAND(j):
    return random.randint(0, j)

def Hello(Author):
    Cof = RAND(1)
    if Cof == 0:
        Awaite = VFND.HELLO[RAND(3)] + ' ' + VFND.QATION[RAND(1)] + ' ' + str(Author)

    if Cof == 1:
        Awaite = VFND.HELLO[RAND(3)] + ' ' + str(Author)
    
    return str(Awaite)

def GoShool(Author):
    Awaite = GoShooll[RAND(2)] + ' ' + str(Author)
    return str(Awaite)

def Bay(Author):
    Awaite = VFND.BAY[RAND(2)] + ' ' + str(Author)
    return str(Awaite)

def GoodNight(Author):
    Awaite = 'Спокойной ночи ' + str(Author)
    return str(Awaite)   

def GoodMoning(Author):
    Awaite = str.capitalize(VFND.GOODMONING[RAND(2)]) + ' доброе ' + str(Author)
    return str(Awaite)

def WeWellCome(Author):
    Cof = RAND(1)
    if Cof == 0:
        Awaite = 'Пожалйста ' + str(Author)
    if Cof == 1:
        Awaite = 'Я рада что смогла помочь ' + str(Author)
    return str(Awaite)

def WhatDo(Author):
    Awaite = DoList[RAND(3)] + ' ' + str(Author)
    return str(Awaite)

def ItIsCool(Author):
    Awaite = str.capitalize(ItCoolL[RAND(3)]) + ', ' + str(Author)
    return str(Awaite)    

def WhatYou(Author, Nastroy):
    if Nastroy > 0.0:
        Awaite = AllGood[RAND(1)] + ' ' + str(Author)
    if Nastroy < 0.0:
        Awaite = AllNormal[RAND(1)] + ' ' + str(Author)
    if Nastroy < -1.0:
        Awaite = AllBad[RAND(1)] + ' '  + str(Author)
    return str(Awaite)

def CoolNastroy(Author, Nastroy):
    if Nastroy > 0.0:
        Awaite = CoolNastroyL[RAND(5)] + ' ' + str(Author)
    if Nastroy == 1.0:
        Awaite = CoolNastroyLTo[RAND(5)] + ' ' + str(Author)
    if Nastroy < 0.0:
        Awaite = Ok[RAND(1)] + ' ' + str(Author)
    return str(Awaite)

def BadNastroy(Author, Nastroy):
    if Nastroy > 0.0:
        Awaite = BadNastroyL[RAND(3)] + ' ' + str(Author)
    if Nastroy < 0.0:
        Awaite = BadNastroyLTo[RAND(2)] + ' ' + str(Author)
    return str(Awaite)

def Cool(Author, Nastroy):
    if Nastroy > 0.0:
        Awaite = Yas[RAND(5)] + ' ' + str(Author)
    if Nastroy < 0.0:
        Awaite = Ok[RAND(1)] + ' ' + str(Author)
    return str(Awaite)
    
def WhoAreU(Author):
    Awtite = 'Кто ' + You[RAND(1)] + ' ' + str(Author)
    return Awtite

def GoSex(Author):
    file = open('Img.txt', 'r')
    text = file.read()
    img = text.split('#')
    j = len(img)
    k = j - 1
    r = random.randint(0, k)
    Awtite = Go[RAND(3)] + ' ' + str(Author) + '\n' + img[r]
    return Awtite    

def ILoovU(Author):
    Awtite = LoveL[RAND(1)] + ' ' + str(Author)
    return Awtite    


class UserData():

    def DataRead(Author):
        file = open('UserDats/' + str(Author) + '.txt', 'r')
        Text = file.read()
        Data = Text.split('%20')
        file.close()
        return Data
        
    def DataUpdate(Author, PointLove, PointFrend):
        file = open('UserDats/' + str(Author) + '.txt', 'w')
        Date = str(Author) + "%20" + str(PointLove) + "%20" + str(PointFrend)
        file.write(Date)
        file.close()       

    def Creat(Author):
        file = open('UserDats/' + str(Author) + '.txt', 'w')
        Date = str(Author)
        file.write(Date)
        file.close()
