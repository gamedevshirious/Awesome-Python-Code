from kivy.uix.colorpicker import ColorPicker
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


parent = BoxLayout()
clr_picker = ColorPicker()
parent.add_widget(clr_picker)

# To monitor changes, we can bind to color property changes
def on_color(instance, value):
    print("RGBA = ", str(value))  #  or instance.color
    print("HSV = ", str(instance.hsv))
    print("HEX = ", str(instance.hex_color))

clr_picker.bind(color=on_color)



class UltimateNoterApp(App):
	def build(self):
		return parent
	
	def on_pause(self):
		return True

	def on_resume(self):
		pass

if __name__ == '__main__':
	UltimateNoterApp().run()
