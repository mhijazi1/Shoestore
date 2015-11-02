Feature: Submit email for reminder
	In order to be reminded of upcoming shoe releases
	As a User of the Shoe store
	I want to be able to submit my email address

Scenario: On successful submission of a valid email address user should receive a confirmation message
	Given there is an area to submit my email address
	When I submit a valid email address
	Then I should receive a message 

Scenario: On successful submission of a invalid email address user should not receive a confirmation message
	Given there is an area to submit my email address
	When I submit an invalid email address
	Then I should not receive a message 

Scenario: On successful submission of an empty email address user should not receive a confirmation message
	Given there is an area to submit my email address
	When I submit an invalid email address
	Then I should not receive a message 