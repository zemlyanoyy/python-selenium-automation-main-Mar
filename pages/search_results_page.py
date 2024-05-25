from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_SHOWN = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_results(self, expected_product):
        actual_text = self.find_element(*self.SEARCH_RESULT_SHOWN).text
        assert expected_product in actual_text, f"Expected word {expected_product} not in {actual_text}"