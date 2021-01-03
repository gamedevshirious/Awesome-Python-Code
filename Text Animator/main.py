import time, sys, os

	
def typewriter(text):
	for c in text:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(.1)

text = """
Hello!
I am Shreyash










"""

os.system("cls")
typewriter(text)