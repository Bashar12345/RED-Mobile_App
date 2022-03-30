from kivymd.app import MDApp
from kivy.factory import Factory
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang.builder import Builder
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.boxlayout import MDBoxLayout


Builder.load_file('page_ux.kv')

Window.size = (300, 500)


class Shots(MDBoxLayout):
    pass

class Nav_pills(MDBoxLayout):
    pass

class Header(MDBoxLayout):
    pass

class Home_page(Screen):
    pass
class Login_page(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1=MDRoundFlatButton(text='B button',pos_hint ={'top': .85})
        # b2=MDFlatButton(text='b button')
        # b3=MDRoundFlatButton(text='c button')

        self.add_widget(b1)
    pass



class Page_manager(Factory.ScreenManager):
    pass







class MainApp(MDApp):
    def build(self):
        #Uix= Builder.load_string(display)
        Uix=Builder.load_file('page_ux.kv')
        return Uix


if __name__ == "__main__":
    MainApp().run()







# Page_manager= ScreenManager()
# Page_manager.add_widget(home_page(name='homepage'))
# Page_manager.add_widget(login_page(name='login_page'))
# Page_manager.current = "homepage"




# sm = ScreenManger()
# db = DataBase("users.txt")

# screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"), Calendar(name="Calendar")]
# for screen in screens:
#     sm.add_widget(screen)

# sm.current = "login"