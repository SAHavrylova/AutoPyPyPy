from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class TrackInvoice(BasePage):
    URL = "https://novaposhta.ua/"

    def __init__(self) -> None:
        super().__init__()

    def move_to(self):
        self.driver.get(TrackInvoice.URL)
    
    def write_number(self, number):
        # Find the field where enter the invoice number
        invoice_elem = self.driver.find_element(By.ID, "cargo_number")

        #Enter incorrect invoice
        invoice_elem.send_keys(number)

        #Find button Submit
        btn_elem = self.driver.find_element(By.CSS_SELECTOR, '.search_cargo_form input[type="submit"]')

        #Emulate a left mouse btn click
        btn_elem.click()
    
    def check_title(self, exp_title):
        return self.driver.title == exp_title
