from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:

    SEARCH_INPUT_FIELD_LOCATOR = (By.ID, 'search_form_input')
    RESULT_LINK_LOCATOR = (By.CSS_SELECTOR, 'a[data-testid="result-title-a"')
    MORE_RESULTS_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'a.result--more__btn')

    def __init__(self, browser):
        self.browser = browser

    def get_page_title(self):
        return self.browser.title

    def get_search_phrase(self):
        search_input_field = self.browser.find_element(*self.SEARCH_INPUT_FIELD_LOCATOR)
        search_phrase = search_input_field.get_attribute('value')
        return search_phrase

    def get_result_links_titles(self):
        result_links = self.browser.find_elements(*self.RESULT_LINK_LOCATOR)
        result_links_titles = [result_link.text for result_link in result_links]
        return result_links_titles

    def get_more_results_button(self):
        first_more_results_buttons = self.browser.find_element(*self.MORE_RESULTS_BUTTON_LOCATOR)
        return first_more_results_buttons
