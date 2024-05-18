class BasePage:

    def find_el(self):
        print("Finding element")

    def click(self):
        print("Clicking")

    def verify_text(self, expected_text):
        print(f'Checking for {expected_text}')


class LoginPage(BasePage):

    def login(self, email, password):
        print("Logging in")

    def verify_terms_and_conditions(self): #TC
       self.verify_text("TC text")


class RegPage(BasePage):
    def register(self):
        print("Registering...")


login_page = LoginPage()
reg_page = RegPage()
login_page.login()
login_page.click()

