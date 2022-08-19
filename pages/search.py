from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

    URL = 'https://www.duckduckgo.com'
    SEARCH_INPUT_FIELD_LOCATOR = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser, search_phrase=None):
        self.browser = browser

        if search_phrase is None:
            self.search_phrase = "goose"
        else:
            self.search_phrase = search_phrase

    def load(self):
        self.browser.get(self.URL)

    def search(self):
        search_input_field = self.browser.find_element(*self.SEARCH_INPUT_FIELD_LOCATOR)
        search_input_field.send_keys(self.search_phrase + Keys.RETURN)
