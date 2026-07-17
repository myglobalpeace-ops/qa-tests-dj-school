from pages.home_page import HomePage



def test_homepage_open(driver):

    page = HomePage(driver)


    page.open()


    assert "DJ" in page.get_title()