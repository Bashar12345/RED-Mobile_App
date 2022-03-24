#from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton

from kivymd.uix.boxlayout import BoxLayout as bl
from kivy.uix.anchorlayout import AnchorLayout as al
from kivy.uix.gridlayout import GridLayout as gl
from kivy.uix.stacklayout import StackLayout as sl



class MDAnchorLayout(al, MDAdaptiveWidget):
    pass

class MDGridLayout(gl, MDAdaptiveWidget):
    pass

# class MDBoxLayout(bl, MDAdaptiveWidget):
# 	b1=MDRoundFlatButton(text='A button')
# 	b2=MDRoundFlatButton(text='b button')
# 	b3=MDRoundFlatButton(text='c button')

# 	self.add_widget(b1)
# 	self.add_widget(b2)
# 	self.add_widget(b3)
# 	pass

class Main_layout(gl,MDAdaptiveWidget): # GridLayout
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#b1=BaseRoundButton(text='A button')
		#b2=BaseRoundButton(text='b button')
		#b3=MDRoundFlatButton(text='c button')

		#self.add_widget(b1)
		#self.add_widget(b2)
		#self.add_widget(b3)
		
		

class red_app(MDApp):
	def build(self):
		return Main_layout()
	pass

#def build(self):
#  return Label(text='Hello world',font_size=45)
 

if __name__ == '__main__':
    red_app().run()