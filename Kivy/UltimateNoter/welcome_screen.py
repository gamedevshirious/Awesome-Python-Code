from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string('''
<WelcomeScreen> :
	BoxLayout :
		orientation : "vertical"
		Button :
			background_color : [0.4, 0.8, 1.0, 1.0]
			text: 'Welcome to Ultimate Noter'
			font_size : 35
		Label :
			text : "Presented by : Shreyash"
			size_hint_y : .1
''')


class WelcomeScreen(Screen) :
	def on_enter(self) :
		def no_args_func(self):
			self.manager.current = "main_menu"
		Clock.schedule_once(lambda dt: no_args_func(self), 2.5)
