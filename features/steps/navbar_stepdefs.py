from behave import given, when, then
from pages.navbar import NavBar

validEmail = "valid@email.com"
invalidEmail = "notanemail"
message = "Thanks! We will notify you of our new shoes at this email: "

@given(u'there is an area to submit my email address')
def there_is_an_area_to_submit_my_email_address(context):
	assert context.currentPage.check_if_reminder_email_input_exists(), "No email input area found"

@when(u'I submit a valid email address')
def i_submit_a_valid_email_address(context):
	context.currentPage.submit_email(validEmail)
	context.inputemail = validEmail
@when(u'I submit an invalid email address')
def i_submit_an_invalid_email_address(context):
	context.currentPage.submit_email(invalidEmail)
	context.inputemail = invalidEmail
@when(u'I submit an empty email address')
def i_submit_an_empty_email_address(context):
	context.currentPage.submit_email("")
	context.inputemail = ""

@then(u'I should receive a message')
def i_should_recive_a_message(context):
	output = message + context.inputemail
	assert context.currentPage.get_flash_notice() == output, "Valid email does not return a positive response"

@then(u'I should not receive a message')
def i_should_not_recive_a_message(context):
	output =  message + context.inputemail
 	assert context.currentPage.get_flash_notice() != output, "Invalid email returns a positive response"
