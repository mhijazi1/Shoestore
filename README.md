# Shoestore
## Setup
Gherkin project for testing [Shoestore](http://shoestore-manheim.rhcloud.com/) using behave and selenium
In order to run the tests you will need the behave and selenium modules and python

For instructions on installing behave please see this [page](http://pythonhosted.org/behave/)

For instructions on installing selenium please see this [page](http://selenium-python.readthedocs.org/installation.html)

Additionally you can setup the type of browser used from the config.py file.
Firefox is used and avalible by default
Chrome and IE drivers need to be added to the root directory to be used.
they can be found here

[Chrome](https://sites.google.com/a/chromium.org/chromedriver/home)

[IE](https://sites.google.com/a/chromium.org/chromedriver/home) *WINDOWS ONLY*!!!

## Usage

From the Shoestore directory simply execute `behave` from the command line


##Notes
Please note that 3 of the tests should fail 

the november month test for images

    features/month.feature:24  Month should display a small blurb, image, and have a suggested price for each shoe -- @1.11 Months
    Assertion Failed: No image found for shoe with id charlotte_olympia_charlotte_olympia'parisienne'sandal

entering an invalid email address for the reminder email

    features/reminder.feature:11  On successful submission of a invalid email address user should not receive a confirmation message
    Assertion Failed: Empty email returns a positive response


entering no email address for the reminder email

    features/reminder.feature:16  On successful submission of an empty email address user should not receive a confirmation message
    Assertion Failed: Empty email returns a positive response
