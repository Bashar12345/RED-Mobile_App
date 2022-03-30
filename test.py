from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder

#Window.size = (300, 500)


class test_RED_app(App, MDApp):
    CLASSES = {
        "Page_manager": "Main",
        "Login_page": "Main",
        "Home_page": "Main",
        "Shots": "Main",
        "Nav_pills":"Main",
        "Header":"Main",
    }

    AUTORELOADER_PATHS = [
        ('.', {"recursive": True})
    ]

    def build_app(self, *args):
        print("App auto relaoding")
        return Factory.Page_manager()


test_RED_app().run()
