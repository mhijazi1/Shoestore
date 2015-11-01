Feature: Submit email for reminder
	In order to be reminded of upcoming shoe releases
	As a User of the Shoe store
	I want to be able to submit my email address

Scenario: On successful submission of a valid email address user should receive a message
	Given there is an area to submit my email address
	When I submit my email address
	Then I should recive a message 