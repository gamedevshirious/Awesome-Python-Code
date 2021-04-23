from kivy.app import App
from kivy.uix.screenmanager import * 
from welcome_screen import WelcomeScreen
from login_screen import LoginScreen


sm = ScreenManager(transition = WipeTransition())
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(LoginScreen(name='login'))

class ScreensApp(App):
	def build(self):
		return sm
	
	def on_pause(self):
		return True

	def on_resume(self):
		pass

if __name__ == '__main__':
	ScreensApp().run()
