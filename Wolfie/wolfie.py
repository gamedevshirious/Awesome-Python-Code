import discord
import pprint
import asyncio
import time
import random
from discord.ext import commands
import sqlite3 as sql
'''
with open('birthdays.txt','r+') as bf :
    f = bf.readlines()'''

# jugaad / life hacks
# google
# remember people
# ai
# trouble shooter
# notes

wolfi = sql.connect("wolfie_memory.db")
w = wolfi.cursor()

# w.execute('Create table be(word varchar(50)) ; ')
# w.execute('Create table ques(word varchar(50)) ; ')

ids = ['270898185961078785']
greetings = ['Hi', 'O/', 'Hola', 'bonjour', 'hOi', 'Greetings', 'Namaskar']
greetmsg = ['Nice to meet you ^_^', 'How you doin ...',
            'WoW you exist ... O.O', 'Hope we go great together',
            'I bet you are Shirious\'s friend', 'Cool']
rms = ['find', 'greet', 'Hey', 'Wolfie', '   ', '  ']

wolfie = commands.Bot(description='Wolfie', command_prefix='//',
                      )

###############################################################################

def remove(s):
    for i in range(len(rms)):
        s = s.replace(rms[i],'')
    return s

################################################################################

def parrot(trigg) :
    for i in w.execute('select * from be ;') :
        a = i
    for i in w.execute('select * from ques ;'):
        q = i
    for i in range(len(a)) :
        trigg = trigg.replace(a[i],'')
    ss = trigg.split()
    return str(random.choice(q))+' '+str(str(random.choice(a)))+' ?'

@wolfie.event
async def on_ready() :
    await wolfie.change_presence(game=discord.Game(name='with ...',type=0))
    print('Ready to Rock ...')

@wolfie.command(pass_context = True )
async def ping(ctx) :
    print(ctx.message.author.id)
    mx = await wolfie.say(":sparkles:Pong")
    time.sleep(5)
    await wolfie.delete_message(mx)

@wolfie.command(pass_context = True)
async def insert(ctx) :
    mssg = ctx.message.content
    mssg = mssg.split()
    mssg.pop(0)
    tb,wr = mssg[0],mssg[1]
    w.execute("Insert into {0} values('{1}')".format(str(tb),str(wr)))
    wolfi.commit()
    await wolfie.delete_message(ctx.message)

@wolfie.command(pass_context = True)
async def show(ctx) :
    mssg = ctx.message.content
    mssg = mssg.split()
    mssg.pop(0)
    for i in w.execute("select * from {}".format(mssg[0])) :
        msg = i
    await wolfie.say(msg)
    await wolfie.delete_message(ctx.message)

@wolfie.event
async def on_message(msg) :
    if str(msg.author.id) in ids :
        if 'find' in str(msg.content) :
            s = remove(str(msg.content))
            s = s.replace(' ','')
            s = str(eval(s))
            await wolfie.send_message(msg.channel,s)
        if 'greet' in str(msg.content) :
            s = remove(str(msg.content))
            g = str(greetings[int(random.randint(0,greetings))])
            m = str(greetmsg[int(random.randint(0,greetmsg))])
            g = g +' , '+ s +'\n' +m
            await wolfie.send_message(msg.channel,g)
        await wolfie.process_commands(msg)
    if '..' in msg.content :
        await wolfie.send_message(msg.channel,parrot(msg.content))

import requests
import bs4 as bs


@wolfie.command(pass_context = True)
async def pkl_score(ctx):
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 \
            http://notifyninja.com/monitoring'}

    url = "https://www.sportskeeda.com/go/pro-kabaddi"
    data = []
    data = requests.get(url, headers=head)
    soup = bs.BeautifulSoup(data.text, "lxml")
    datax, flag = [], 0
    data2 = soup.get_text()
    data2 = str(data2).split("\n")

    for i in range(len(data2)):
        if "Zone " in str(data2[i]):
            datax.append(data2[i])
            datax.append(data2[i+4])
            datax.append(data2[i+5])
            datax.append(data2[i+9])
            datax.append(data2[i+10])

    for i in range(5):
        datax.pop(0)
    data = []
    for i in range(0, 10, 5):
        data2 = []
        for j in range(5):
            data2.append(datax[i+j])
        data.append(data2)
    for dte in data:
        t, t1, t1s, t2, t2s = dte[::]
        w_em = discord.Embed(
            title=t,
            colour=int(hex(random.randint(0, 16777215)), 16)
        )
        w_em.add_field(name=str(t1), value=str(t1s))
        w_em.add_field(name=str(t2), value=str(t2s))
        await wolfie.say(embed=w_em)

# wolfie.run('Mjc0MDM4NjU2MDAyNjg2OTc2.DI1wSg.IGlgDbFHj7POiR6G7Uv04RdCcTQ',bot=False)
wolfie.run('NDQ3Mzk1NTEyNjYxMDQ5MzU0.Dpeq-w.N_QYBwjFB98KK_HG1kmMcJvJ_BI') # wolfie token
