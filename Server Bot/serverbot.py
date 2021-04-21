import discord
import asyncio
from discord.ext import commands
import random
import urbandictionary as ud
import os
import time
import sqlite3 as sql
from discord import Embed
from datetime import datetime
from time import localtime, strftime
import bs4 as bs
import requests
# bot = commands.Bot(command_prefix = '//')

# bot = commands.Bot(name = 'Pokemon Battle Bot' , command_prefix = '>>')
bot = commands.Bot(name = 'IU Server Bot' , command_prefix = '<@447395512661049354> ')

poks = ['bulbasaur','ivysaur','venusaur','charmander','charmeleon','charizard','squirtle','wartortle','blastoise','caterpie','metapod','butterfree','weedle','kakuna','beedrill','pidgey','pidgeotto','pidgeot','rattata','raticate','spearow','fearow','ekans','arbok','pikachu','raichu','sandshrew','sandslash','nidoran\ f','nidorina','nidoqueen','nidoran\ m','nidorino','nidoking','clefairy','clefable','vulpix','ninetales','jigglypuff','wigglytuff','zubat','golbat','oddish','gloom','vileplume','paras','parasect','venonat','venomoth','diglett','dugtrio','meowth','persian','psyduck','golduck','mankey','primeape','growlithe','arcanine','poliwag','poliwhirl','poliwrath','abra','kadabra','alakazam','machop','machoke','machamp','bellsprout','weepinbell','victreebel','tentacool','tentacruel','geodude','graveler','golem','ponyta','rapidash','slowpoke','slowbro','magnemite','magneton','farfetch\'d','doduo','dodrio','seel','dewgong','grimer','muk','shellder','cloyster','gastly','haunter','gengar','onix','drowzee','hypno','krabby','kingler','voltorb','electrode','exeggcute','exeggutor','cubone','marowak','hitmonlee','hitmonchan','lickitung','koffing','weezing','rhyhorn','rhydon','chansey','tangela','kangaskhan','horsea','seadra','goldeen','seaking','staryu','starmie','mr.\ mime','scyther','jynx','electabuzz','magmar','pinsir','tauros','magikarp','gyarados','lapras','ditto','eevee','vaporeon','jolteon','flareon','porygon','omanyte','omastar','kabuto','kabutops','aerodactyl','snorlax','articuno','zapdos','moltres','dratini','dragonair','dragonite','mewtwo','mew','chikorita','bayleef','meganium','cyndaquil','quilava','typhlosion','totodile','croconaw','feraligatr','sentret','furret','hoothoot','noctowl','ledyba','ledian','spinarak','ariados','crobat','chinchou','lanturn','pichu','cleffa','igglybuff','togepi','togetic','natu','xatu','mareep','flaaffy','ampharos','bellossom','marill','azumarill','sudowoodo','politoed','hoppip','skiploom','jumpluff','aipom','sunkern','sunflora','yanma','wooper','quagsire','espeon','umbreon','murkrow','slowking','misdreavus','unown','wobbuffet','girafarig','pineco','forretress','dunsparce','gligar','steelix','snubbull','granbull','qwilfish','scizor','shuckle','heracross','sneasel','teddiursa','ursaring','slugma','magcargo','swinub','piloswine','corsola','remoraid','octillery','delibird','mantine','skarmory','houndour','houndoom','kingdra','phanpy','donphan','porygon2','stantler','smeargle','tyrogue','hitmontop','smoochum','elekid','magby','miltank','blissey','raikou','entei','suicune','larvitar','pupitar','tyranitar','lugia','ho-oh','celebi','treecko','grovyle','sceptile','torchic','combusken','blaziken','mudkip','marshtomp','swampert','poochyena','mightyena','zigzagoon','linoone','wurmple','silcoon','beautifly','cascoon','dustox','lotad','lombre','ludicolo','seedot','nuzleaf','shiftry','taillow','swellow','wingull','pelipper','ralts','kirlia','gardevoir','surskit','masquerain','shroomish','breloom','slakoth','vigoroth','slaking','nincada','ninjask','shedinja','whismur','loudred','exploud','makuhita','hariyama','azurill','nosepass','skitty','delcatty','sableye','mawile','aron','lairon','aggron','meditite','medicham','electrike','manectric','plusle','minun','volbeat','illumise','roselia','gulpin','swalot','carvanha','sharpedo','wailmer','wailord','numel','camerupt','torkoal','spoink','grumpig','spinda','trapinch','vibrava','flygon','cacnea','cacturne','swablu','altaria','zangoose','seviper','lunatone','solrock','barboach','whiscash','corphish','crawdaunt','baltoy','claydol','lileep','cradily','anorith','armaldo','feebas','milotic','castform','kecleon','shuppet','banette','duskull','dusclops','tropius','chimecho','absol','wynaut','snorunt','glalie','spheal','sealeo','walrein','clamperl','huntail','gorebyss','relicanth','luvdisc','bagon','shelgon','salamence','beldum','metang','metagross','regirock','regice','registeel','latias','latios','kyogre','groudon','rayquaza','jirachi','deoxys','turtwig','grotle','torterra','chimchar','monferno','infernape','piplup','prinplup','empoleon','starly','staravia','staraptor','bidoof','bibarel','kricketot','kricketune','shinx','luxio','luxray','budew','roserade','cranidos','rampardos','shieldon','bastiodon','burmy','wormadam','mothim','combee','vespiquen','pachirisu','buizel','floatzel','cherubi','cherrim','shellos','gastrodon','ambipom','drifloon','drifblim','buneary','lopunny','mismagius','honchkrow','glameow','purugly','chingling','stunky','skuntank','bronzor','bronzong','bonsly','mime\ jr.','happiny','chatot','spiritomb','gible','gabite','garchomp','munchlax','riolu','lucario','hippopotas','hippowdon','skorupi','drapion','croagunk','toxicroak','carnivine','finneon','lumineon','mantyke','snover','abomasnow','weavile','magnezone','lickilicky','rhyperior','tangrowth','electivire','magmortar','togekiss','yanmega','leafeon','glaceon','gliscor','mamoswine','porygon-z','gallade','probopass','dusknoir','froslass','rotom','uxie','mesprit','azelf','dialga','palkia','heatran','regigigas','giratina','cresselia','phione','manaphy','darkrai','shaymin','arceus','victini','snivy','servine','serperior','tepig','pignite','emboar','oshawott','dewott','samurott','patrat','watchog','lillipup','herdier','stoutland','purrloin','liepard','pansage','simisage','pansear','simisear','panpour','simipour','munna','musharna','pidove','tranquill','unfezant','blitzle','zebstrika','roggenrola','boldore','gigalith','woobat','swoobat','drilbur','excadrill','audino','timburr','gurdurr','conkeldurr','tympole','palpitoad','seismitoad','throh','sawk','sewaddle','swadloon','leavanny','venipede','whirlipede','scolipede','cottonee','whimsicott','petilil','lilligant','basculin','sandile','krokorok','krookodile','darumaka','darmanitan','maractus','dwebble','crustle','scraggy','scrafty','sigilyph','yamask','cofagrigus','tirtouga','carracosta','archen','archeops','trubbish','garbodor','zorua','zoroark','minccino','cinccino','gothita','gothorita','gothitelle','solosis','duosion','reuniclus','ducklett','swanna','vanillite','vanillish','vanilluxe','deerling','sawsbuck','emolga','karrablast','escavalier','foongus','amoonguss','frillish','jellicent','alomomola','joltik','galvantula','ferroseed','ferrothorn','klink','klang','klinklang','tynamo','eelektrik','eelektross','elgyem','beheeyem','litwick','lampent','chandelure','axew','fraxure','haxorus','cubchoo','beartic','cryogonal','shelmet','accelgor','stunfisk','mienfoo','mienshao','druddigon','golett','golurk','pawniard','bisharp','bouffalant','rufflet','braviary','vullaby','mandibuzz','heatmor','durant','deino','zweilous','hydreigon','larvesta','volcarona','cobalion','terrakion','virizion','tornadus','thundurus','reshiram','zekrom','landorus','kyurem','keldeo','meloetta','genesect','chespin','quilladin','chesnaught','fennekin','braixen','delphox','froakie','frogadier','greninja','bunnelby','diggersby','fletchling','fletchinder','talonflame','scatterbug','spewpa','vivillon','litleo','pyroar','flabebe','floette','florges','skiddo','gogoat','pancham','pangoro','furfrou','espurr','meowstic','honedge','doublade','aegislash','spritzee','aromatisse','swirlix','slurpuff','inkay','malamar','binacle','barbaracle','skrelp','dragalge','clauncher','clawitzer','helioptile','heliolisk','tyrunt','tyrantrum','amaura','aurorus','sylveon','hawlucha','dedenne','carbink','goomy','sliggoo','goodra','klefki','phantump','trevenant','pumpkaboo','gourgeist','bergmite','avalugg','noibat','noivern','xerneas','yveltal','zygarde','diancie','hoopa','volcanion','rowlet','dartrix','decidueye','litten','torracat','incineroar','popplio','brionne','primarina','pikipek','trumbeak','toucannon','yungoos','gumshoos','grubbin','charjabug','vikavolt','crabrawler','crabominable','oricorio','cutiefly','ribombee','rockruff','lycanroc','wishiwashi','mareanie','toxapex','mudbray','mudsdale','dewpider','araquanid','fomantis','lurantis','morelull','shiinotic','salandit','salazzle','stufful','bewear','bounsweet','steenee','tsareena','comfey','oranguru','passimian','wimpod','golisopod','sandygast','palossand','pyukumuku','type:\ null','silvally','minior','komala','turtonator','togedemaru','mimikyu','bruxish','drampa','dhelmise','jangmo-o','hakamo-o','kommo-o','tapu\ koko','tapu\ lele','tapu\ bulu','tapu\ fini','cosmog','cosmoem','solgaleo','lunala','nihilego','buzzwole','pheromosa','xurkitree','celesteela','kartana','guzzlord','necrozma','magearna','marshadow']

#IUs = bot.get_server(281793428793196544)
#poll = IUs.get_channel(314799585761427457)

IU = sql.connect("IU_profile.db")
q = IU.cursor()
try :
	q.execute('CREATE TABLE IU_profile(id char(18) primary key , name varchar(30) , nick varchar(30) , pic varchar(1000) , DOB date , city varchar(20) , lang text , github varchar(1000) , games text , anime text , status text , info text);')
except :
	pass
IU.commit()

@bot.event
async def on_ready() :
	await bot.change_presence(game=discord.Game(name='with Bing ...',type=0))
	print('Ready to Rock ...')

@bot.command()
async def poll(msg) :
	poll = msg.author.server.get_channel("314799585761427457")
	em = Embed(title = 'Attention ...' , colour = int(hex(random.randint(0,16777215)),16),description = str(msg.content) )
	pmsg = await bot.send_message(destination = poll , embed = em)
	await bot.add_reaction(message = pmsg,emoji = "🔼")
	await bot.add_reaction(message = pmsg,emoji = "🔽")

@bot.command(pass_context = True)
async def announce(ctx) :
	if ctx.message.author.top_role==ctx.message.server.role_hierarchy[0]:
		msg = ctx.message
		ann = ctx.message.author.server.get_channel("295394349867597825")
		em = Embed(title = 'An Important Announcement !!!' ,colour = int(hex(random.randint(0,16777215)),16),description = str(msg.content.replace("IU_announce",">>>")))
		em.set_thumbnail(url = ctx.message.author.avatar_url)
		em.set_footer(text = '... by '+str(ctx.message.author.name))
		await bot.send_message(destination = ann , embed = em)
	else :
		em = Embed(title = 'Sorry ...' ,description = 'You lack enough permissions ...',colour = int(hex(random.randint(0,16777215)),16))
		await bot.send_message(destination = ctx.message.channel , embed = em)


'''
@bot.command(pass_context = True , aliases = ['scores' , 'iplscores'] )
async def ipl(ctx) :
	data = requests.get("http://www.cricbuzz.com/")
	soup = bs.BeautifulSoup(data.text,"lxml")
	data = []
	for link in soup.find_all('div') :
		l = link.get('class')
		if l == None : continue
		if "cb-ovr-flo" in l :
			data.append(link.text)
	tossres = data[5]
	inn = [ data[2] , data[4] ]
	tm = [ data[1] , data[3] ]
	curr = data[0]
	em = Embed(title = "{0} vs {1}".format(tm[0],tm[1]) , description = "{5} ... \nCurrent Inning : {0} \n{1} : {2}\n{3} : {4}".format(curr,tm[0],inn[0],tm[1],inn[1],tossres)+"\n*Score Updated at* "+str(strftime("%a, %d %H:%M:%S", localtime())), colour = int(hex(random.randint(0,16777215)),16))
	await bot.send_typing(ctx.message.channel)
	await bot.say(embed = em)

@bot.command(aliases=['iplscores', 'scores'],pass_context=True)
async def ipl(ctx) :
	data = requests.get("http://www.cricbuzz.com/")
	soup = bs.BeautifulSoup(data.text,"lxml")
	data = []
	for link in soup.find_all('div') :
		l = link.get('class')
		print(l)
		if l is None : continue
		if "cb-ovr-flo" in l:
			data.append(link.text)
		print(data)
		
		tossres = data[5]
		inn = [ data[2] , data[4] ]
		tm = [ data[1] , data[3] ]
		curr = data[0]
		em = discord.Embed(title = "{0} vs {1}".format(tm[0],tm[1]) , description = "{5} ... \nCurrent Inning : {0} \n{1} : {2}\n{3} : {4}".format(curr,tm[0],inn[0],tm[1],inn[1],tossres)+"\n*Score Updated at* "+str(strftime("%a, %d %H:%M:%S", localtime())), colour = int(hex(random.randint(0,16777215)),16))
		em = Embed(title = 'Pong ! in ...' , colour = int(hex(random.randint(0,16777215)),16),description = str(random.randint(100,999))+" ps")
		await bot.say(embed = em)

@bot.command(aliases = ['scoretable','ipltable','ipl_table','points','points_table','pt'] , pass_context = True)
async def pointstable(ctx) :
	data = requests.get("http://www.cricbuzz.com//cricket-series/2676/indian-premier-league-2018/points-table")
	soup = bs.BeautifulSoup(data.text,"lxml")
	data,tmd = [],[]
	teams = ['Delhi Daredevils','Royal Challengers Bangalore','Rajasthan Royals','Kolkata Knight Riders','Mumbai Indians','Chennai Super Kings','Sunrisers Hyderabad','Kings XI Punjab']
	i = 0
	for link in soup.find_all('td') :
		data.append(link.text)
	for i in range(len(data)) :
		if data[i] in teams :
			if len(data[i+1]) <= 2 :
				x = []
				for j in range(8) :
					x.append(data[i+j])
				tmd.append(x)
	table = ""
	for t in tmd :
		rank = str(tmd.index(t)+1)
		name,plyed,won,lost,points,NRR = t[0],t[1] , t[2] , t[3] , t[-2] , t[-1]
		table += str("\n"+rank + ") " + name + "\n\tP : " + plyed + "\t\tW : "+won+"\t\tL : "+lost+"\n\tP : "+points+"\t\tNRR = "+NRR)
	em = Embed(title = "Points Table IPL 2018" , description = table , colour = int(hex(random.randint(0,16777215)),16) )
	await bot.send_typing(ctx.message.channel)
	await bot.say(embed = em )
'''

@bot.command(pass_context = True )
async def ping(ctx) :
	'''replies Pong !'''
	em = Embed(title = 'Heya ...' ,description = str(ctx.message.author.name), colour = int(hex(random.randint(0,16777215)),16))
	print(ctx.message.author.id)
	await bot.say(embed = em )

@bot.command(pass_context = True)
async def lyrics(ctx,artst = "",sng = "") :
	artist = str(artst).lower().replace(' ','')
	song = str(sng).lower().replace(' ','')
	print(artist , song)
	
	head = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 http://notifyninja.com/monitoring' }
	data = requests.get("https://www.azlyrics.com/lyrics/" +str(artist)+"/"+str(song)+".html" , headers = head)
	#data = requests.get("https://www.azlyrics.com/lyrics/edsheeran/shapeofyou.html" , headers = head)
	soup = bs.BeautifulSoup(data.text,"lxml")
	data = []
	for link in soup.find_all('div') :
		data.append(link.text)
	maxl = 0
	for d in data :
		if len(d) > maxl :
			dt = d
			maxl = len(d)
	for i in range(9) :
		dt = dt.replace('\n\n','\n')
	dt  = dt.split('\n\r\n')
	try :
		ddd = []
		song,lyr = dt[0] , dt[1].split("\n")
		parts = len(lyr) // 15
		l,u = 0, 0
		for i in range(parts-1) :
			u,l = u+16 , u
			ddd.append("\n-".join(lyr[l:u]))
		ddd.append("\n-".join(lyr[u:]))
	except :
		song = "Sorry"
		lyr = "Not Found"
	await bot.send_typing(ctx.message.channel)
	for lyrr in ddd :
		em = Embed(title = song , description = lyrr , colour = int(hex(random.randint(0,16777215)),16))
		await bot.send_message(destination = ctx.message.channel, embed = em)
	
@bot.command(pass_context = True )
async def pokemon(ctx) :
	'''shows gif of a pokemon !'''
	ms = ' : '
	try :
		cc = str(ctx.message.content).split()[1].lower()
		if cc not in poks :
			ms = 'misconception ... Take a '
			cc= str(random.choice(poks))
	except :
		cc= str(random.choice(poks))
	em = Embed(title = 'You caught a \n'+ms+cc.capitalize()+' !' , colour = int(hex(random.randint(0,16777215)),16))
	em.set_thumbnail(url = 'http://www.pokestadium.com/sprites/xy/'+cc+'.gif')
	await bot.say(embed = em )

@bot.command(pass_context=True)
async def purge(ctx) :
	'''Purge specific number of messages ...'''
	n = int(((ctx.message.content).split())[1])
	await bot.purge_from(channel = ctx.message.channel,limit = n+1)
	asyncio.sleep(15)
	em = Embed(title = 'Deleted {} message(s)'.format(n+1) , colour = int(hex(random.randint(0,16777215)),16))
	ss = await bot.say(embed = em )
	asyncio.sleep(3000)
	await bot.delete_message(ss)
'''
@bot.command(pass_context = True)
async def register(ctx) :
	try :
		q.execute("insert into IU_profile(id,name,nick,pic) values('{0}','{1}','{2}','{3}')".format(ctx.message.author.id,ctx.message.author.name,ctx.message.author.display_name,ctx.message.author.avatar_url))
		await bot.say(embed = Embed(title = 'Done', description = "Check your DMs"))
		IU.commit()
		await bot.send_message(ctx.message.author,'Lets fill other info ...')
		await bot.send_message(ctx.message.author,'... Your Birthday\nStrictly in *YYYY-MM-DD* format ^_^')
		dd = await bot.wait_for_message(author = ctx.message.author )
		dd = str(dd.content)
		await bot.send_message(ctx.message.author,'... Tell me about where you from \n*city*,*state*')
		ss = await bot.wait_for_message(author = ctx.message.author)
		ss = str(ss.content)
		await bot.send_message(ctx.message.author,'... And about your favorite Programming languages\ncomma \',\' separated ...')
		ll = await bot.wait_for_message(author = ctx.message.author)
		ll = str(ll.content)
		await bot.send_message(ctx.message.author,'Do you have a Github/Sololearn Account ?\nDrop its link with separated commas / write \'None\' if no ...')
		gg = await bot.wait_for_message(author = ctx.message.author)
		gg = str(gg.content) #if (gg.content).lower() != 'none' else None
		await bot.send_message(ctx.message.author,'What genre/kinds of games you like ?\nList comma \',\' separated ...')
		gm = await bot.wait_for_message(author = ctx.message.author)
		gm = str(gm.content) #if (gm.content).lower() != 'none' else None
		await bot.send_message(ctx.message.author,'Do you watch Anime ?\nList ur Favorites/Genre / write \'None\' if no ...')
		aa = await bot.wait_for_message(author = ctx.message.author)
		aa = str(aa.content) #if (aa.content).lower() != 'none' else None
		await bot.send_message(ctx.message.author,'Finally tell smth about you which can make other ppl know you \nOr simply your hobbies or Topics you like to talk bout ... ^_^')
		ii = await bot.wait_for_message(author = ctx.message.author)
		ii = str(ii.content)
		q.execute("UPDATE IU_profile SET DOB = '{1}' , city = '{2}' , lang = '{3}' , github = '{4}' , games = '{5}' , anime = '{6}' , info = '{7}' WHERE id = {0}".format(ctx.message.author.id,dd,ss,ll,gg,gm,aa,ii))
		await bot.send_message(ctx.message.author,'Congo info Updated :white_flower:')
		IU.commit()
	except :
		await bot.say(embed = Embed(title = 'Error !' , description = 'Maybe , baby I know since ages ... :white_flower:'))
	server = ctx.message.channel.server
	rl = discord.utils.get(server.roles, name='Friends')
	await bot.add_roles(ctx.message.author , rl)
	IU.commit()

@bot.command(pass_context = True)
async def profile(ctx) :
	auth = ctx.message.author
	rls = auth.roles
	try :
		a = str(ctx.message.content).split()
		a = str(a[1])
		id = str(a).replace('<@','').replace('>','').replace('!','')
		print(id)
	except :
		id = str(auth.id)

	try :
		for i in q.execute("SELECT * FROM IU_profile WHERE id = {0}".format(str(id))) :
			a = i
		if 'Friends' not in rls :
			for i in q.execute("SELECT * FROM IU_profile WHERE id = {0}".format(ctx.message.author.id)) :
				a = i
			print(a)
			xx = "We know {0}\nA.K.A : {1}\nExisting since : {2}\nIs Glory of {3}\nPlays games : {4}\nKnows Anime : {5}\nCodes : {6}\nAnd Github {7}\n\nMore about {0} ,\n\t{8}".format(a[1],a[2],a[4],a[5],a[8],a[9],a[6],a[7],a[11])
			em = Embed(title = 'id = '+str(a[0]) , description = xx , colour = int(hex(random.randint(0,16777215)),16))
			em.set_thumbnail(url = str(a[3]))
			em.set_footer(text = str(a[10]))
		else :
			for i in q.execute("SELECT id,pic,info,status FROM IU_profile WHERE id = {0}".format(ctx.message.author.id)) :
				a = i
			em = Embed(title = 'id = '+str(a[0]) , description = str(a[2]) , colour = int(hex(random.randint(0,16777215)),16))
			em.set_thumbnail(url = str(a[1]))
			em.set_footer(text = str(a[3]))
	except :
		em = Embed(title = ':x:Error' , colour = int(hex(random.randint(0,16777215)),16) , description = 'User not Registered !!!\nUse iu_register to register yourself on our Bot DB')
		await bot.say(embed = em)
		return
	await bot.say(embed = em )

@bot.command(pass_context = True)
async def update(ctx) :
	"""You can update your info via this command ..."""
	try :
		mx = (ctx.message.content).split()
		c = mx[1]
		mx.pop(0)
		mx.pop(0)
		inf = " ".join(mx)
		print(mx)
		q.execute("UPDATE IU_profile SET {1} = '{2}' WHERE id = {0}".format(ctx.message.author.id,c,inf))
		await bot.say(embed = Embed(description = "Update Complete !" , colour = int(hex(random.randint(0,16777215)),16)))
		IU.commit()
	except :
		await bot.say(embed = Embed(description = "```Use 'iu_update param new_info' to update your info ...\nUse \nnick : nickname\npic : temp picture\ncity : your state or location\nlang : coding languages\ngithub : github profile link\ngames : new games\nstatus : updates status\ninfo : information```" , colour = int(hex(random.randint(0,16777215)),16)))

@bot.command(pass_context=True)
async def note(ctx) :
	nts = ''
	# print(msg.message.content)
	try :
		m = str(ctx.message.content).split()
		mx = m[1]
		m.pop(0)
		m.pop(0)
		inf = ' '.join(m)
		if mx.lower() == 'show' :
			for i in q.execute("select point from notes where tag like '{}'".format(mx)) :
				nts = "\n".join(i)
			if nts == '' :
				nts = 'information not Found'
			await bot.send_message(ctx.message.author,nts)
		else :
			q.execute("insert into notes values('{0}','{1}')".format(mx,inf))
			IU.commit()
	except IndexError :
		await bot.say('`Enter Correct Syntax :\niu_note [tag|show] [info|tag]`')

@bot.event()
async def on_member_join(ctx,member) :
	wel = ctx.message.author.server.get_channel("429618676875001856")
	em = Embed(title = 'User Welcome ...' , colour = int(hex(random.randint(0,16777215)),16),description = "Welcome !!!" )
	em.set_thumbnail(url = member.avatar_url)
	pmsg = await bot.send_message(destination = wel, embed = em)
'''

@bot.event
async def on_message(msg) :
	if str(msg.author.id) == "270898185961078785" :
		await bot.process_commands(msg)

bot.run('NDQ3Mzk1NTEyNjYxMDQ5MzU0.DeRZdQ.M1eyUTzo75UdR3dDjU2z-xbQ128') #Wolfie

'''
# NOTE: These methods return None when not found.
#       Additionally, these methods are only useful
#       when the bot is ready. ➔ = returns

bot.get_channel(channel_id)
  # ➔ discord.Channel/discord.PrivateChannel
bot.get_server(server_id) # ➔ discord.Server

server.get_channel(channel_id)  # ➔ discord.Channel
server.get_member(member_id)    # ➔ discord.Member
discord.utils.get(server.roles, name='my role')
  # ➔ discord.Role
discord.utils.get(server.roles, id='role id')
  # ➔ discord.Role
'''
