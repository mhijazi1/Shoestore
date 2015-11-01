from behave import given, when, then


@given(u'I am on the "{month}" release page')
def i_am_on_the_december_release_page(context, month):
    raise NotImplementedError(u'STEP: I am on the December release page')


@then(u'I should see an image for each shoe')
def i_should_see_an_image_for_each_shoe(context):
    raise NotImplementedError(u'STEP: I should see an image for each shoe')


@then(u'I should see a suggested price for each shoe')
def i_should_see_a_suggested_price_for_each_shoe(context):
    raise NotImplementedError(u'STEP: I should see a suggested price for each shoe')


@then(u'I should see a small Blurb of each shoe')
def i_should_see_a_small_blurb_of_each_shoe(context):
    raise NotImplementedError(u'STEP: I should see a small Blurb of each shoe')

