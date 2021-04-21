import discord
import asyncio
from discord.ext import commands
import tictactoe2
import random
import os
import connnect4
import time
from datetime import datetime
from discord import Embed

bot = commands.Bot(description = 'Mini Games Bot\nYour Discord Gaming Bot ...' , command_prefix = '<<')
bot.remove_command("help")

#########
#non bot functions :
def replacenums(s) :
    dic = {
    '1' : ':one:','2':':two:','3':':three:','4':':four:','5':':five:','6':':six:','7':':seven:','8':':eight:','9':':nine:' , 'X':':x:','O':':o:'
    }#'a': ':regional_indicator_a:', 'p2': '  ', 'c': ':regional_indicator_c:', 'p1': '  ', 'e': ':regional_indicator_e:', 'd': ':regional_indicator_d:', 'g': ':regional_indicator_g:', 'f': ':regional_indicator_f:', 'i': ':regional_indicator_i:', 'h': ':regional_indicator_h:', 'k': ':regional_indicator_k:', 'j': ':regional_indicator_j:', 'l': ':regional_indicator_l:', 'b': ':regional_indicator_b:'}
    dicc = ['1','2','3','4','5','6','7','8','9','X','O']#,'p1','a','b','c','d','e','f','p2','g','h','i','j','k','l']
    for i in range(len(dicc)) :
        s = s.replace(dicc[i],dic[dicc[i]])
    return s
########
yup = ('yes')
nup = ('no')
coders = ('270898185961078785')
########

@bot.event
async def on_ready() :
    await bot.change_presence(game=discord.Game(name='with <<help | <<invite ',type=0))
    print('Ready to Rock ...')

@bot.command(pass_context = True )
async def ping(ctx,n=1) :
    if n >=5 : n=5
    for i in range(n):
        em = Embed(title = 'Pong !', description = 'in ...' , colour = int(hex(random.randint(0,16777215)),16))
        em.set_thumbnail( url =  ctx.message.author.avatar_url)
        ms = await bot.say(embed = em )


@bot.command(pass_context = True )
async def bugreport(ctx) :
    now = str(datetime.now())
    bug = str(ctx.message.content).replace('<<bugreport','')
    if bug == '' :
        s = '<<bugreport "complain" \n To report bug / report / complain / suggestion / request / advice / contribution \n E.g. <<bugreport swat the bug dev before bug swats us'
        await bot.say(embed = Embed(title = 'Use correct syntax ^_^' , description = s ,  colour = int(hex(random.randint(0,16777215)),16)))
        return
    with open('reports.txt','a') as bf :
        bf.write('\n'+now+' : '+str(ctx.message.author)+' : '+bug)
    await bot.send_message(ctx.message.author,'Thank You for your valuable feedback ...\nThe Devs will surely work upon your Request\nKeep screenshots ready for our convenience\nFor more information You may also join our server ... \nhttps://discord.gg/mXucKTH')
    bf.close()

@bot.command(pass_context = True )
async def todayreport(ctx) :
    if str(ctx.message.author.id) in coders :
        now = str(datetime.now())
        bug = str(ctx.message.content).replace('<<todayreport','')
        with open('todayreport.txt','a') as bf :
            bf.write('\n'+now+' : '+bug)
        await bot.send_message(ctx.message.author,'Gud Job!\nKeep Going')
        await bot.delete_message(ctx.message)
        bf.close()

@bot.command(pass_context = True)
async def help(ctx) :
    try :
        ccd = str(ctx.message.content).replace('<<help','')
        ccd = ccd.split()
        with open('help2.txt','r') as hp :
            h = hp.readlines()
        ccd = ccd[0]
        msg = []
        for x in range(len(h)):
            if ccd in h[x] :
                mm = (h[x]).split(':')
                msg.append('**'+mm[0]+'**\t:\t'+mm[1])
        if msg == [] :
            em = discord.Embed(colour = int(hex(random.randint(0,16777215)),16))
            em.description = 'No help Found !!!\nTry Correct command ...'
            await bot.say(embed = em)
            return
        em = discord.Embed(title = '__MiniGames Bot help on \''+ccd+'\' :__',colour = int(hex(random.randint(0,16777215)),16))
        em.description = str(''.join(msg))
        await bot.say(embed = em)
        hp.close()

    except :
        with open('help.txt') as hf :
            x = hf.readlines()
        em = discord.Embed(title = 'MiniGames Help Menu :' , colour = int(hex(random.randint(0,16777215)),16))
        em.set_footer(text="Use <<help [command] for more info ...\ne.g. <<help rps")
        for i in range(len(x)):
            xf = x[i].split(':')
            em.add_field(name=xf[0] , value= xf[1])
        await bot.say(embed = em )
        hf.close()

@bot.command()
async def invite() :
    s = 'To conduct Mini Games in your server ,\nClick following link :\nhttps://discordapp.com/oauth2/authorize?client_id=321134463675400192&scope=bot&permissions=11328 \n\nPlease Co-Operate with Bot by giving necessary perms to improve gameplay ^_^ , \n\n**Thanks for support and love you shower us ...**'
    await bot.say(embed = Embed(description = s ,  colour = int(hex(random.randint(0,16777215)),16)))

@bot.command(pass_context = True)
async def servers(ctx):
    msg = str(ctx.message.content).replace("<<servers","")
    server_amount = 0
    servers = []
    for server in bot.servers:
        servers.append(server.name)
        server_amount += 1
    if 'list' in msg : em = discord.Embed(title = "I am in '%s' servers!" % (server_amount),description = '__**Server List :**__\n'+"%s" % ("\n".join(servers)), colour = int(hex(random.randint(0,16777215)),16))
    elif 'find' in msg :
        msg = (msg.replace('find','')).split()
        if msg[0] in servers : em = discord.Embed(title = 'Server Found :grin:',  colour = int(hex(random.randint(0,16777215)),16))
        else : em = discord.Embed(title = 'Server Not Found :no_mouth:',  colour = int(hex(random.randint(0,16777215)),16))
    else : em = discord.Embed(title = "I am in %s servers!" % (server_amount),  colour = int(hex(random.randint(0,16777215)),16))
    await bot.say(embed = em )

@bot.command(pass_context = True)
async def rps(ctx) :
    msg = None
    gmchannelid = str(ctx.message.channel.id)
    wins = {'r':'p','p':'s','s':'r'}
    symbol = {'p':':hand_splayed:','r':':fist:','s':':v:'}
    try :
        rules = 'The further game will occur in bot DM and playground !\nAs soon as u see Game x of y on the playground , you enter \'R\'/\'P\'/\'S\' your option in Bot DM !\nThe result will be in playground !\nHave Fun ^_^!!!'
        botg = False
        plyr = (ctx.message.content).replace('<<rps','')
        plyr = plyr.split()
        try :
            plyrid = str(plyr[0]).replace('<@','').replace('>','')
        except :
            botg = True
            plyrid = '321134463675400192'

        ########
        def check(mssg):
            if '!'+str(mssg.author.id) == plyrid or str(mssg.author.id) == plyrid and str(mssg.author.id) != '321134463675400192' or str(mssg.author.id) == str(ctx.message.author.id) or '!' + str(mssg.author.id) == str(ctx.message.author.id):
                return True
            return False
        ########
        if plyrid == '321134463675400192'  or plyrid == '!'+str(ctx.message.author.id) :
            botg = True
            em = discord.Embed(title = 'Lets Bot play !',  colour = int(hex(random.randint(0,16777215)),16))
            msg = await bot.say(embed = em )
        else :
            em = discord.Embed(description = '{} are u ready to Play ? \ntype \'yes\' to confirm !!!'.format(plyr[0]),  colour = int(hex(random.randint(0,16777215)),16))
            xx = await bot.say(embed = em )
            msg = await bot.wait_for_message(content = 'yes',timeout = 10,check = check)
            if msg == None or msg.author == ctx.message.author :
                botg = True
                em = discord.Embed(description = 'Lets Bot play !',  colour = int(hex(random.randint(0,16777215)),16))
                msg = await bot.say(embed = em )
        em = discord.Embed(description = 'How many Games ?',  colour = int(hex(random.randint(0,16777215)),16))
        mx = await bot.say(embed = em )
        ss = await bot.wait_for_message(timeout = 10, check = check)
        try :
            n = int(ss.content)
            if n >= 15 :
                n = 15
            elif n == 0 :
                em = discord.Embed(description = 'XXX**Game Over**XXX',  colour = int(hex(random.randint(0,16777215)),16))
                xx = await bot.say(embed = em )
        except :
            n = 1
        if not botg : await bot.delete_message(ss)
        em = discord.Embed(description = 'Game On!',  colour = int(hex(random.randint(0,16777215)),16))
        temp1 = await bot.say(embed = em )
        i = 1 ; p1win ,p2win = 0 , 0
        em = discord.Embed(description = rules,  colour = int(hex(random.randint(0,16777215)),16))
        rls = await bot.say(embed = em )
        await bot.delete_message(mx)
        while i <= n :
            choices = ['r','p','s']
            em = discord.Embed(title = '***Rock Paper Scissors***',  colour = int(hex(random.randint(0,16777215)),16))
            temp1 = await bot.send_message(ctx.message.channel , embed = em )
            em = discord.Embed(title = 'Game {0} of {1} :'.format(i,n),  colour = int(hex(random.randint(0,16777215)),16))
            temp = await bot.send_message(ctx.message.author, embed = em) if not botg else await bot.send_message(ctx.message.channel, embed = em)
            ch1 = await bot.wait_for_message(author = ctx.message.author)
            while str(ch1.content).lower() not in choices:
                await bot.delete_message(temp)
                await bot.delete_message(ch1)
                em = discord.Embed(title = 'Again {}'.format(ch1.author.display_name),  colour = int(hex(random.randint(0,16777215)),16))
                temp = await bot.send_message(ch1.author,embed = em) if not botg else await bot.send_message(ch1.channel, embed = em)
                ch1 = await bot.wait_for_message(author = ch1.author)
            await bot.delete_message(temp)
            await bot.delete_message(ch1)
            if botg == False :
                try : await bot.delete_message(ch2)
                except : pass
                em = discord.Embed(title = 'Game {0} of {1} :'.format(i,n),  colour = int(hex(random.randint(0,16777215)),16))
                temp = await bot.send_message(msg.author, embed = em)
                ch2 = await bot.wait_for_message(author = msg.author)
                while str(ch2.content).lower() not in choices :
                    await bot.delete_message(temp)
                    await bot.delete_message(ch2)
                    em = discord.Embed(title = 'Again {}'.format(ch2.author.display_name),  colour = int(hex(random.randint(0,16777215)),16))
                    temp = await bot.send_message(ch2.author,embed = em)
                    ch2 = await bot.wait_for_message(author = ch2.author)
                await bot.delete_message(temp)
            else :
                ch = random.choice(choices)
                em = discord.Embed(title = ch.upper(),  colour = int(hex(random.randint(0,16777215)),16))
                ch2 = await bot.say(embed = em)
            if not botg : ch = (ch2.content).lower()
            else : ch = ch
            await bot.delete_message(ch2)
            cc = (ch1.content).lower()
            em = discord.Embed(title = 'Game {0} of {1} :'.format(i,n) , description = '{0} X {1}'.format(symbol[cc],symbol[ch]),  colour = int(hex(random.randint(0,16777215)),16))
            await bot.say(embed = em)
            if ch == wins[cc] :
                p2win +=1
            elif cc == wins[ch] :
                p1win +=1
            i+=1
            try :
                await bot.delete_message(ll)
            except :
                pass
            em = discord.Embed(description = 'Score is :\n\'{0} {1}\' **:** \'{2} {3}\''.format(ctx.message.author.display_name,str(p1win),msg.author.display_name,str(p2win)),  colour = int(hex(random.randint(0,16777215)),16))
            ll = await bot.say(embed = em)
            await bot.delete_message(temp1)
        if p1win > p2win :
            winner,loser = ctx.message.author , msg.author
            if botg :
                winner = ctx.message.author
        elif p2win > p1win :
            winner,loser = msg.author , ctx.message.author
        else :
            em = discord.Embed(title = 'Its a Draw',  colour = int(hex(random.randint(0,16777215)),16))
            await bot.say(embed = em )
            em = discord.Embed(title = 'Game Over' ,  colour = int(hex(random.randint(0,16777215)),16))
            await bot.say(embed = em )
            return
        try :
            await bot.delete_message(rls)
        except :
            pass
        em = discord.Embed(title = ':boom:**{}** wins!'.format(winner.display_name),  colour = int(hex(random.randint(0,16777215)),16))
        await bot.say(embed = em )
        if not botg :
            em = discord.Embed(title = ':sparkles:Congo! you win !!!!',  colour = int(hex(random.randint(0,16777215)),16))
            await bot.send_message(winner , embed = em)
            em = discord.Embed(title = 'Good Game \nSadly you Lose , Better Luck Next time !!!!',  colour = int(hex(random.randint(0,16777215)),16))
            await bot.send_message(loser , embed = em)
        em = discord.Embed(title = 'Game Over' ,  colour = int(hex(random.randint(0,16777215)),16))
        await bot.say(embed = em )
    except :
        em = discord.Embed(title = 'Unfortunately !!! Some Error Occured', description = 'Maybe the Bot requires some Permissions(Manage Messages) ...\n Sorry for inconvinience ...\n Do Try again ^_^ ',  colour = int(hex(random.randint(0,16777215)),16))
        await bot.say(embed = em )

@bot.command(pass_context = True)
async def tictactoe(ctx) :
    sym = ['X','O']
    msg = None
    try :
        em = discord.Embed(description = 'Player 1 is **{}**:\nWhat symbol would you like to choose \'X\' or \'O\' ?'.format(ctx.message.author.display_name),  colour = int(hex(random.randint(0,16777215)),16))
        xx = await bot.say(embed = em )
        sym1 = await bot.wait_for_message(author = ctx.message.author)
        while (sym1.content).upper() not in sym :
            await bot.delete_message(xx)
            await bot.delete_message(sym1)
            em = discord.Embed(description = 'Choose \'X\' or \'O\' !!!',  colour = int(hex(random.randint(0,16777215)),16))
            await bot.say(embed = em )
            sym1 = await bot.wait_for_message(author = ctx.message.author)
        sym1 = (sym1.content).upper()
        sym.remove(sym1)
        plyr1 = tictactoe2.player(str(sym1),ctx.message.author.display_name)
        botg = False
        plyr = (ctx.message.content).replace('<<tictactoe','')
        plyr = plyr.split()
        try :
            plyrid = str(str(plyr[0]).replace('<@','').replace('>',''))
        except :
            botg = True
            plyrid = '321134463675400192'

        ########
        def check(mssg):
            if '!'+str(mssg.author.id) == plyrid or str(mssg.author.id) == plyrid and str(mssg.author.id) != '321134463675400192' or  str(mssg.author.id) == str(ctx.message.author.id) or '!' + str(mssg.author.id) == str(ctx.message.author.id):
                return True
            return False
        ########
        if plyrid == '321134463675400192'  or plyrid == '!' +str(ctx.message.author.id) and botg == False :
            botg = True
            em = discord.Embed(description = 'Lets Bot play !',  colour = int(hex(random.randint(0,16777215)),16))
            msg = await bot.say(embed = em )
        else :
            em = discord.Embed(description = '{} are u ready to Play ? \ntype \'yes\' to confirm !!!'.format(plyr[0]),  colour = int(hex(random.randint(0,16777215)),16))
            xx = await bot.say(embed = em )
            msg = await bot.wait_for_message(content = 'yes',timeout = 20,check = check)
            if msg == None or msg.author == ctx.message.author :
                botg == True
                em = discord.Embed(description = 'Lets Bot play !',  colour = int(hex(random.randint(0,16777215)),16))
                msg = await bot.say(embed = em )
        em = discord.Embed(description = 'Player 2 is **{0}**:\n{0} you get an \'{1}\'\n*Ready to play!*'.format(msg.author.display_name,sym[0]),  colour = int(hex(random.randint(0,16777215)),16))
        await bot.say(embed = em )
        plyr2 = tictactoe2.player(str(sym[0]),msg.author.display_name)
        brrd = tictactoe2.board()
        new = str(brrd.drawbrd(plyr1,plyr2))
        new = replacenums(new)
        em = discord.Embed(description = new,  colour = int(hex(random.randint(0,16777215)),16))
        old = await bot.say(embed = em )
        while brrd.left != [] :
            em = discord.Embed(title = '{}\'s move :'.format(plyr1.name),  colour = int(hex(random.randint(0,16777215)),16))
            xx = await bot.say(embed = em )
            mv = await bot.wait_for_message(author = ctx.message.author)
            while str(mv.content) not in brrd.left :
                await bot.delete_message(mv)
                await bot.delete_message(xx)
                em = discord.Embed(title = 'Again ! {}'.format(plyr1.name),  colour = int(hex(random.randint(0,16777215)),16))
                xx = await bot.say(embed = em )
                mv = await bot.wait_for_message(author = ctx.message.author)
            plyr1.move(str(mv.content),brrd)
            await bot.delete_message(mv)
            await bot.delete_message(xx)
            new = str(brrd.drawbrd(plyr1,plyr2))
            new = replacenums(new)
            await bot.delete_message(old)
            em = discord.Embed(description = new,  colour = int(hex(random.randint(0,16777215)),16))
            old = await bot.say(embed = em )
            if plyr1.is_win() :
                em = discord.Embed(description = ':sparkles:Winner is {}'.format(plyr1.name),  colour = int(hex(random.randint(0,16777215)),16))
                await bot.say(embed = em )
                return
            if brrd.left == [] :
                em = discord.Embed(title = 'Its a Draw',  colour = int(hex(random.randint(0,16777215)),16))
                await bot.say(embed = em )
                em = discord.Embed(title = 'Game Over' ,  colour = int(hex(random.randint(0,16777215)),16))
                await bot.say(embed = em )
                return
            em = discord.Embed(title = '{}\'s move :'.format(plyr2.name),  colour = int(hex(random.randint(0,16777215)),16))
            xx = await bot.say(embed = em )
            if botg == True :
                lmn = tictactoe2.play(plyr1,brrd)
                em = discord.Embed(title = lmn,  colour = int(hex(random.randint(0,16777215)),16))
                mv = await bot.say(embed = em )
            else :
                mv = await bot.wait_for_message(author = msg.author)
                lmn = str(mv.content)
                while str(mv.content) not in brrd.left :
                    await bot.delete_message(mv)
                    await bot.delete_message(xx)
                    em = discord.Embed(title = 'Again ! {}'.format(plyr2.name),  colour = int(hex(random.randint(0,16777215)),16))
                    xx = await bot.say(embed = em )
                    mv = await bot.wait_for_message(author = msg.author)
                    lmn = str(mv.content)
            plyr2.move(str(lmn),brrd)
            await bot.delete_message(mv)
            await bot.delete_message(xx)
            new = str(brrd.drawbrd(plyr1,plyr2))
            new = replacenums(new)
            await bot.delete_message(old)
            em = discord.Embed(description = new,  colour = int(hex(random.randint(0,16777215)),16))
            old = await bot.say(embed = em )
            if plyr2.is_win() :
                em = discord.Embed(description = ':sparkles:Winner is {}'.format(plyr2.name),  colour = int(hex(random.randint(0,16777215)),16))
                await bot.say(embed = em )
                break
        em = discord.Embed(title = 'Game Over'.format(plyr1.name),  colour = int(hex(random.randint(0,16777215)),16))
        await bot.say(embed = em )
    except :
        em = discord.Embed(title = 'Unfortunately !!! Some Error Occured \n Maybe the Bot requires some Permissions(Manage Messages) ...\n Sorry for inconvinience ...\n Do Try again ^_^ ',  colour = int(hex(random.randint(0,16777215)),16))
        await bot.say(embed = em )

bot.run('MzIxMTM0NDYzNjc1NDAwMTky.DBZoKg.Jl1g867szwWoNQJoAd8KKSZYhPE')
# bot.run('NDk3Mzk4ODE4NDg1MTc0Mjcy.DpesEQ.ixPA3lLa_pe-lxOBe7Y5l9qYUjU')


'''
embed = discord.Embed(title="title ~~(did you know you can have markdown here too?)~~", colour=discord.Colour(0x34e25a), url="https://discordapp.com", description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```", timestamp=datetime.datetime.utcfromtimestamp(1507173831))

em.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
em.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
em.set_author(name="author name", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
em.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

em.add_field(name="🤔", value="some of these properties have certain limits...")
em.add_field(name="😱", value="try exceeding some of them!")
em.add_field(name="🙄", value="an informative error should show up, and this view will remain as-is until all issues are fixed")
em.add_field(name="<:thonkang:219069250692841473>", value="these last two", inline=True)
em.add_field(name="<:thonkang:219069250692841473>", value="are inline fields", inline=True)

await bot.say(content="this `supports` __a__ **subset** *of* ~~markdown~~ 😃 ```js\nfunction foo(bar) {\n  console.log(bar);\n}\n\nfoo(1);```", embed=embed)'''
