import discord
import VFND
import BC_Core as bc
import ToolsKit as tool
import MusicCore as music
import random
import ManyCore as many

T = open('TOKEN.txt', 'r')
TOKEN = str(T.read())

INTIM = ['фотки', 'Интимки', 'имнтинки']

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
            Author = message.author
            for i in ms_l:

                if i in VFND.HELLO:
                    try:
                        UserList = bc.UserData.DataRead(Author)
                        if bc.UserData.DataRead(Author) != '':
                            await message.channel.send(bc.Hello(Author) + tool.emodji('class_heppy'))
                        
                        else:
                            await message.channel.send(bc.WhoAreU(Author))
                            bc.UserData.DataUpdate(Author, '0.0', '0.1')
                    except:
                        await message.channel.send(bc.WhoAreU(Author))
                        bc.UserData.DataUpdate(Author, '0.0', '0.1')

                if i in VFND.IMGET:
                    for j in ms_l:
                        if j in VFND.GOODPOINT:
                            await message.channel.send(bc.GoodPoint(Author) + tool.emodji('class_work')  + tool.emodji('class_heppy')  + tool.emodji('class_love'))

                        if j in VFND.BADPOINT:
                            await message.channel.send(bc.BadPoint(Author) + tool.emodji('class_bad') + tool.emodji('class_bad'))

                        if j in VFND.NORMALPOINT:
                            await message.channel.send(bc.NormalPoint(Author) + tool.emodji('class_heppy'))

                if i in VFND.BAY:
                    await message.channel.send(bc.Bay(Author))               

                if i in VFND.GOODMONING:
                    await message.channel.send(bc.GoodMoning(Author))

                if i in VFND.GOODNIGHT:
                    await message.channel.send(bc.GoodNight(Author) + tool.emodji('class_sleep'))


                if i in VFND.GO or i in VFND.DOGOSE:
                    for j in ms_l:

                        if j in VFND.GAME:
                            await message.channel.send(VFND.GO[random.randint(0, 3)] + tool.emodji('class_cool') + tool.emodji('class_game') + tool.emodji('class_game'))

                        if j in VFND.SHOTSTAND:
                            await message.channel.send(VFND.GO[random.randint(0, 3)] + tool.emodji('class_cool') + tool.emodji('class_heppy') + tool.emodji('class_game'))

                        if j in VFND.WALK:
                            await message.channel.send(bc.GoInto.Walk(Author) + tool.emodji('class_heppy'))

                        if j in VFND.TEATR:
                            await message.channel.send(str(bc.GoInto.Teatr(Author)) + tool.emodji('class_bad') + tool.emodji('class_sleep'))

                        if j in VFND.EXCURSION:
                            await message.channel.send(bc.GoInto.Excursiun(Author) + tool.emodji('class_heppy'))

                        if j in VFND.FOREFT:
                            await message.channel.send(bc.GoInto.Forest(Author) + tool.emodji('class_heppy'))

                        if j in VFND.PECNINK:
                            await message.channel.send(bc.GoInto.Pecnic(Author) + tool.emodji('class_bad'))

                        if j in VFND.KINO:
                            await message.channel.send(bc.GoInto.Kino(Author) + tool.emodji('class_heppy'))

                        if j in VFND.KONCERT:
                            for k in ms_l:
                                if k in VFND.ROKMUSIC:
                                    await message.channel.send(bc.GoInto.Rokmusic(Author) + tool.emodji('class_heppy'))
                                else:
                                    await message.channel.send(bc.GoInto.Koncert(Author) + tool.emodji('class_bad'))

                        if j in VFND.PARS:
                            for k in ms_l:
                                if k in VFND.PORN:
                                    UserList = bc.UserData.DataRead(Author)
                                    Nastroi = float(UserList[2])
                                    await message.channel.send(tool.Parser.Porn())

                        if j in VFND.SEX:
                            UserList = bc.UserData.DataRead(Author)
                            Nastroi = float(UserList[2])
                            await message.channel.send(bc.GoSex(Author))

                if i in VFND.WEWELLCOM:
                    await message.channel.send(bc.WeWellCome(Author))
                    
                if i in VFND.YOURSELF:
                    for j in ms_l:
                        if j in VFND.WHATYOU:
                            UserList = bc.UserData.DataRead(Author)
                            Nastroi = float(UserList[2])
                            await message.channel.send(bc.WhatYou(Author, Nastroi))

                if i in VFND.IT:
                    for j in ms_l:
                        if j in VFND.COOL:
                            UserList = bc.UserData.DataRead(Author)
                            Nastroi = float(UserList[2])
                            await message.channel.send(bc.ItIsCool(Author))                    

                if i in VFND.WHATDO:
                    await message.channel.send(bc.WhatDo(Author))

                if i in VFND.WATCH:
                    await message.channel.send(tool.Parser.Kino())

                if i in VFND.READ:
                    for j in ms_l:
                        if j in VFND.STATS:
                            await message.channel.send(tool.Parser.StopGameRu())

                if i in VFND.COMPLUMENTS:
                    User = bc.UserData.DataRead(Author)
                    bc.UserData.DataUpdate(Author, float(User[1]) + 0.05, float(User[2]) + 0.1)
                    await message.channel.send(bc.ILoovU(Author) + tool.emodji('class_love')) 

                if i in VFND.TOO:
                    UserList = bc.UserData.DataRead(Author)
                    Nastroi = float(UserList[2])

                    if Nastroi > 0.0:
                        await message.channel.send(bc.CoolNastroy(Author, Nastroi) + tool.emodji('class_love'))       

                    if Nastroi <= 0.0:
                        await message.channel.send(bc.BadNastroy(Author, Nastroi) + tool.emodji('class_bad'))                     

                if i in VFND.MYSELF :
                    for k in ms_l:
                        if k in VFND.NASTROY or k in VFND.LIVE or k in VFND.ALL:
                            for j in ms_l:

                                if j in VFND.COOL:
                                    UserList = bc.UserData.DataRead(Author)
                                    Nastroi = float(UserList[2])
                                    await message.channel.send(bc.CoolNastroy(Author, Nastroi) + tool.emodji('class_cool'))       

                                if j in VFND.BAD:
                                    UserList = bc.UserData.DataRead(Author)
                                    Nastroi = float(UserList[2])
                                    await message.channel.send(bc.BadNastroy(Author, Nastroi) + tool.emodji('class_bad')) 

                if i in VFND.FORYOU:
                    await message.channel.send('Привет меня зовут Selene!\nЯ работаю бухгалтером и ПМ, у меня есть готовые протоколы для работы с доходами и расходами. я знаю готовые модели бюджета. Я могу помочь распределить деньги. Я буду фиксировать траты в специальный отчёт')   



                if i in VFND.DO or i in VFND.SAY:
                    for j in ms_l:

                        if j in VFND.TODO:
                            del ms_l[0]
                            del ms_l[0]
                            Many = ms_l[0]
                            del ms_l[0]
                            massge = ' '.join(ms_l)
                            many.Rooport.Write(str(Author) + '.txt', str(Author), '|', Many, str(massge))
                            await message.channel.send('Транзакция в учёте'  + tool.emodji('class_working'))

                        if j in VFND.ROOPORT:
                            await message.channel.send('Отчёт готов!\n')
                            try:
                                await message.channel.send(many.Rooport.Read(str(Author) + '.txt'))
                            except:
                                await message.channel.send('Прости но слешком большой список тран закций' + tool.emodji('class_happy'))

                if i in VFND.MUSIC:
                    for k in ms_l:
                        if k in VFND.ALBUM:
                            for j in ms_l:
                                if j in VFND.ZOEALBUM:
                                    await message.channel.send()
                                    Album = music.MyLib.GetAlbum('MyAlbem.txt')
                                    await message.channel.send(music.UWMM(Author))
                                    await message.channel.send(Album[1])

                if i in VFND.DROP:
                    for j in ms_l:

                        if j in INTIM:
                            await message.channel.send(tool.image())

                if i in VFND.SEARCH:

                    for j in ms_l:
                        if j in VFND.PORN:
                            del ms_l[0]
                            del ms_l[0]
                            del ms_l[0]
                            await message.channel.send(tool.Search.PornHub(ms_l))

                    for j in ms_l:
                        if j in VFND.GOOGLE:
                            del ms_l[0]
                            del ms_l[0]
                            del ms_l[0]
                            await message.channel.send(tool.Search.Googol(ms_l))

                        if j in VFND.YANDEX:
                            del ms_l[0]
                            del ms_l[0]
                            del ms_l[0]
                            await message.channel.send(tool.Search.Yandex(ms_l))

                        if j in VFND.YOUTUBE:
                            del ms_l[0]
                            del ms_l[0]
                            del ms_l[0]
                            await message.channel.send(tool.Search.Youtube(ms_l))


client = MyClient()
client.run(TOKEN)