import pytest
from Employee import Employer
from Database import DataBase

api = Employer("https://x-clients-be.onrender.com")
db = DataBase("postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")

# Получаем список сотрудников из БД и АПИ и сравниваем их
def test_get_list_for_employers():
    # Создаем компанию - БД
    db.create_company('CarService', 'SpaceStar')
    # Получаем ID Последней созданной компании - БД
    max_id = db.last_company_id()
    # Добавляем сотрудника в компанию - БД
    db.create_employer(max_id, 'Alexander', 'Anjievskiy', 9288119108)
    # Получаем список сотрудников из последней созданной компании - БД
    db_employer_list = db.get_list_employer(max_id)
    # Получаем список сотрудников из последней созданной компании - АПИ
    api_emlpoyer_list = api.get_list_employee_company(max_id)
    # Сравниваем списки сотрудников полученных из БД и АПИ
    assert len(db_employer_list) == len(api_emlpoyer_list)
    # Удаляем сотрудника компании, для удаления компании в будущем
    response = (api.get_list_employee_company(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    # Удаляем компанию
    db.delete(max_id)

# Добавляем сотрудника в базу данных и сравниваем данные сотрудника с АПИ
def test_add_new_employer():
    db.create_company('Pelmeni', 'Vkusno')
    max_id = db.last_company_id()
    db.create_employer(max_id, 'Alexander', 'Anjievskiy', 9288119108)
    response = (api.get_list_employee_company(max_id))[0]
    employer_id = response["id"]
    # Сравниваем айди компании
    assert response["companyId"] == max_id
    # Сравниваем имя сотрудника с заданым в БД
    assert response["firstName"] == 'Alexander'
    # Сравниваем статус сотрудника 
    assert response["isActive"] == True
    # Сравниваем фамилию сотрудника с заданной 
    assert response["lastName"] == 'Anjievskiy'
    # Удаляем сотрудника из БД
    db.delete_employer(employer_id)
    # Удаляем последнюю созданную компанию
    db.delete(max_id)

# Сравниваем информацию о сотруднике полученую по АПИ с информацией полученой при создании через БД
def test_info_for_employer():
    db.create_company('GodOfWar','Games')
    max_id = db.last_company_id()
    db.create_employer(max_id,"Admin","littleAdmin", 9888845678)
    employer_id = db.get_employer_id(max_id)
    # Cравниваем информацию о сотруднике полученую через АПИ с инфо полученую через БД
    get_api_info = (api.get_info_for_employee(employer_id)).json()
    assert get_api_info["firstName"] == "Admin"
    assert get_api_info["lastName"] == "littleAdmin"
    assert get_api_info["phone"] == '9888845678'
    # Удаляем созданного сотрудника БД
    db.delete_employer(employer_id)
    # Удаляем компанию БД
    db.delete(max_id)

# Сравниваем информацию о сотруднике полученую по АПИ с измененной информацией о сотруднике в БД
def test_update_employe_info():
    db.create_company('Love','Lovers')
    max_id = db.last_company_id()
    db.create_employer(max_id,"Men","Girls", 9888845678)
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info('Dragon',employer_id)
    # Сравниваем информацию о сотруднике полученую через АПИ с измененной информацией в БД
    get_api_info = (api.get_info_for_employee(employer_id)).json()
    assert get_api_info['firstName'] == 'Dragon'
    assert get_api_info['lastName'] == 'Girls'
    assert get_api_info['isActive'] == True
    # Удаляем сотрудника БД
    db.delete_employer(employer_id)
    # Удаляем созданную компанию 
    db.delete(max_id)






