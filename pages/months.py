from selenium import webdriver 
import navbar
import re

class Months(navbar.NavBar):
	shoe_list_id = "shoe_list"
	shoe_image_class_name = "shoe_image"
	shoe_description_class_name = "shoe_description"
	shoe_price_class_name = "shoe_price"

	def __init__(self, webdriver):
		self.driver = webdriver

	def get_shoe_list_ids(self):
		shoe_list = self.driver.find_element_by_id(self.shoe_list_id)
		shoes = shoe_list.find_elements_by_tag_name("li")
		shoes_id = []
		for shoe in shoes:
			shoes_id.append(shoe.get_attribute("id"))
		return shoes_id

	def check_if_discription_exists_for_id(self, shoe_id):
			shoe = self.driver.find_element_by_id(shoe_id)
			shoe_description = self.driver.find_element_by_class_name(self.shoe_description_class_name)

			return shoe_description.text != ""


	def check_if_image_exists_for_id(self, shoe_id):
			shoe = self.driver.find_element_by_id(shoe_id)
			shoe_image = shoe.find_element_by_class_name(self.shoe_image_class_name).find_element_by_tag_name("img")
			image_url=shoe_image.get_attribute("src")

			return image_url != ""

	def check_if_price_exists_for_id(self, shoe_id):
		shoe = self.driver.find_element_by_id(shoe_id)
		shoe_price = shoe.find_element_by_class_name(self.shoe_price_class_name)

		#check for $0[0].00 format of price
		pattern = re.compile("^\$[\d,]+\.\d\d")
		return pattern.match(shoe_price.text)