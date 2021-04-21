with open('poklist.txt') as f1 :
	f = f1.readlines()

fp = open('poklistnew.txt','w')

skipwords = ('Mega' , 'Style','Size','Alolan','Form')
for i in range(len(f)) :
	flag = False
	q = str(f[i])
	for i in range(len(skipwords)) :
		if skipwords[i] in q :
			flag = True
	if flag == False :
		fp.write(q)