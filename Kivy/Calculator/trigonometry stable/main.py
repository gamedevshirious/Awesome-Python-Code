from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
import math

Builder.load_string('''
<Screen> :
	orientation : "vertical"
	padding : (self.width*2) / 100 , 0		
	GridLayout :		
		padding : 0 , (self.height * 2.5) /100
		cols : 2
		size_hint : 1 , .70
		ScrollView :
			Label :
				id : eqn
				text : ""
				font_size : 26
				is_focusable : False
				readonly : True
				size_hint : 1 , None
				text_size : self.width , None
				height : self.texture_size[1]
				
		Button :
			text : "<-"
			size_hint : .25 , .25
			on_press : root.back_btn() 
			
		ScrollView :
			Label :
				id : ans
				text : ""
				font_size : 26
				text_size : self.width , None
				size_hint : 1,None
				height : self.texture_size[1]
		Button :
			text : "CLR"
			size_hint : .25 , .25
			on_press : root.clr_btn() 
			
	GridLayout :
		cols : 5
		size_hint : 1 , .1
		Button :
			text : "="
			on_press : if deqn.text != "" and deqn.text != ")" : root.calculate()
		Button :
			text : "("
			on_press : root.btnpress(self.text)	
		Button :
			text : ")"			
			on_press : root.btnpress(self.text)	
		TextInput :
			id : usr_rad
			text : ""
			input_filter : "float"
			font_size : 24
		Button: 
			text : "rad"
			on_press : if usr_rad.text != "" : root.btnpress(self.text +" "+usr_rad.text, "math.radians("+usr_rad.text+")" )
				
	BoxLayout :
		size_hint : 1,.0001
		ScrollView :
			Label :
				id : deqn
				text : ""
	TabbedPanel :
		size_hint : 1 , .7
		do_default_tab : False
		TabbedPanelItem:
	        text: 'Default'
			GridLayout :	
				cols : 5
				Button :
					text : "+"
					on_press : root.btnpress(self.text)
				Button :
					text : "1"
					on_press : root.btnpress(self.text)
				Button :
					text : "2"
					on_press : root.btnpress(self.text)
				Button :
					text : "3"
					on_press : root.btnpress(self.text)
				Button :
					text : "-"
					on_press : root.btnpress(self.text)
			
				Button :
					text : "X"
					on_press : root.btnpress(self.text , "*")	
				Button :
					text : "4"
					on_press : root.btnpress(self.text)
				Button :
					text : "5"
					on_press : root.btnpress(self.text)
				Button :
					text : "6"
					on_press : root.btnpress(self.text)
				Button :
					text : "/"
					on_press : root.btnpress(self.text)
				
				Button :
					text : "("
					on_press : root.btnpress(self.text )	
				Button :
					text : "7"
					on_press : root.btnpress(self.text)
				Button :
					text : "8"
					on_press : root.btnpress(self.text)
				Button :
					text : "9"
					on_press : root.btnpress(self.text)
				Button :
					text : ")"
					on_press : root.btnpress(self.text)
					
				Button :
					text : "^"
					on_press : root.btnpress(self.text)
				Button :
					text : "."
					on_press : root.btnpress(self.text)
				Button :
					text : "0"
					on_press : root.btnpress(self.text)
				Button :
					text : "00"
					on_press : root.btnpress(self.text)
				Button :
					text : "="
					on_press : if deqn.text != "" and deqn.text != ")" : root.calculate()
		TabbedPanelItem:
			text : "Trigonometry"
			TabbedPanel :
				size_hint : 1 , 1
				do_default_tab : False
				TabbedPanelItem:
				    text: 'Page 1'				
					GridLayout :
						cols : 3
						Button: 
							text : "sin"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )
						Button: 
							text : "cos"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )
						Button: 
							text : "tan"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )
						Button: 
							text : "asin"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )				
						Button: 
							text : "acos"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )				
						Button: 
							text : "atan"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )				
						Button: 
							text : "sinh"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )				
						Button: 
							text : "cosh"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )				
						Button: 
							text : "tanh"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )				
						Button: 
							text : "asinh"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )				
						Button: 
							text : "acosh"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )				
						Button: 
							text : "atanh"
							on_press : root.btnpress(self.text+"(" , "math."+ self.text + "(" )		
				TabbedPanelItem:
					text: 'Page 2'		
					GridLayout :
						cols : 3
						Button: 
							text : "sec"
							on_press : root.btnpress(self.text+"(" , "1/math.cos" + "(" )	
						Button: 
							text : "cosec"
							on_press : root.btnpress(self.text+"(" , "1/math.sin" + "(" )	
						Button: 
							text : "cot"
							on_press : root.btnpress(self.text+"(" , "1/math.tan" + "(" )	
						Button: 
							text : "asec"
							on_press : root.btnpress(self.text+"(" , "1/math.acos" + "(" )				
						Button: 
							text : "acosec"
							on_press : root.btnpress(self.text+"(" , "1/math.asin" + "(" )	
						Button: 
							text : "acot"
							on_press : root.btnpress(self.text+"(" , "1/math.atan" + "(" )	
						Button: 
							text : "sech"
							on_press : root.btnpress(self.text+"(" , "1/math.cosh" + "(" )	
						Button: 
							text : "cosech"
							on_press : root.btnpress(self.text+"(" , "1/math.sinh" + "(" )	
						Button: 
							text : "coth"
							on_press : root.btnpress(self.text+"(" , "1/math.tanh" + "(" )	
						Button: 
							text : "asech"
							on_press : root.btnpress(self.text+"(" , "1/math.acosh" + "(" )	
						Button: 
							text : "acosech"
							on_press : root.btnpress(self.text+"(" , "1/math.asinh" + "(" )	
						Button: 
							text : "acoth"
							on_press : root.btnpress(self.text+"(" , "1/math.atanh" + "(" )	
				
		TabbedPanelItem:
	        text: 'Constants'
			GridLayout :
				cols : 3
				Button: 
					text : "PI"
					on_press : root.btnpress(self.text , "math.pi" )	
				Button: 
					text : "e"
					on_press : root.btnpress(self.text , "math.e" )	
				Button: 
					text : "rad 0"
					on_press : root.btnpress(self.text , "math.radians(0)" )	
				Button: 
					text : "rad 30"
					on_press : root.btnpress(self.text , "math.radians(30)" )	
				Button: 
					text : "rad 60"
					on_press : root.btnpress(self.text , "math.radians(60)" )	
				Button: 
					text : "rad 90"
					on_press : root.btnpress(self.text , "math.radians(90)" )	
''')

class Screen(BoxLayout) :
	stack = ListProperty([])
	dstack = ListProperty([])
	
	def btnpress(self , show , happ = "") :
		try :
			chk = self.dstack[-1][-1]
			nums = "1234567890.^-+/*X)"
			print(chk , show[0])
			if chk in nums and show[0] not in nums :			
				print("*"+str(show))
				self.ids.deqn.text += ("*" + show) if happ == "" else ( "*" + happ )
				print(self.ids.deqn.text)
			else :
				self.ids.deqn.text += show if happ == "" else happ
		except :			
			self.ids.deqn.text += show if happ == "" else happ
			
		self.ids.eqn.text += show
		self.stack.append(self.ids.eqn.text)
		self.dstack.append(self.ids.deqn.text)
	
	def calculate(self ):
		try :
			eqnn = self.ids.deqn.text 
			eqnn = eqnn.replace("^","**").replace("/" , "*1.0/")
			while eqnn.count("(") > eqnn.count(")") :
				eqnn += ")"
			print(eqnn )
			Ans = eval(eqnn)
			print(Ans)
			self.ids.ans.text = "0" if Ans > 0.000000001 and Ans < -0.000000001 else str(Ans)
		except ZeroDivisionError :
			self.clr_btn()
			popup = Popup(title='Error !!!' , content=Label(text="Dividing by zero Error !!!") , size = (200,100) , size_hint = (None  , None))
			popup.open()	
		except :
			self.clr_btn()
			popup = Popup(title='Error !!!', content=Label(text="Syntax Error !!!")  , size = (200,100) , size_hint = (None  , None))
			popup.open()	
	
	def back_btn(self) :
		print(len(self.stack) ,len(self.dstack))
		if(len(self.stack) > 0 and  len(self.dstack) > 0) :
			self.ids.eqn.text = (self.stack).pop()
			self.ids.deqn.text = (self.dstack).pop()
		else :			
			self.stack = []
			self.ids.eqn.text = ""
	
	def clr_btn(self) :
		self.ids.usr_rad.text = ""
		self.ids.deqn.text = ""
		self.ids.eqn.text = ""
		self.ids.ans.text = ""
		self.stack = []
		self.dstack = []
		
	
		
class CalculatorApp(App) :
	def build(self) :
		return Screen()
		
	def on_pause(self):
		return True

	def on_resume(self):
		pass

CalculatorApp().run()    
