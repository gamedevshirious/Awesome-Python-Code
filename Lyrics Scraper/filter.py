with open("test.txt" , "r") as testfile :
	arr = testfile.readlines()
test = [[] , []]

def nat(s) :
	return s.lower().replace(' ','').rstrip().lstrip().replace("|" , "&").replace("feat." , "&").replace("," , "&").replace("www." , "").replace(".com" , "").strip(".0123456789")


for case in arr :
	art = case.split(":")
	art , sng = art[0] , art[1]
	art = nat(art)
	sng = nat(sng)
	url = art+"/"+sng+".html" 
	print(url)
