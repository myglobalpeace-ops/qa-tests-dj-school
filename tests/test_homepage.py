from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_homepage_open():

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.get(
        "https://myglobalpeace-ops.github.io/DJ-Shool/"
    )


    assert "DJ" in driver.title


    driver.quit()