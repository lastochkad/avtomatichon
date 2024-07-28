from Lesson_3.lesson_3_task_2.smartphone import Smartphone
catalog = []
phone1 = Smartphone("Samsung","GalaxyS20","+79288119108")
phone2 = Smartphone("Apple", "iPhone 15", "+79998765432")
phone3 = Smartphone("Motorolla","E398", "+79676789923")
phone4 = Smartphone("Xiaomi", "Mi14Pro","+791999334675")
phone5 = Smartphone("Huawei", "Mate 60 Pro", "+78884561234")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.mark} {phone.model} - {phone.number}")