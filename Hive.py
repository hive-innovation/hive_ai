import kivy
from kivymd.app import MDApp 
from kivy.lang import Builder 
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import BooleanProperty, DictProperty, ListProperty, NumericProperty, ObjectProperty, OptionProperty, StringProperty
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.animation import cos
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.screen import MDScreen 
#from kivymd.uix.picker.MDThemepicker import MDThemepicker
from kivymd.app import MDApp 
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests

##''''Ímporting all the screens and widget we have  and need in our application''''

Builder.load_file('kivy/pages/home.kv')
Builder.load_file('main.kv')
Builder.load_file('kivy/pages/dashboard.kv')
Builder.load_file('kivy/pages/home.kv')
Builder.load_file('kivy/pages/group_screen.kv')
Builder.load_file('kivy/pages/call_screen.kv')
Builder.load_file('kivy/pages/chat_screen.kv')
Builder.load_file('kivy/front_end/story_layout.kv')
Builder.load_file('kivy/front_end/avatar.kv')
Builder.load_file('kivy/front_end/chat_list_item.kv')
Builder.load_file('kivy/front_end/group_list_item.kv')
Builder.load_file('kivy/front_end/call_list_item.kv')
Builder.load_file('kivy/front_end/bottom_navigator.kv')
Builder.load_file('kivy/front_end/text_field.kv')
Builder.load_file('kivy/front_end/chatbubble.kv')
Builder.load_file('kivy/front_end/login.kv')
Builder.load_file('kivy/front_end/signup.kv')


Window.size = (320, 600) #giving the size of our application,, but when transforming it to android or ios we will remove it,this is to see how it will look on phone

class WindowManager(ScreenManager):
	'''A window manager to manage switching between sceens.'''

class HiveMain(Screen):
	'''A screen that display the story fleets and all message histories.'''

class CallScreen(Screen):
	'''A screen that display the call histories.'''

class ChatScreen(Screen):
	'''A screen that display messages with a user.'''#still to come since we will have a forum

	text = StringProperty()
	image = ObjectProperty()
	active = BooleanProperty(defaultvalue=False)

class StoryWithImage(MDBoxLayout):
	'''A horizontal layout with an image(profile picture)
		and a text(username) - The Story.'''

	text = StringProperty()
	source = StringProperty()

class ChatListItem(MDCard):
	'''A clickable chat item for the chat timeline.'''

	isRead = OptionProperty(None, options=['delivered', 'read', 'new', 'waiting'])
	friend_name = StringProperty()
	mssg = StringProperty()
	timestamp = StringProperty()
	friend_avatar = StringProperty()
	profile = DictProperty()

class GroupListItem(MDCard):
	'''A clickable chat item for the group chat timeline.'''

	isRead = OptionProperty(None, options=['delivered', 'read', 'new', 'waiting'])
	group_name = StringProperty()
	group_avatar = StringProperty()
	friend_mssg = StringProperty()
	timestamp = StringProperty()

class ChatBubble(MDBoxLayout):
	'''A chat bubble for the chat screen messages.'''

	profile = DictProperty()
	msg = StringProperty()
	time = StringProperty()
	sender = StringProperty()
	isRead = OptionProperty('waiting', options=['read', 'delivered', 'waiting'])

class GroupScreen(Screen):
	'''A screen that display messages history in groups .'''


class Login(Screen):
	'''A screen that display messages history in groups .'''
	
class Signup(Screen):
	'''A screen that display messages history in groups .'''
	
class Dashboard(Screen):
	'''A screen that display messages history in groups .'''

	
class HomeScreen(Screen):
	'''A screen that display messages history in groups .'''

class HiveMain(Screen):
	'''A screen that display messages history in groups .'''



class Hive(MDApp): 
	''' The main App class using kivymd's properties.'''

	def build(self): 
		''' Initializes the Application
		and returns the root widget'''
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_palette = 'Teal'
		self.theme_cls.accent_palette = 'Teal'
		self.theme_cls.normal = 'white'
		self.theme_cls.accent_hue = '400'
		self.title = "Hive"
		self.wm = WindowManager(transition=FadeTransition())
		screens = [
			HiveMain(name='home'), GroupScreen(name='group'), CallScreen(name='call'), 
			HomeScreen(name='homescreen'),
			ChatScreen(name='chat'), Dashboard(name='dashboard'), Signup(name='signup'),
			Login(name='login')
		]
		for screen in screens:
			self.wm.add_widget(screen)
		
		self.url  = "https://loginsetup-14858.firebaseio.com/.json"
		

	
##############Building the bottom overlay as when u click the button########
		return self.wm
	def callback_for_menu_item(self,*args):
		toast(args[0])

	def show_grid(self):
		bottom_sheet_menu = MDGridBottomSheet()
		data={
			"Facebook":"facebook",
			"YouTube":"youtube",
			"Twitter":"twitter",
			"Da Cloud":"cloud-upload",
			"Camera":"camera",
} 
		for item in data.items():
			bottom_sheet_menu.add_item(
				item[0],
				lambda x, y=item[0]: self.callback_for_menu_item(y),
				icon_src=item[1]
			)
		bottom_sheet_menu.open()
		##ends here
	def change_screen(self, screen):
		'''Change screen using the window manager.'''
		self.wm.current = screen

	def show_theme_picker(self):
		'''Display a dialog window to change app's color and theme.'''
		theme_dialog = MDThemepicker()
		theme_dialog.open()
	

	
## for this i am trying to get the info placed in the form by our user so i can validate then store in our real time database##
	def signup(self):
		signupEmail = self.wm.get_screen('signup').ids.signup_email.text
		signupPassword = self.wm.get_screen('signup').ids.signup_password.text
		signupUsername = self.wm.get_screen('signup').ids.signup_username.text
		if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
			cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
			self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
			self.dialog.open()
		if len(signupUsername.split())>1:
			cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
			self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username without space',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
			self.dialog.open()
		#if "@"  not in signupEmail:
		#	cancel_btn_Email_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_Email_dialog)
		#	self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_Email_dialogue])
		#	self.dialog.open()
			
		else:
			print(signupEmail,signupPassword)
			signup_info = str({f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
			signup_info = signup_info.replace(".","-")
			signup_info = signup_info.replace("\'","")
			to_database = json.loads(signup_info)
			print((to_database))
			requests.patch(url = self.url,json = to_database)
			self.strng.get_screen('login').manager.current = 'login'
	auth = '0QjlZHsBsviGEbNRPNPdMZwq5UDBI1B0qdg9Ogvd' # this is the auth key for our database

	##this pat is still coming##dont mind about it
	def create_chat(self, profile):
		'''Get all messages and create a chat screen'''
		self.chat_screen = ChatScreen()
		self.msg_builder(profile, self.chat_screen)
		self.chat_screen.text = profile['name']
		self.chat_screen.image = profile['image']
		self.chat_screen.active = profile['active']
		self.wm.switch_to(self.chat_screen)
#coming soon
		
	def msg_builder(self, profile, screen):
		'''Create a message bubble for creating chat.'''
		for prof in profile['msg']:
			for messages in prof.split("~"):
				if messages != "":
					message, time, isRead, sender = messages.split(";")
					self.chatmsg = ChatBubble()
					self.chatmsg.msg = message
					self.chatmsg.time = time
					self.chatmsg.isRead = isRead
					self.chatmsg.sender = sender
					screen.ids['msglist'].add_widget(self.chatmsg)
				else:
					print("No message")

				print(self.chatmsg.isRead)
	def login(self):###validation login then redirect to the home screen
		loginEmail = self.wm.get_screen('login').ids.login_email.text
		loginPassword = self.wm.get_screen('login').ids.login_password.text

		self.login_check = False
		supported_loginEmail = loginEmail.replace('.','-')
		supported_loginPassword = loginPassword.replace('.','-')
		request  = requests.get(self.url+'?auth='+self.auth)
		data = request.json()
		emails= set()
		for key,value in data.items():
			emails.add(key)
		if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
			self.username = data[supported_loginEmail]['Username']
			self.login_check=True
			self.wm.get_screen('homescreen').manager.current = 'homescreen'
		else:
			print("user no longer exists")
	def close_username_dialog(self,obj):
		self.dialog.dismiss()
	def close_Email_dialog(self,obj):
		self.dialog.dismiss()
	def username_changer(self):
		if self.login_check:
			self.wm.get_screen('homescreen').ids.username_info.text = f"welcome {self.username}"
	def grouplist_builder(self):
		
		for group in demo.group.groups:
			self.groupitem = GroupListItem()
			self.groupitem.group = group
			self.groupitem.group_name = group['name']
			self.groupitem.group_avatar = group['image']
			self.groupitem.friend_mssg, self.groupitem.timestamp, self.groupitem.isRead = group['msg'].split(';')
			self.wm.screens[1].ids['grouplist'].add_widget(self.groupitem)   

if __name__ == "__main__":
	Hive().run()