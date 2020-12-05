from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty()
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_string('''
<Panel> :
	size : 100 , 10
	Button :
		id : txt
		background_color : [0 , 0 , 1 , 1 ]
		size_hint : .9 , 1
	Button :
		text : "x"
		size_hint : .1 , 1
		background_color : [1 , 0 , 0 , 1 ]
		on_press : txt.text = "pressed"
		

<MainMenuScreen> :
	id : master
	ActionBar :
		pos_hint: {'top':1}
		size_hint_y : .1
		ActionView:
		    use_separator: True
		    ActionPrevious:
		        title: 'Speaking Scientific Calculator'
		        with_previous: False
		    ActionButton :
		        text : "+"
				on_press : master.add_elem()
	GridLayout :
		cols : 1
		size_hint_y : .9
		PageLayout :
			id : grid 
		
''')
class Panel(BoxLayout) :
	pass

class MainMenuScreen(Screen) :
	num = NumericProperty()
	i = 0
	#new_pos = [0 , 500]
	def add_elem(self) :
		g = self.ids.grid 
		b = Panel()
		b.ids.txt.text = str(self.i)
		#self.new_pos[1] -= 50
		self.i += 1
		g.add_widget(b)
		
'''
Button :
			background_color : [0,0,0,0]
			size: (min(self.width,self.height),min(self.width,self.height))
			canvas :
				Color:
					rgba: ((1,1,1,1) if self.state == "normal" else (0,0,0,1))
				Ellipse :
					pos : self.pos
					size: 75 , 75
			pos_hint : {"x" : .75 , "y" : .05}
			on_press : master.add_elem()

'''
