from selenium.webdriver.common.keys import Keys
import time

class NavBar(object):
	
	reminder_email_id = "remind_email_input"
	flash_id = "flash"
	flash_notice_class = "notice"

	def goToMonth(self, month):
		self.month = self.driver.find_element_by_link_text(month)
		self.month.click()
		from pages.months import Months
		return Months(self.driver)

	def check_if_reminder_email_input_exists(self):
		reminder_email_input = self.driver.find_elements_by_id(self.reminder_email_id)
		return reminder_email_input
	
	def submit_email(self, email):
		reminder_email_input = self.driver.find_element_by_id(self.reminder_email_id)
		reminder_email_input.send_keys(email)
		reminder_email_input.send_keys(Keys.RETURN)
		time.sleep(2)

	#get email regestration message
	def get_flash_notice(self):
		flash_notice = self.driver.find_elements_by_class_name(self.flash_notice_class)

		if flash_notice:
			return flash_notice[0].text
		else: 
			return ""