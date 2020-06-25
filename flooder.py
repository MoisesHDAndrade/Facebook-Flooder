from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from motivation import motivation, emoji

class Flooder:
	def __init__(self, user, password, url):
		self.option = webdriver.ChromeOptions()
		self.driver = webdriver.Chrome(executable_path='./chrome83')
		self.url = url
		self.user = user
		self.password = password
		self.counting = 0
		self.phrases = motivation()

	def login(self):
		self.driver.get(self.url)
		user = self.driver.find_element_by_id('email')
		user.click()
		user.send_keys(self.user)
		passwrd = self.driver.find_element_by_id('pass')
		passwrd.click()
		passwrd.send_keys(self.password)
		login = self.driver.find_element_by_id('u_0_2').click()
		time.sleep(3)
		

	def comment(self,qty):
		while self.counting < qty:
			try:
				time.sleep(1)
				comentary_counter = self.driver.find_element_by_class_name("gtad4xkn")
				if 'comentário' in comentary_counter.text:
					self.counting = int(comentary_counter.text.replace("comentário","").strip())
				if 'comentários' in comentary_counter.text:
					self.counting = int(comentary_counter.text.replace("comentários","").strip())
				print(self.counting)
				text_box = self.driver.find_element_by_class_name('_1mj')
				#text_box = self.driver.find_element_by_xpath("//*[contains(text(),'Escreva um comentário...')]")
				text_box.click()
				time.sleep(1)
				text_box.send_keys(random.choice(motivation()))
				text_box.send_keys(Keys.ENTER)
				time.sleep(1)
			except:
				time.sleep(1)
				print('deu ruim')
				#text_box = self.driver.find_element_by_xpath("//*[contains(text(),'Escreva um comentário...')]")
				text_box = self.driver.find_element_by_class_name('_1mj')
				text_box.click()
				time.sleep(1)
				text_box.send_keys(f'"{random.choice(motivation())}" Bot motivacional {random.choice(emoji())}')
				text_box.send_keys(Keys.ENTER)
				time.sleep(1)
			

			

app = Flooder('your user login','your password', 'post url')
app.login()
app.comment(3)
