from css_selectors import driver
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)


# reference
# app = Application(driver)
# app.main_page
# app.header
# app.search_results_page