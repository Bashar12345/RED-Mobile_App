import os
import platform

from kivy.factory import Factory  # NOQA: E402
from kivy.core.window import Window
from kivymd.app import MDApp

from libs.uix.baseclass.root import Root

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

Window.size = (300, 500)


class RED_Mobile_App(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(RED_Mobile_App, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "ReD_App"

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"

    def build(self):
        return Factory.Root()
