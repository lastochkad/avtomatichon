from Lesson_3.lesson_3_task_3.adress import Adress
from Lesson_3.lesson_3_task_3.mailing import Mailing

to_adress = Adress("74900", "Pyatigorsk", "Teplosernaya", "29","22")
from_adress = Adress("86888","Moscow", "Kutuzova", "33", "102")
mailing = Mailing(to_adress, from_adress, 2000, "BW10303")

print(f"Отправление {mailing.track} из {mailing.from_adress.index}, {mailing.from_adress.city},"
      f"{mailing.from_adress.street}, {mailing.from_adress.house} - {mailing.from_adress.apartment} "
      f"в {mailing.to_adress.index}, {mailing.to_adress.city}, {mailing.to_adress.street},"
      f"{mailing.to_adress.house} - {mailing.to_adress.apartment}. Стоимость {mailing.cost} рублей.")