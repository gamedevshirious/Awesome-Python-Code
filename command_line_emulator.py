# python command line emulator
import os , shlex , subprocess


while True :
	cmd = input("$")
	if "cd" in cmd :
		try :
			os.chdir(cmd.split()[1])
		except :
			pass
		continue
	res = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE)
	print("Output : \n"+str(res.stdout,encoding="utf-8", errors="strict"))
	print("\n"+"-"*100+"\n")
	print("Exited with : "+str(res.stderr )+" Error")
	print("\n"+"-"*100+"\n")


