#from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton

from kivymd.uix.boxlayout import MDBoxLayout as bl
from kivymd.uix.anchorlayout import AnchorLayout as al



class MDwidget(al):
	pass

class box_layout(bl):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#b1=BaseRoundButton(text='A button')
		#b2=BaseRoundButton(text='b button')
		b3=MDRoundFlatButton(text='c button')

		#self.add_widget(b1)
		#self.add_widget(b2)
		self.add_widget(b3)
		
		

class red_app(MDApp):
	pass

#def build(self):
#  return Label(text='Hello world',font_size=45)
 

if __name__ == '__main__':
    red_app().run()