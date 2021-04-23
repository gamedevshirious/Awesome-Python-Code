from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_string('''
<Screen> :
    orientation : "vertical"
    font_size : 17
    GridLayout :
        cols : 2

        Label:
            text : "Current meter"
            font_size : 17
        TextInput :
            id : c_meter
            text : "15417"
            font_size : 17
            input_filter : "float"

        Label:
            text : "Mileage"
            font_size : 17
        TextInput :
            id : mileage
            text : "70"
            font_size : 17
            input_filter : "float"

        Label:
            text : "Fuel"
            font_size : 17
        TextInput :
            id : fuel
            text : "100"
            font_size : 17
            input_filter : "float"

        Label:
            text : "Rate"
            font_size : 17
        TextInput :
            id : rate
            text : "80"
            font_size : 17
            input_filter : "float"

        Button :
            text : "Calculate"
            font_size : 17
            on_press : root.calculate()
        Button :
            id : ans
            disabled : "true"
            text : "Expected kms"
            font_size : 17
    GridLayout :
        size_hint : 1, .2
        cols : 3
        Label:
            id : l_c_meter
            text : "Current Meter"
            font_size : 17
        Label:
            text : "->"
            font_size : 30
        Label:
            id : l_n_meter
            text : "Expected Meter"
            font_size : 17

''')

class Screen(BoxLayout) :
    def calculate(self):
        try :
            c_meter = int(self.ids.c_meter.text)
            self.ids.l_c_meter.text = str(c_meter)
            m, f, r = float(self.ids.mileage.text), float(self.ids.fuel.text), float(self.ids.rate.text)
            ans = m * (f/r)
            self.ids.ans.text = str(ans)[:6]
            self.ids.l_n_meter.text = str(int(c_meter + ans))
        except :
            popup = Popup(title='Error !!!' , content=Label(text="An Error Occured!!!") , size = (200,100) , size_hint = (None  , None))
            popup.open()


class TravelCalculatorApp(App) :
    def build(self) :
        return Screen()

    def on_pause(self):
        return True

    def on_resume(self):
        pass

TravelCalculatorApp().run()

'''
AnchorLayout:
        size_hint : 1, .4
        anchor_x : "center"
        anchor_y : "center"
'''
