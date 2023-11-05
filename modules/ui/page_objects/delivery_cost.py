from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class DeliveryCost(BasePage):
    URL = "https://novaposhta.ua/delivery"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(DeliveryCost.URL)
    
    def check_page_title(self, delivery_cost_title):
        return self.driver.title == delivery_cost_title
    
    def route_sender(self, senderCity):
        #Find sender city element
        sender_city = self.driver.find_element(By.ID, "DeliveryForm_senderCity")
        
        #Enter the city
        sender_city.send_keys(senderCity)

        #Expected result after entered name "Вінниця" and click
        expected_res_sender = self.driver.find_element(By.ID, "lie71629ab-4b33-11e4-ab6d-005056801329")
        expected_res_sender.click()

    def route_recipient(self):
        #Find recipient city element
        recipient_city = self.driver.find_element(By.ID, "DeliveryForm_recipientCity")
        recipient_city.click()
        
        #Find element on dropdown menu
        dropdown_recipient = self.driver.find_element(By.CLASS_NAME, "cdb5c88f5-391c-11dd-90d9-001a92567626")
        recipient_text = dropdown_recipient.text
        assert recipient_text == "Львів"
        dropdown_recipient.click()
    
    def place_character(self, qnt, value, weight, length, width, height):
        #Find quantity element
        quantity_elem = self.driver.find_element(By.CLASS_NAME, "short allowed-char count")
        quantity_elem.send_keys(qnt)
        if int(qnt) > 999:
            quantity_elem.send_keys("999")

        #Find declared value element and send keys
        value_elem = self.driver.find_element(By.CLASS_NAME, "short allowed-char cost")
        value_elem.send_keys(value)

        #Find weight element and send keys
        weight_elem = self.driver.find_element(By.CLASS_NAME, "short allowed-char weight")
        weight_elem.send_keys(weight)

        #Find length element and send keys
        length_elem = self.driver.find_element(By.CLASS_NAME, "allowed-char volumetricLength")
        length_elem.send_keys(length)

        #Find width element and send keys
        width_elem = self.driver.find_element(By.CLASS_NAME, "allowed-char volumetricWidth")
        width_elem.send_keys(width)
        
        #Find height element and send keys
        height_elem = self.driver.find_element(By.CLASS_NAME, "allowed-char volumetricHeight")
        height_elem.send_keys(height)
    
    def btn_submit(self):
        btn_submit = self.driver.find_element(By.CLASS_NAME, "btn submit")
        btn_submit.click()
    
    def check_results(self, expected_title):
        return self.driver.title == expected_title

