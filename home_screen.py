
from kivymd.app import MDApp
from kivy.factory import Factory
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex

class Shots(MDBoxLayout):
    pass



class Header(MDBoxLayout):
    pass

class DataCard(MDCard, RoundedRectangularElevationBehavior):
        
    cardtext = ''  #StringProperty()
    pass

    



class HomeScreen(MDScreen):
    """
    Example Screen.
    """




home_screen_string ='''
#: import environ os.environ
#: import get_color_from_hex kivy.utils.get_color_from_hex
<HomeScreen>
	id:home_layout
    name:'home'

	MDBoxLayout: 
		
		orientation: 'vertical'
		#adaptive_size: True
		size_hint:1,1
		#pos_hint: {'top':1.0}
		padding: '2dp'
        ScrollView:
			do_scroll_y:True
			do_scroll_x:False
			size_hint:1,1
			size:self.size
			bar_color:1,1,1,1
			GridLayout:
				size_hint_y: None
				height:self.minimum_height
				width: self.minimum_width
				cols:1
				#row_force_default:True
				#row_default_height:'45dp'
				spacing:'9dp'

				Header:                                   #toolbar

				MDBoxLayout:                              # Custom Tab tab
					size_hint_y:None
					height:'40dp'
					spacing:'4dp'
					padding:'12dp',0,'12dp',0
					#pos_hint: {'center_y':0.85}

					#padding: '10dp'
					ScrollView:
						do_scroll_y: False
						do_scroll_x: True
						size: self.size
						bar_color:1,1,1,1
						bar_inactive_color:1,1,1,1
						GridLayout:
							size_hint_x: None
							height:self.minimum_height
							width: self.minimum_width
							rows:1
							spacing:'10dp'
							
							MDRoundFlatButton:
								text:'History of Islam'
								size_hint:None,None
								width: '35dp'
								height: '20dp'
								pos_hint: {'center_y': 0.5}
								on_release: root.manager.current = "history"
							MDRoundFlatButton:
								text:"Quran's fact"
								size_hint:None,None
								width: '35dp'
								height: '20dp'
								pos_hint: {'center_y': 0.5}
								on_release: root.manager.current = "quran_fact"
							MDRoundFlatButton:
								text:'Haddits'
								size_hint:None,None
								width: '35dp'
								height: '20dp'
								pos_hint: {'center_y': 0.5}
								on_release: root.manager.current = "haddits"
							MDRoundFlatButton:
								text:'Science'
								size_hint:None,None
								width: '35dp'
								height: '20dp'
								pos_hint: {'center_y': 0.5}
								on_release: root.manager.current = "science"
							MDRoundFlatButton:
								text:'Desh'
								size_hint:None,None
								width: '35dp'
								height: '20dp'
								pos_hint: {'center_y': 0.5}
								on_release: root.manager.current = "desh"

				Shots:                                    # shots

				MDCard:
					md_bg_color: [0,1,1,1]
					size_hint_y:None
					#pos_hint:{'top':.41}
					MDLabel:
						text: "Title"
						theme_text_color: "Secondary"
						size_hint_y: None
						#height: self.texture_size[1]
				DataCard:

				MDCard:
					md_bg_color: [1,0,1,1]
					size_hint_y:None
					#pos_hint:{'top':.38}
					
				MDCard:
					md_bg_color: [1,1,0,1]
					size_hint_y:None
					#pos_hint:{'top':.33}
				MDCard:
					md_bg_color: [0,1,1,1]
					size_hint_y:None
					#pos_hint:{'top':.41}
				MDCard:
					md_bg_color: [1,0,1,1]
					size_hint_y:None
					#pos_hint:{'top':.38}
					
				MDCard:
					md_bg_color: [1,1,0,1]
					size_hint_y:None
					#pos_hint:{'top':.33}




<DataCard>:
	padding: 16
	md_bg_color: [1,0,1,1]
	size_hint_y:None
	size: self.size
	ext: "Title"
	MDRelativeLayout:
		size_hint: None, None
		size: root.size
		MDIconButton:
			icon: "dots-vertical"
			pos:
				root.width - (self.width + root.padding[0] + dp(4)), \
				root.height - (self.height + root.padding[0] + dp(4))
		MDLabel:
			id: label
			text: root.cardtext
			adaptive_size: True
			color: .2, .2, .2, .8













<Header>:                               # toolbar
	#pos_hint: {'top': 1.0}
	size_hint_y:None
	height:'60dp'
	spacing:'10dp'
	padding:'12dp',0,'12dp',0
	FitImage:
		id:im
		source: f"{environ['RED_Mobile_App_ROOT']}/assets/images/05.jpg"
		mipmap: True
		size_hint: None, None
		size:'40dp','40dp'
		pos_hint: {'center_y': 0.5}
		radius:[30,]
	MDLabel:
		text:'RED'
		font_style:'H5'
		bold:True
	MDIconButton:
		icon:'hand-heart'
		pos_hint: {'center_y': 0.5}
		radius:[30,]
	MDIconButton:
		icon:'logout'
		pos_hint: {'center_y': 0.5}
		radius:[30,]




<Shots>:                               # shots
	#pos_hint:{'top':.64}
	size_hint_y:None
	height:'182dp'
	padding:'2dp'
	spacing:'10dp'
	FitImage:
		source:f"{environ['RED_Mobile_App_ROOT']}/assets/images/demo_pic1.jpg"
		mipmap: True
		size_hint: None, None
		size:'120dp','180dp'
		pos_hint: {'center_y': 0.5}
		radius:[5,]
	FitImage:
		source:f"{environ['RED_Mobile_App_ROOT']}/assets/images/demo_pic2.jpg"
		mipmap: True
		size_hint: None, None
		size:'120dp','180dp'
		pos_hint: {'center_y': 0.5}
		radius:[5,]





		#   MDBoxLayout:
		#   	 size_hint_y:.35
		# 	   padding:'10dp'
		# 	   spacing:'10dp'
		# 	   pos_hint:{'top':.44}
		# 	   CustomTexInput:
		# 	   	 hint_text:"search"




	# MDRoundFlatButton:
	# 	text:'profile'
	# 	pos_hint:{'center_x': 0.5,'center_y': 0.5}
	# 	on_press: root.manager.current = 'login_page'















# MDBoxLayout:                               # toolbar'''