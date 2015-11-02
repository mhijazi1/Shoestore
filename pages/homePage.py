from selenium import webdriver 
import navbar


class HomePage(navbar.NavBar):
	pageUrl = "http://shoestore-manheim.rhcloud.com/"

	def __init__(self, webdriver):
		self.driver = webdriver
		self.driver.get(self.pageUrl)
	
		