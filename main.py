from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout as al
from kivy.uix.boxlayout import BoxLayout as bl
from kivy.uix.gridlayout import GridLayout as gl
from kivy.uix.stacklayout import StackLayout as sl
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

from kivymd.uix.button import (MDFlatButton, MDRectangleFlatButton,
                               MDRoundFlatButton, MDTextButton)
from kivymd.uix.label import MDLabel

#Builder.load_file("red_app.kv")

class RootScreen(MDScreen):
    pass


class nav_box(gl, MDAdaptiveWidget):
    pass


class box_layout(bl):
    pass


class top_bar(al, MDAdaptiveWidget):
    pass


class tab_button(sl, MDAdaptiveWidget):
    pass


class header(gl, MDAdaptiveWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class main_screen(gl,MDAdaptiveWidget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		pass
# class MDBoxLayout(bl, MDAdaptiveWidget):
# 	b1=MDRoundFlatButton(text='A button')
# 	b2=MDRoundFlatButton(text='b button')
# 	b3=MDRoundFlatButton(text='c button')

# 	self.add_widget(b1)
# 	self.add_widget(b2)
# 	self.add_widget(b3)
# 	pass

class Main_layout(bl, MDAdaptiveWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    # b1=BaseRoundButton(text='A button')
    # b2=BaseRoundButton(text='b button')
    # b3=MDRoundFlatButton(text='c button')

    # self.add_widget(b1)
    # self.add_widget(b2)
    # self.add_widget(b3)
    btn_txt= StringProperty('clicked')
    def on_click(self):
        self.btn_txt=" you clicked"
        print('clicked')




class red_app(MDApp):
    def build(self):
        return Main_layout()


# def build(self):
#  return Label(text='Hello world',font_size=45)


if __name__ == '__main__':
    red_app().run()
