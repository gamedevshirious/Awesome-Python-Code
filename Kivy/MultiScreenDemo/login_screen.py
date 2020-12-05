from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_string('''
<LoginScreen> :
	GridLayout:
		cols : 1
		Button:
			text: 'Goto settings'
			on_press: root.manager.current = 'welcome'
		Button:
			text: 'Quit'
''')

class LoginScreen(Screen) :
	pass
