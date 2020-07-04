from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
import time
import random
from motivation import motivation, emoji
from secret import email, password, post

class Flooder:
	def __init__(self, url):
		self.option = webdriver.ChromeOptions()   
		self.chrome_options = Options() 
		self.chrome_options.add_argument("--headless")
		#self.option = webdriver.FirefoxOptions()
		self.driver = webdriver.Chrome(executable_path='./chrome83')
		#self.driver = webdriver.Firefox(executable_path='./geckodriver')
		self.url = url
		self.email = email()
		self.password = password()
		self.counting = 0
		self.phrases = motivation()



	def login(self):
		self.driver.get(self.url)
		user = self.driver.find_element_by_id('email')
		user.click()
		user.send_keys(self.email)
		passwrd = self.driver.find_element_by_id('pass')
		passwrd.click()
		passwrd.send_keys(self.password)
		login = self.driver.find_element_by_id('u_0_2').click()
		time.sleep(3)
		

	def flood(self, qty):
		contador = 0
		while contador <= qty:
			time.sleep(1)
			try:
				coment_button = self.driver.find_element_by_xpath("//*[contains(text(),'Comentar')]").click()
				text_box = self.driver.find_element_by_class_name('_1mj')
				text_box.click()
				time.sleep(1)
				if 'chrome' in str(self.driver):
					text_box.send_keys(f'"{random.choice(motivation())}" :|] [Bot motivacional] {random.choice(emoji())}')
					text_box.send_keys(Keys.ENTER)
					time.sleep(1)
					contador += 1
				else:
					text_box.send_keys(f'"{random.choice(motivation())}" :|] [Bot motivacional] {random.choice(emoji())}')
					text_box.send_keys(Keys.ENTER)
					time.sleep(1)
					contador += 1	
			except:
				time.sleep(1)
				text_box = self.driver.find_element_by_class_name('_1mj')
				text_box.click()
				
				if 'chrome' in str(self.driver):
					text_box.send_keys(f'"{random.choice(motivation())}" :|] [Bot motivacional] {random.choice(emoji())}')
					text_box.send_keys(Keys.ENTER)
					time.sleep(1)
					contador += 1
				else:
					text_box.send_keys(f'"{random.choice(motivation())}" :|] [Bot motivacional] {random.choice(emoji())}')
					text_box.send_keys(Keys.ENTER)
					time.sleep(1)
					contador += 1	
			

app = Flooder(post())
app.login()
app.flood(250000)
