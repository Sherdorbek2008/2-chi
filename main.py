# 1
# class Phone:
#     def __init__(self, brand, model, battery_capacity, color, storage):
#         self.__brand = brand
#         self.__model = model
#         self.__battery_capacity = battery_capacity
#         self.__color = color
#         self.__storage = storage
#
#     @property
#     def brand(self):
#         return self.__brand
#
#     @brand.setter
#     def brand(self, brand):
#         self.__brand = brand
#         return self.__brand
#
#     @brand.deleter
#     def brand(self):
#         del self.__brand
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         self.__model = model
#         return self.__model
#
#     @model.deleter
#     def model(self):
#         del self.__model
#
#     @property
#     def battery_capacity(self):
#         return self.__battery_capacity
#
#     @battery_capacity.setter
#     def battery_capacity(self, battery_capacity):
#         self.__battery_capacity = battery_capacity
#         return self.__battery_capacity
#
#     @battery_capacity.deleter
#     def battery_capacity(self):
#         del self.__battery_capacity
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, color):
#         self.__color = color
#         return self.__color
#
#     @color.deleter
#     def color(self):
#         del self.__color
#
#     @property
#     def storage(self):
#         return self.__storage
#
#     @storage.setter
#     def storage(self, storage):
#         self.__storage = storage
#         return self.__storage
#
#     @storage.deleter
#     def storage(self):
#         del self.__storage
#
# def Make_call(phnumber):
#
#         return f"{phnumber} ga qongiroq amalga oshirildi"
#
# def charge(n):
#         return f"telefoninngiz zaryadlanmoqda"
#
# def get_storge(self):
#         return f"Telefon xotirasi.\n>>> {self.__storage}"
# print("commands add telefon qoshish\n call qongiroq qilish\n charge zaryadlash\n get storge xotirani korish\nstop chiqish")
# while True:
#
#     comand=input("Buyruqni kiriting:")
#     if comand == 'add':
#             brand = input("brand: ")
#             model = input("modeli: ")
#             while True:
#                 batery = input('batareya quvattini kiriting: ')
#                 if  batery.isdigit():
#                     break
#                 else:
#                     print('batreya faqathariflardan iborat boladi')
#
#             while True:
#                 colour = input('rangini kiriting: ')
#                 if colour.isalpha():
#                     break
#                 else:
#                     print('rang faqat hariflardan iborat bolishi kerak!!!!')
#
#             while True:
#                 storge = input('xotirasini kiriting: ')
#                 if storge.isnumeric():
#                     break
#                 else:
#                     print('xotira faqat raqamlardan iborat bolishi kerak!!!!')
#
#             phone=Phone(brand,model,batery,colour,storge)
#
#     elif comand == 'call':
#         while True:
#             phone = input('telefon raqamingizni kiriting: ')
#             if phone.startswith("+998") and phone[1:].isdigit() and len(phone) == 13:
#                 print(Make_call(phone))
#                 break
#             else:
#                 print('telefon raqam faqat +998 dan boshlanishi va + dan so\'ng barcha raqamlar bo\'lishi kerak')
#     elif comand=="charge":
#         print(charge(100))
#     elif comand=="get storge":
#         print(get_storge)
#
#     elif comand == 'stop':
#         break
#
#     else:
#         print("Noma'lum buyruq, iltimos qayta urinib ko'ring.")
# ----------------------------------------------------------------------------------------------------------
# 2
# class Computer:
#     def __init__(self, brand, processor, ram, storage, graphics_card):
#         self.__brand = brand
#         self.__processor = processor
#         self.__ram = ram
#         self.__storage = storage
#         self.__graphics_card = graphics_card
#
#     @property
#     def brand(self):
#         return self.__brand
#
#     @brand.setter
#     def brand(self, brand):
#         self.__brand = brand
#
#     @brand.deleter
#     def brand(self):
#         del self.__brand
#
#     @property
#     def processor(self):
#         return self.__processor
#
#     @processor.setter
#     def processor(self, processor):
#         self.__processor = processor
#
#     @processor.deleter
#     def processor(self):
#         del self.__processor
#
#     @property
#     def ram(self):
#         return self.__ram
#
#     @ram.setter
#     def ram(self, value):
#         if value < 0:
#             raise ValueError("Tezkor xotira manfiy bo'lishi mumkin emas.")
#         self.__ram = value
#
#     @ram.deleter
#     def ram(self):
#         del self.__ram
#
#     @property
#     def storage(self):
#         return self.__storage
#
#     @storage.setter
#     def storage(self, storage):
#         self.__storage = storage
#
#     @storage.deleter
#     def storage(self):
#         del self.__storage
#
#     @property
#     def graphics_card(self):
#         return self.__graphics_card
#
#     @graphics_card.setter
#     def graphics_card(self, graphics_card):
#         self.__graphics_card = graphics_card
#
#     @graphics_card.deleter
#     def graphics_card(self):
#         del self.__graphics_card
#
#     def upgrade_ram(self, additional_ram):
#         self.ram += additional_ram
#         print(f"Tezkor xotira yangilandi: {self.ram} GB ga oshdi.")
#
#     def install_program(self, program_name):
#         print(f"{program_name} dasturi o'rnatildi.")
#
#     def get_specs(self):
#         specs = {
#             'Brend': self.brand,
#             'Protsessor': self.processor,
#             'Tezkor xotira': self.ram,
#             'Doimiy xotira': self.storage,
#             'Grafika kartasi': self.graphics_card
#         }
#         return specs
#
#
#
# print("buyruqlar: add (kompyuter qo'shish), upgrade (xotirani oshirish), install (dastur o'rnatish), specs (xususiyatlar), stop (to'xtatish)")
# computer = None
#
# while True:
#     command = input("Buyruqni kiriting: ")
#
#     if command == 'add':
#         brand = input("Brend: ")
#         processor = input("Protsessor: ")
#
#         while True:
#             try:
#                 ram = int(input("Tezkor xotira (GB): "))
#                 if ram < 0:
#                     raise ValueError
#                 break
#             except ValueError:
#                 print("Iltimos, to'g'ri raqam kiriting.")
#
#         storage = input("Doimiy xotira: ")
#         graphics_card = input("Grafika kartasi: ")
#
#         computer = Computer(brand, processor, ram, storage, graphics_card)
#         print("Kompyuter muvaffaqiyatli qo'shildi.")
#
#     elif command == 'upgrade':
#         if computer:
#             additional_ram = int(input("Qo'shimcha tezkor xotira (GB): "))
#             computer.upgrade_ram(additional_ram)
#         else:
#             print("Avval kompyuter qo'shish kerak.")
#
#     elif command == 'install':
#         if computer:
#             program_name = input("O'rnatiladigan dastur nomi: ")
#             computer.install_program(program_name)
#         else:
#             print("Avval kompyuter qo'shish kerak.")
#
#     elif command == 'specs':
#         if computer:
#             specs = computer.get_specs()
#             for key, value in specs.items():
#                 print(f"{key}: {value}")
#         else:
#             print("Avval kompyuter qo'shish kerak.")
#
#     elif command == 'stop':
#         print("Dastur to'xtatildi.")
#         break
#
#     else:
#         print("Noma'lum buyruq, iltimos qayta urinib ko'ring.")
# --------------------------------------------------------------------------------------------
# 3
# class Book:
#     def __init__(self, title, author, genre, pages, price):
#         self.__title = title
#         self.__author = author
#         self.__genre = genre
#         self.__pages = pages
#         self.__price = price
#
#     @property
#     def title(self):
#         return self.__title
#
#     @title.setter
#     def title(self, title):
#         self.__title = title
#
#     @title.deleter
#     def title(self):
#         del self.__title
#
#     @property
#     def author(self):
#         return self.__author
#
#     @property
#     def genre(self):
#         return self.__genre
#
#     @property
#     def pages(self):
#         return self.__pages
#
#     @property
#     def price(self):
#         return self.__price
#
#     def get_title(self):
#         return self.__title
#
#     def read(self):
#         print(f"{self.__title} kitobini o'qiyotganingizni tasavvur qiling...")
#
#     def get_price(self):
#         return self.__price
#
#
#
# print("buyruqlar: add (kitob qo'shish), read (kitobni o'qish), price (narxni ko'rsatish), stop (to'xtatish)")
# book = None
#
# while True:
#     command = input("Buyruqni kiriting: ")
#
#     if command == 'add':
#         title = input("Kitob nomi: ")
#         author = input("Muallif: ")
#         genre = input("Janr: ")
#
#         while True:
#             try:
#                 pages = int(input("Sahifalar soni: "))
#                 if pages < 0:
#                     raise ValueError
#                 break
#             except ValueError:
#                 print("Iltimos, to'g'ri raqam kiriting.")
#
#         while True:
#             try:
#                 price = float(input("Narx: "))
#                 if price < 0:
#                     raise ValueError
#                 break
#             except ValueError:
#                 print("Iltimos, to'g'ri narx kiriting.")
#
#         book = Book(title, author, genre, pages, price)
#         print("Kitob muvaffaqiyatli qo'shildi.")
#
#     elif command == 'read':
#         if book:
#             book.read()
#         else:
#             print("Avval kitob qo'shish kerak.")
#
#     elif command == 'price':
#         if book:
#             print(f"{book.get_title()} narxi: {book.get_price()} so'm")
#         else:
#             print("Avval kitob qo'shish kerak.")
#
#     elif command == 'stop':
#         print("Dastur to'xtatildi.")
#         break
#
#     else:
#         print("Noma'lum buyruq, iltimos qayta urinib ko'ring.")
# --------------------------------------------------------------------------------------------
# 4
# class Restaurant:
#     def __init__(self, name, cuisine_type, address, rating, capacity):
#         self.__name = name
#         self.__cuisine_type = cuisine_type
#         self.__address = address
#         self.__rating = rating
#         self.__capacity = capacity
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def cuisine_type(self):
#         return self.__cuisine_type
#
#     @cuisine_type.setter
#     def cuisine_type(self, cuisine_type):
#         self.__cuisine_type = cuisine_type
#
#     @cuisine_type.deleter
#     def cuisine_type(self):
#         del self.__cuisine_type
#
#     @property
#     def address(self):
#         return self.__address
#
#     @address.setter
#     def address(self, address):
#         self.__address = address
#
#     @address.deleter
#     def address(self):
#         del self.__address
#
#     @property
#     def rating(self):
#         return self.__rating
#
#     @rating.setter
#     def rating(self, rating):
#         if 1 <= rating <= 5:
#             self.__rating = rating
#         else:
#             raise ValueError("Reyting 1 dan 5 gacha bo'lishi kerak.")
#
#     @rating.deleter
#     def rating(self):
#         del self.__rating
#
#     @property
#     def capacity(self):
#         return self.__capacity
#
#     @capacity.setter
#     def capacity(self, capacity):
#         if capacity > 0:
#             self.__capacity = capacity
#         else:
#             raise ValueError("Sig'im musbat raqam bo'lishi kerak.")
#
#     @capacity.deleter
#     def capacity(self):
#         del self.__capacity
#
#     def serve(self):
#         print(f"{self.__name} restoranida xizmat ko'rsatilmoqda!")
#
#     def get_rating(self):
#         return self.__rating
#
#     def book_table(self, number_of_people):
#         if number_of_people > self.__capacity:
#             print(f"Xafsizlik sababli, {self.__name} restoranida {self.__capacity} dan ortiq odamni joylay olmaymiz.")
#         else:
#             print(f"{self.__name} restoranida {number_of_people} kishilik stol buyurtma qilindi.")
#
#
#
# print("buyruqlar: add (restoran qo'shish), serve (xizmat ko'rsatish), rating (reytingni ko'rsatish), book (stol buyurtma qilish), stop (to'xtatish)")
# restaurant = None
#
# while True:
#     command = input("Buyruqni kiriting: ")
#
#     if command == 'add':
#         name = input("Restoran nomi: ")
#         cuisine_type = input("Oshxona turi: ")
#         address = input("Manzil: ")
#
#         while True:
#             try:
#                 rating = float(input("Reyting (1 dan 5 gacha): "))
#                 if rating < 1 or rating > 5:
#                     raise ValueError
#                 break
#             except ValueError:
#                 print("Iltimos, 1 dan 5 gacha bo'lgan raqam kiriting.")
#
#         while True:
#             try:
#                 capacity = int(input("Sig'im: "))
#                 if capacity < 1:
#                     raise ValueError
#                 break
#             except ValueError:
#                 print("Iltimos, to'g'ri sig'im kiriting.")
#
#         restaurant = Restaurant(name, cuisine_type, address, rating, capacity)
#         print("Restoran muvaffaqiyatli qo'shildi.")
#
#     elif command == 'serve':
#         if restaurant:
#             restaurant.serve()
#         else:
#             print("Avval restoran qo'shish kerak.")
#
#     elif command == 'rating':
#         if restaurant:
#             print(f"{restaurant.name} reytingi: {restaurant.get_rating()}")
#         else:
#             print("Avval restoran qo'shish kerak.")
#
#     elif command == 'book':
#         if restaurant:
#             try:
#                 number_of_people = int(input("Nechta odam uchun stol buyurtma qilmoqchisiz? "))
#                 restaurant.book_table(number_of_people)
#             except ValueError:
#                 print("Iltimos, to'g'ri raqam kiriting.")
#         else:
#             print("Avval restoran qo'shish kerak.")
#
#     elif command == 'stop':
#         print("Dastur to'xtatildi.")
#         break
#
#     else:
#         print("Noma'lum buyruq, iltimos qayta urinib ko'ring.")
# --------------------------------------------------------------------------------------------
# 5
# class Zoo:
#     def __init__(self, name, location, animal_count, ticket_price, opening_hours):
#         self.__name = name
#         self.__location = location
#         self.__animal_count = animal_count
#         self.__ticket_price = ticket_price
#         self.__opening_hours = opening_hours
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def location(self):
#         return self.__location
#
#     @location.setter
#     def location(self, location):
#         self.__location = location
#
#     @location.deleter
#     def location(self):
#         del self.__location
#
#     @property
#     def animal_count(self):
#         return self.__animal_count
#
#     @animal_count.setter
#     def animal_count(self, animal_count):
#         if animal_count >= 0:
#             self.__animal_count = animal_count
#         else:
#             raise ValueError("Hayvonlar soni musbat raqam bo'lishi kerak.")
#
#     @animal_count.deleter
#     def animal_count(self):
#         del self.__animal_count
#
#     @property
#     def ticket_price(self):
#         return self.__ticket_price
#
#     @ticket_price.setter
#     def ticket_price(self, ticket_price):
#         if ticket_price >= 0:
#             self.__ticket_price = ticket_price
#         else:
#             raise ValueError("Chiptaning narxi musbat bo'lishi kerak.")
#
#     @ticket_price.deleter
#     def ticket_price(self):
#         del self.__ticket_price
#
#     @property
#     def opening_hours(self):
#         return self.__opening_hours
#
#     @opening_hours.setter
#     def opening_hours(self, opening_hours):
#         self.__opening_hours = opening_hours
#
#     @opening_hours.deleter
#     def opening_hours(self):
#         del self.__opening_hours
#
#     def add_animal(self):
#         self.__animal_count += 1
#         print(f"Hayvon qo'shildi. Hozirgi hayvonlar soni: {self.__animal_count}")
#
#     def remove_animal(self):
#         if self.__animal_count > 0:
#             self.__animal_count -= 1
#             print(f"Hayvon olib tashlandi. Hozirgi hayvonlar soni: {self.__animal_count}")
#         else:
#             print("Olib tashlash uchun hayvon yo'q.")
#
#     def get_animal_count(self):
#         return self.__animal_count
#
#
#
# print("buyruqlar: create (hayvonot bog'ini yaratish), add (hayvon qo'shish), remove (hayvonni olib tashlash), count (hayvonlar sonini ko'rsatish), stop (to'xtatish)")
# zoo = None
#
# while True:
#     command = input("Buyruqni kiriting: ")
#
#     if command == 'create':
#         name = input("Hayvonot bog'ining nomi: ")
#         location = input("Joylashuvi: ")
#
#         while True:
#             try:
#                 animal_count = int(input("Boshlang'ich hayvonlar soni: "))
#                 if animal_count < 0:
#                     raise ValueError
#                 break
#             except ValueError:
#                 print("Iltimos, to'g'ri raqam kiriting.")
#
#         while True:
#             try:
#                 ticket_price = float(input("Chiptaning narxi: "))
#                 if ticket_price < 0:
#                     raise ValueError
#                 break
#             except ValueError:
#                 print("Iltimos, to'g'ri narx kiriting.")
#
#         opening_hours = input("Ochilish vaqti: ")
#
#         zoo = Zoo(name, location, animal_count, ticket_price, opening_hours)
#         print("Hayvonot bog'i muvaffaqiyatli qo'shildi.")
#
#     elif command == 'add':
#         if zoo:
#             zoo.add_animal()
#         else:
#             print("Avval hayvonot bog'ini qo'shish kerak.")
#
#     elif command == 'remove':
#         if zoo:
#             zoo.remove_animal()
#         else:
#             print("Avval hayvonot bog'ini qo'shish kerak.")
#
#     elif command == 'count':
#         if zoo:
#             print(f"Hozirgi hayvonlar soni: {zoo.get_animal_count()}")
#         else:
#             print("Avval hayvonot bog'ini qo'shish kerak.")
#
#     elif command == 'stop':
#         print("Dastur to'xtatildi.")
#         break
#
#     else:
#         print("Noma'lum buyruq, iltimos qayta urinib ko'ring.")
# --------------------------------------------------------------------------------------------
# 6
# class StudentGroup:
#     def __init__(self, group_name, department, total_students, group_leader, semester):
#         self.__group_name = group_name
#         self.__department = department
#         self.__total_students = total_students
#         self.__group_leader = group_leader
#         self.__semester = semester
#
#     @property
#     def group_name(self):
#         return self.__group_name
#
#     @group_name.setter
#     def group_name(self, group_name):
#         self.__group_name = group_name
#
#     @group_name.deleter
#     def group_name(self):
#         del self.__group_name
#
#     @property
#     def department(self):
#         return self.__department
#
#     @department.setter
#     def department(self, department):
#         self.__department = department
#
#     @department.deleter
#     def department(self):
#         del self.__department
#
#     @property
#     def total_students(self):
#         return self.__total_students
#
#     @total_students.setter
#     def total_students(self, total_students):
#         if total_students >= 0:
#             self.__total_students = total_students
#         else:
#             raise ValueError("Talabalar soni musbat raqam bo'lishi kerak.")
#
#     @total_students.deleter
#     def total_students(self):
#         del self.__total_students
#
#     @property
#     def group_leader(self):
#         return self.__group_leader
#
#     @group_leader.setter
#     def group_leader(self, group_leader):
#         self.__group_leader = group_leader
#
#     @group_leader.deleter
#     def group_leader(self):
#         del self.__group_leader
#
#     @property
#     def semester(self):
#         return self.__semester
#
#     @semester.setter
#     def semester(self, semester):
#         self.__semester = semester
#
#     @semester.deleter
#     def semester(self):
#         del self.__semester
#
#     def add_student(self):
#         self.__total_students += 1
#         print(f"Talaba qo'shildi. Hozirgi talaba soni: {self.__total_students}")
#
#     def remove_student(self):
#         if self.__total_students > 0:
#             self.__total_students -= 1
#             print(f"Talaba olib tashlandi. Hozirgi talaba soni: {self.__total_students}")
#         else:
#             print("Olib tashlash uchun talabalar yo'q.")
#
#     def get_leader(self):
#         return self.__group_leader
#
# print("buyruqlar: create (guruhni yaratish), add (talaba qo'shish), remove (talaba olib tashlash), leader (guruh yetakchisini ko'rsatish), stop (to'xtatish)")
# group = None
#
# while True:
#     command = input("Buyruqni kiriting: ")
#
#     if command == 'create':
#         group_name = input("Guruh nomi: ")
#         department = input("Bo'lim: ")
#
#         while True:
#             try:
#                 total_students = int(input("Boshlang'ich talabalar soni: "))
#                 if total_students < 0:
#                     raise ValueError
#                 break
#             except ValueError:
#                 print("Iltimos, to'g'ri raqam kiriting.")
#
#         group_leader = input("Guruh yetakchisi: ")
#         semester = input("Semestr: ")
#
#         group = StudentGroup(group_name, department, total_students, group_leader, semester)
#         print("Guruh muvaffaqiyatli qo'shildi.")
#
#     elif command == 'add':
#         if group:
#             group.add_student()
#         else:
#             print("Avval guruhni qo'shish kerak.")
#
#     elif command == 'remove':
#         if group:
#             group.remove_student()
#         else:
#             print("Avval guruhni qo'shish kerak.")
#
#     elif command == 'leader':
#         if group:
#             print(f"Guruh yetakchisi: {group.get_leader()}")
#         else:
#             print("Avval guruhni qo'shish kerak.")
#
#     elif command == 'stop':
#         print("Dastur to'xtatildi.")
#         break
#
#     else:
#         print("Noma'lum buyruq, iltimos qayta urinib ko'ring.")
