from modules.ui.page_objects.track_invoice import TrackInvoice
import pytest

@pytest.mark.ui
def test_check_incorrect_invoice_number():
    track_invoice = TrackInvoice()

    #GO to https://novaposhta.ua/
    track_invoice.move_to()

    #Enter voice number
    track_invoice.write_number(59500000031324)

    assert track_invoice.check_title("Керуйте доставкою посилок Нової пошти")
    
    track_invoice.close()
