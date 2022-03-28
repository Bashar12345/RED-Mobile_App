from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix import MDAdaptiveWidget
from kivy.lang import Builder

from kivy.uix.anchorlayout import AnchorLayout as al
from kivy.uix.boxlayout import BoxLayout as bl
from kivy.uix.gridlayout import GridLayout as gl
from kivy.uix.stacklayout import StackLayout as sl
from kivy.uix.floatlayout import FloatLayout

from kivymd.uix.button import *

from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView

from kivy.properties import StringProperty
from kivy.core.window import Window

from kivymd.utils.fitimage import FitImage
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard

Window.size = (300, 500)
from kivymd.uix.button import (MDFlatButton, MDRectangleFlatButton,
                               MDRoundFlatButton, MDTextButton)
from kivymd.uix.label import MDLabel


# Builder.load_file("red_app.kv")
class nav_box(gl, MDAdaptiveWidget):
    pass


class box_layout(bl):
    pass


class top_bar():
    pass


class tab_button(sl, MDAdaptiveWidget):
    pass


class Main_layout(bl, MDAdaptiveWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    btn_txt = StringProperty('clicked')

    def on_click(self):
        self.btn_txt = " you clicked"
        print('clicked')


class header(gl, MDAdaptiveWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 1
        self.rows_minimum = {0, .25}


class UI(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # b1=MDFlatButton(text='A button',pos_hint ={'top': .85})
        # b2=MDFlatButton(text='b button')
        # b3=MDRoundFlatButton(text='c button')

        # self.add_widget(b1)
        # self.add_widget(b2)
        # self.add_widget(b3)

    pass


class home_page(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # view=ScrollView(do_scroll_y=True,do_scroll_x=False,scroll_timeout=25)
        pass


class login_page(Screen):
    pass


class page_manager_UI(ScreenManager):
    pass


class red_app(MDApp):
    def build(self):
        Builder.load_file('layout.kv')
        display=page_manager_UI()
        hm=home_page()
        display.add_widget(hm)
        return page_manager_UI()


if __name__ == '__main__':
    red_app().run()

    # b1=MDFlatButton(text='A button')
    # b2=MDFlatButton(text='b button')
    # b3=MDRoundFlatButton(text='c button')

    # self.add_widget(b1)
    # self.add_widget(b2)
    # self.add_widget(b3)

    # def login(self,MDIconButton):
    #     b = MDIconButton(icon="data/logo/kivy-icon-256.png")
    #     self.add_widget(b)
    #     print('loged in')

# def build(self):
#  return Label(text='Hello world',font_size=45)

# def __init__(self, **kwargs):
#     super(main_screen,self).__init__(**kwargs)
#     self.cols = 1
#     self.rows = 5
#     b=MDRectangleFlatButton(text='Hello',size= ('40dp', '40dp'), pos= ('100dp', '200dp'))
#    self.add_widget(b)

# sm=ScreenManager()

# class MDBoxLayout(bl, MDAdaptiveWidget):
# 	b1=MDRoundFlatButton(text='A button')
# 	b2=MDRoundFlatButton(text='b button')
# 	b3=MDRoundFlatButton(text='c button')

# 	self.add_widget(b1)
# 	self.add_widget(b2)
# 	self.add_widget(b3)
# 	pass

# class Custom_Card(MDCard, RoundedRectangularElevationBehavior):
#     '''Implements a material design v3 card.'''
#     text = StringProperty()
