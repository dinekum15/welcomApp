from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

import json
import requests

Window.size = (340, 600)

class LoginScreen(Screen):
	pass

class MainScreen(Screen):
	pass

class WindowManager(ScreenManager):
	pass

kv = Builder.load_file('welcom.kv')		
wm = WindowManager()
wm.add_widget(LoginScreen(name='login'))
wm.add_widget(MainScreen(name='main'))
wm.current='login'


class welcomApp(App):
	auth_key = 'PYLzTEO8YhZacPGceFwJe56pbRTazFZdDERAzP6I'
	url = 'https://screendatabase-908ba.firebaseio.com/Users'
		
	def build(self):
		return wm
	
	def login(self):
		#print(self.root.ids.login_screen.ids.staffno.text)
		uid = self.root.ids.login_screen.ids.staffno.text
		pwd = self.root.ids.login_screen.ids.pwd.text
		self.logincheck = False
		if uid!='' and pwd!='':
			if self.validateLogin(uid, pwd):
				self.logincheck = True
				self.userInfo = self.GetFromDB(uid)
				#print(self.userInfo)
				self.welcom()
				self.root.ids.login_screen.ids.staffno.text = ''
				self.root.ids.login_screen.ids.pwd.text = ''
				self.root.ids.login_screen.ids.loginerror.text = ''
			else:
				self.root.ids.login_screen.ids.loginerror.text = 'Incorrect staff no or password'
		else:
			self.root.ids.login_screen.ids.loginerror.text = 'Enter your login details'
	
	def welcom(self):
		wm.current = 'main'
		if self.logincheck:
			self.root.ids.main_screen.ids.uName.text = self.userInfo['Name']
			self.root.ids.main_screen.ids.uStaffNo.text = self.userInfo['Staff_No']
	
	def validateLogin(self, *args):
		url = f'{self.url}/{args[0]}/.json'
		data = requests.get(url+'?auth='+self.auth_key).json()
		if args[0] == data['Staff_No'] and args[1] == data['Password']:
			return True
		else:
			return False
	def GetFromDB(self,*args):
		url = f'{self.url}/{args[0]}/.json'
		data = requests.get(url+'?auth='+self.auth_key).json()
		return data

welcomApp().run()