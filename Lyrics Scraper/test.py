import subprocess , shlex

testfile = open("test.txt" , "a") 
	
print("Started ...")
x = 1
while True and x == 1 :
	proc = subprocess.Popen(shlex.split('rhythmbox-client --no-start --print-playing-format %aa-.-%tt'), stdout=subprocess.PIPE) 
	info , err = proc.communicate()
	info = str(info,encoding="utf-8", errors="strict").split("-.-")

	artist = str(info[0])
	song = str(info[1])
	
	testfile.write(artist+" : "+song)
	print(artist+" : "+song)
	x = int(input("Capture"))
