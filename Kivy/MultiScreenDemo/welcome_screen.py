from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_string('''
<WelcomeScreen> :
	BoxLayout:
		Button:
			text: 'Goto settings'
			on_press: root.manager.current = 'login'
		Button:
			text: 'Quit'
''')

class WelcomeScreen(Screen) :
	pass
