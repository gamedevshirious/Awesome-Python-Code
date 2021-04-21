'''
 - message
1  status
2  target
3  

+ to increase
- to decrease

psn - poison
slp - sleep
brn - burn
frz - freeze
fln - flinch
ran - any random stat
'''
with open('mvlist.txt','r') as fp :
	f1 = fp.readlines()
# alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
f = open('newmvarr.txt','a')
c = open('status.txt','r')
x = c.readlines()
a = int(x[-1])
print("Use own and oppp")
for i in range(a,len(f1)) : #len(f1)
	new = str(f1[i])
	ss = new.split("'' , '")
	print(ss[0],'\n',ss[-1])
	ss = str(input('Message : \n'))
	sq = str(input('status eff : \n'))
	sm = str(input('target : \n'))
	if ss == 'finish' : 
		c = open('status.txt','w')
		c.write(str(i))
		c.close()
		break
	new = new.replace("''","'{}' ,".format(ss)).replace("'1'"," , '{}' ,".format(sq)).replace("'2'"," , '{}' ,".format(sm))
	f.write(new)

f.close()
fp.close()