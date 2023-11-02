import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_by_id():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_data():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0
    

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовник", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    #Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром" 


@pytest.mark.database
def test_check_all_products():
    db = Database()
    products = db.get_all_products()

    print(products)


@pytest.mark.database
def test_check_address_by_postal_code():
    db = Database()
    address = db.get_address_by_postal_code("2055")

    assert address[0][0] == "Stepana Bandery str, 2"
    print("This addres in the Database")


@pytest.mark.database
def test_check_add_postal_code():
    db = Database()
    db.insert_postal_code_to_customer(55, "Vinn", "2100", "Ukraine")
    db.delete_code_by_id(55)
    id = db.get_all_customers_id()
    assert id != 55


@pytest.mark.database
def test_check_all_customers_id():
    db = Database()
    customer_id = db.get_all_customers_id()

    print(customer_id)

'''Сommented on this type because it is for removing codes by id

@pytest.mark.database
def test_delete_by_customers_id():
    db = Database()
    db.delete_code_by_id(55)
    ids_qnt = db.get_all_customers_id()

    print(ids_qnt)
'''


@pytest.mark.database
def test_check_add_invalid_postal_code():
    db = Database()
    db.insert_postal_code_to_customer(155, "Vinn", 2100, "Ukraine")
    new_city = db.get_user_city_and_postalCode("Vinn", "2100")
    
    assert new_city[0][0] == "Vinn" 
    assert new_city[0][1] == "2100"
    
    db.update_postal_code_by_city_and_id(155, "Vinn", "21000")
    updated_city = db.get_user_city_and_postalCode("Vinn", "21000")
    
    assert updated_city[0][0] == "Vinn" and updated_city[0][1] == "21000"
    print(updated_city, "are updated")
    
    db.delete_code_by_id(155)
    id_str = db.get_all_customers_id()
    
    assert id_str != 155
    print("Test completed successfully")
