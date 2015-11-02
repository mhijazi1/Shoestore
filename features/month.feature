Feature: Monthly display of new releases
	In order to view upcoming shoes being released every month
	As a user off the Shoe store.
	I want to be able to visit a link for each month and see the shoes being released

Scenario Outline: Month should display a small blurb, image, and have a suggested price for each shoe
	Given I am on the <Month> release page
	Then I should see a small Blurb of each shoe
	And I should see an image for each shoe
	And I should see a suggested price for each shoe

	Examples: Months
	| Month       |
	| "January"   |
	| "February"  |
	| "March"     |
	| "April"     |
	| "May"       |
	| "June"      |
	| "July"      |
	| "August"    |
	| "September" |
	| "October"   |
	| "November"  |
	| "December"  |