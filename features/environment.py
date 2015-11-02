from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.homePage import HomePage

import config
def before_all(context):
	#checks config.py to determine proper browser
	browser = str.lower(config.browser)
	if browser == "firefox":
		driver = webdriver.Firefox()
	elif browser == "chrome":
		driver = webdriver.Chrome("./chromedriver")
	elif browser == "ie":
		driver = webdriver.Ie("./selenium-server-standalone-2.48.2.jar")
	else:
		raise Exception("No appropriate browser selected, please check config.py")

	#navigates to home page
	currentPage =  HomePage(driver)
	try:
		#wait for inital page to load
		element = WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.LINK_TEXT, "January")))
	except:
		#if loading fails then quit
		driver.quit()
		raise

	#add browser and currentpage to context
	context.browser = driver
	context.currentPage = currentPage
	

def after_all(context):
	#after tests close browser
	context.browser.quit()