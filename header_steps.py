from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

@when("Search for {search_query}")
def search_product(context, search_query):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_query)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(7)