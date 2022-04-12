"""
HotReloader
-----------
Uses kaki module for Hot Reload (limited to some uses cases).
Before using, install kaki by `pip install kaki`

"""


import os
import platform
import sys

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs", "applibs"))

from kaki.app import App as HotReloaderApp  # NOQA: E402
# from kivy.logger import LOG_LEVELS, Logger  # NOQA: E402

# Logger.setLevel(LOG_LEVELS["debug"])


from kivy.factory import Factory  # NOQA: E402
from kivy.core.window import Window  # NOQA: E402
from kivymd.app import MDApp  # NOQA: E402

#from libs.uix.baseclass.root import Root  # NOQA: E402

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

#KV_FOLDER = os.path.join(os.getcwd(), "libs", "uix", "kv")


class RED_Mobile_App(HotReloaderApp, MDApp):  # NOQA: N801
    DEBUG = 1  # To enable Hot Reload

    # *.kv files to watch
    #KV_FILES = [os.path.join(KV_FOLDER, i) for i in os.listdir(KV_FOLDER)]

    # Class to watch from *.py files
    # You need to register the *.py files in libs/uix/baseclass/*.py
    CLASSES = {
    'Page_manager':'app_root'}
    #  'IndexScreen': 'libs.uix.baseclass.index_screen',
    #  'HistoryScreen': 'libs.uix.baseclass.history',
    #  'Quran_factScreen': 'libs.uix.baseclass.quran_fact',
    #  'HadditsScreen': 'libs.uix.baseclass.hadditss',
    #  'ScienceScreen': 'libs.uix.baseclass.science',
    #  'DeshScreen': 'libs.uix.baseclass.desh',  # NOQA: F821

    # Auto Reloader Path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def __init__(self, **kwargs):
        super(RED_Mobile_App, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "ReD_App"

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"

    def build_app(self,*args):  # build_app works like build method
        print("App auto relaoding")
        return Factory.Page_manager()   #For only testing perpouse


if __name__ == "__main__":
    RED_Mobile_App().run()
