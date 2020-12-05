from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.base import runTouchApp

Builder.load_string('''
<Screen> :
	orientation : "vertical"
	padding : (self.width * 2) / 100 , (self.height * 2) /100		
    Label :
        text : "Calculator"
        font_size : 32	
    	size_hint : 1 , .10
	GridLayout :		
		padding : 0 , (self.height * 2.5) /100
		cols : 2
		spacing  : 5
		TextInput :
			id : eqn
			text : ""
			font_size : 40
			is_focusable : False
			readonly : True
			size_hint : 1 , .25
		Button :
		    text : "<-"
		    size_hint : .25 , .25
		    on_press : root.back_btn() 
		ScrollView :
    		Label :
	    		id : ans
		    	text : ""
		    	font_size : 40
			    size_hint : 1 , .25
			    text_size : self.width , None
			    size_hint_y : None
			    height : self.texture_size[1]
		Button :
		    text : "CLR"
		    size_hint : .25 , .25
		    on_press : root.clr_btn() 
		    
	GridLayout :	
		spacing : 5
		cols : 5
		Button :
			text : "+"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "1"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "2"
			on_press : eqn.text = eqn.text + self.text 
		Button :
			text : "3"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "-"
			on_press : eqn.text = eqn.text + self.text
		
		Button :
			text : "*"
			on_press : eqn.text = eqn.text + self.text		
		Button :
			text : "4"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "5"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "6"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "/"
			on_press : eqn.text = eqn.text + self.text
			
		Button :
			text : "("
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "7"
			on_press : eqn.text = eqn.text + self.text 
		Button :
			text : "8"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "9"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : ")"
			on_press : eqn.text = eqn.text + self.text
			
		Button :
			text : "^"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "."
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "0"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "00"
			on_press : eqn.text = eqn.text + self.text
		Button :
			text : "="
			on_press : root.calculate()
''')

class Screen(BoxLayout) :
	def calculate(self ):
		try :
			eqnn = str(self.ids.eqn.text).replace("/","*1.0/")
			Ans = eval(eqnn.replace("^","**"))
			self.ids.ans.text = str(Ans)
		except :
			self.ids.ans.text = ""
			self.ids.eqn.text = ""
			popup = Popup(title='Error !!!',
            content=Label(text="Please use correct syntax to perform the operation !!!"),
            size_hint=(None, None), size=(400, 100))
			popup.open()
			
	def back_btn(self) :
	    eqnn = str(self.ids.eqn.text)
	    self.ids.eqn.text = eqnn[:-1]
	
	def clr_btn(self) :
	    self.ids.eqn.text = ""
	    self.ids.ans.text = ""
	    

	
runTouchApp(Screen())    


