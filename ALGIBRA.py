import discord
from discord.ext import commands
import math

bot = commands.Bot(command_prefix='=')

@bot.command()
async def СУММ(ctx, a, b):
    rez = float(a) + float(b)
    await ctx.send(rez)

@bot.command()
async def ВЫЧИ(ctx, a, b):
    rez = float(a) - float(b)
    await ctx.send(rez)

@bot.command()
async def ДЕЛЕ(ctx, a, b):
    rez = float(a) / float(b)
    await ctx.send(rez)

@bot.command()
async def УМНО(ctx, a, b):
    rez = float(a) * float(b)
    await ctx.send(rez)

@bot.command()
async def СТЕП(ctx, a, b):
    rez = float(a) ** int(b)
    await ctx.send(rez)

@bot.command()
async def КВАДКОР(ctx, a):
    S = math.sqrt(float(a))
    await ctx.send(S)

@bot.command()
async def СИН(ctx, a):
    S = math.sin(float(a))
    await ctx.send(S)

@bot.command()
async def КОСИН(ctx, a):
    S = math.cos(float(a))
    await ctx.send(S)

@bot.command()
async def ТАН(ctx, a):
    S = math.tan(float(a))
    await ctx.send(S)

@bot.command()
async def ОКРУГ(ctx, a):
    S = math.ceil(float(a))
    await ctx.send(S)

@bot.command()
async def СРЕДЗНАЧЬ(ctx, c):
    a = c.split(',')
    b=[]
    for i in a: 
        b.append(int(i))
    print(b)
    rez = sum(b) / len(b)   
    await ctx.send(rez)
    
@bot.command()
async def ДИСК(ctx, a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    q = b ** 2
    dis = q - 4 * a * c
    if dis < 0:
        error = 'Уравнение не имеет корней'
        await ctx.send(error)

    if dis > 0:
        disq = math.sqrt(dis)
        x1a = -b -disq
        x1b = 2 * a
        x2a = -b +disq
        x2b = 2 * a
        await ctx.send(dis)
        await ctx.send("x1: " + str(x1a)+'/'+str(x1b))
        await ctx.send("x2: " + str(x2a)+'/'+str(x2b))
        
@bot.command()
async def ПРОП(ctx, a, b, c, d):

    if a == 'x':
        #a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        rez = b * c / d
        

    if b == 'x':
        a = float(a)
        #b = float(b)
        c = float(c)
        d = float(d)
        rez = a * d / c

    if c == 'x':
        a = float(a)
        b = float(b)
        #c = float(c)
        d = float(d)
        rez = a * d / b

    if d == 'x':
        a = float(a)
        b = float(b)
        c = float(c)
        #d = float(d)
        rez = b * c / a

    await ctx.send(rez)

@bot.command()
async def ИСЛЕДПОРАБ(ctx, a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    q = b ** 2
    dis = q - 4 * a * c
    if dis < 0:
        error = 'Уравнение не имеет корней'
        await ctx.send(error)

        await ctx.send("Вершина: " + '(' + str(Vx) + ';' + str(Vy) + ')')
        await ctx.send("Нули фукции: ∅")
        await ctx.send("Экстремул: " + EX + ' f(' + str(Vx) + ') = ' + str(Vy) + '\n x∈R')

    if dis > 0:
        disq = math.sqrt(dis)
        x1a = -b -disq
        x1b = 2 * a
        x2a = -b +disq
        x2b = 2 * a

        Vx = b / 2 * a
        Vy = dis / 4 * a
        #Vy = Vy * -1

        if Vx > 0:
            EX = 'Max'

        if Vx < 0:
            EX = 'Min'

            

        await ctx.send("Вершина: " + '(' + str(Vx) + ';' + str(Vy) + ')')
        await ctx.send("Нули фукции: " + str(x1a)+'/'+str(x1b) + ";" + str(x2a)+'/'+str(x2b))
        await ctx.send("Экстремул: " + EX + ' f(' + str(Vx) + ') = ' + str(Vy) + '\n x∈R')



bot.run('OTA0MDA1ODY5MjI0NzU1MjQw.YX1PEg.bLEeiyoaK8RIc5b8YHVRQt4QQUQ')
