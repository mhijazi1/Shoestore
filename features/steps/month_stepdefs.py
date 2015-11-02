from behave import given, when, then


@then(u'I should see an image for each shoe')
def i_should_see_an_image_for_each_shoe(context):
	#get current page from context (month page)
	currentPage = context.currentPage
	#get id's of all shoes listed 
	shoe_ids = currentPage.get_shoe_list_ids()
	for shoe_id in shoe_ids:
		assert currentPage.check_if_image_exists_for_id(shoe_id), "No image found for shoe with id " + shoe_id




@then(u'I should see a suggested price for each shoe')
def i_should_see_a_suggested_price_for_each_shoe(context):
	#get current page from context (month page)
	currentPage = context.currentPage
	#get id's of all shoes listed 
	shoe_ids = currentPage.get_shoe_list_ids()
	for shoe_id in shoe_ids:
		assert currentPage.check_if_price_exists_for_id(shoe_id), "No price found for shoe with id " + shoe_id



@then(u'I should see a small Blurb of each shoe')
def i_should_see_a_small_blurb_of_each_shoe(context):
	#get current page from context (month page)
	currentPage = context.currentPage
	#get id's of all shoes listed 
	shoe_ids = currentPage.get_shoe_list_ids()
	for shoe_id in shoe_ids:
		assert currentPage.check_if_discription_exists_for_id(shoe_id), "No description found for shoe with id " + shoe_id