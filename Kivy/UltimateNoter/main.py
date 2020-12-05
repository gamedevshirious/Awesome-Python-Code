from kivy.app import App
from kivy.uix.screenmanager import *

from main_menu import MainMenuScreen
from welcome_screen import WelcomeScreen


sm = ScreenManager(transition = WipeTransition())
sm.add_widget( WelcomeScreen(name='welcome'))
sm.add_widget(MainMenuScreen(name='main_menu'))

class UltimateNoterApp(App):
	def build(self):
		sm.current = "welcome"
		return sm
	
	def on_pause(self):
		return True

	def on_resume(self):
		pass

if __name__ == '__main__':
	UltimateNoterApp().run()
