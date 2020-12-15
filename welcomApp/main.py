from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window

import json
import requests

Window.size = (340, 600)

class LoginScreen(Screen):
	staffno = ObjectProperty(None)
	pwd = ObjectProperty(None)
	loginerror = ObjectProperty(None)

	def login(self):
		uid = self.staffno.text
		pwd = self.pwd.text
		#print(uid, pwd)
		
		if uid!='' and pwd!='':
			if validateLogin(uid, pwd):
				wm.current = 'main'
				MainScreen.userInfo = GetFromDB(uid)
				MainScreen.logincheck=True
				self.staffno.text = ''
				self.pwd.text = ''
				self.loginerror.text = ''
			else:
				self.loginerror.text = 'Incorrect staff no or password'
		else:
			self.loginerror.text = 'Enter your login details'

class MainScreen(Screen):
	uName = ObjectProperty(None)
	uStaffNo = ObjectProperty(None)
	userInfo=''
	logincheck=False
	def on_enter(self):
		if self.logincheck:
			self.uName.text = self.userInfo['Name']
			self.uStaffNo.text = self.userInfo['Staff_No']

class WindowManager(ScreenManager):
	pass

def validateLogin(username, password):
	url = f'{link}/{username}/.json'
	data = requests.get(url+'?auth='+auth_key).json()
	if username == data['Staff_No'] and password == data['Password']:
		return True
	else:
		return False

def GetFromDB(username):
	url = f'{link}/{username}/.json'
	data = requests.get(url+'?auth='+auth_key).json()
	return data

auth_key = 'PYLzTEO8YhZacPGceFwJe56pbRTazFZdDERAzP6I'
link = 'https://screendatabase-908ba.firebaseio.com/Users'

kv = Builder.load_file('welcom.kv')		
wm = WindowManager()
wm.add_widget(LoginScreen(name='login'))
wm.add_widget(MainScreen(name='main'))
wm.current='login'


class welcomApp(App):
	
		
	def build(self):
		return wm
	

welcomApp().run()