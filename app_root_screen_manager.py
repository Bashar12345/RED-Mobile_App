
from kivy.factory import Factory 
# libs.baseclass.register_screen.ShrineRegisterScreen

PAGES = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import IndexScreen libs.baseclass.index_screen.IndexScreen
#:import HomeScreen libs.baseclass.home_screen.HomeScreen
#:import HistoryScreen libs.baseclass.history.HistoryScreen
#:import Quran_factScreen libs.baseclass.quran_fact.Quran_factScreen
#:import HadditsScreen libs.baseclass.haddits.HadditsScreen
#:import ScienceScreen libs.baseclass.science.ScienceScreen
#:import DeshScreen libs.baseclass.desh.DeshScreen

Page_manager:
    transition: FadeTransition()

    # IndexScreen:
    #     name: "index"

    HomeScreen:
        name: "home"
    
    HistoryScreen:
        name: 'history'
    
    Quran_factScreen:
        name: 'quran_fact'
    
    HadditsScreen:
        name: 'haddits'
    
    ScienceScreen:
        name: 'science'
    
    DeshScreen:
        name: 'desh'

"""

class Page_manager(Factory.ScreenManager):
    """The Root (or Assembler) of the App."""
    pass




pages="""
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import HomeScreen Views.home_screen.HomeScreen
#:import IndexScreen Views.index_screen.IndexScreen

ScreenManager:
    IndexScreen:
        name: "index"

    HomeScreen:
        name: "home"
"""