@given(u'I am on the "{month}" release page')
def i_am_on_the_a_month_release_page(context, month):
	#get current page from context 
	currentPage = context.currentPage
	#navigate to {month} page
	context.currentPage = currentPage.goToMonth(month)