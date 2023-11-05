from modules.ui.page_objects.delivery_cost import DeliveryCost 
import pytest
import time

@pytest.mark.mui
def test_check_delivery_cost():
    delivery_cost = DeliveryCost()

    #Open page https://novaposhta.ua/delivery
    delivery_cost.go_to()

    time.sleep(1)

    #Check page title
    delivery_cost.check_page_title("Вартість доставки")

    #Enter all inputs
    delivery_cost.route_sender("Вінниця")
    delivery_cost.route_recipient()
    time.sleep(2)
    
    delivery_cost.place_character(14, 10, 50, 60, 70)
    time.sleep(1)

    delivery_cost.btn_submit()
    time.sleep(2)

    delivery_cost.check_results("Вартість доставки")

    delivery_cost.close()