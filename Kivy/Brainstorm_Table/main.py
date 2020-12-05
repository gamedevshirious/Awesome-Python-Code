from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.lang import Builder
from random import randint

Builder.load_file("table.kv")
    
class DeskObj(Scatter) :
    source = StringProperty(None)

class Container(GridLayout) :
    def add_label(self) :
        o = DeskObj(rotation=randint(-30, 30))
        o.ids.obj.text = self.ids.lbl_text.text
        self.ids.desk.add_widget(o)
    def on_pause(self):
        return True
    
runTouchApp(Container())
