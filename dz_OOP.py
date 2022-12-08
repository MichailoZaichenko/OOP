# Задание 1
# Реализуйте класс «Человек». Необходимо хранить в 
# полях класса: ФИО, дату рождения, контактный телефон, 
# город, страну, домашний адрес. Реализуйте методы класса 
# для ввода данных, вывода данных, реализуйте доступ к 
# отдельным полям через методы класса.

class Human:
    def __init__(self, full_name, date_of_birth, contact_phone_number, city, country, home_address):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.contact_phone_number = contact_phone_number
        self.city = city
        self.country = country
        self.home_address = home_address
    def __str__(self):
        return (f'Name: {self.full_name},\n'
                f'Date of birth: {self.date_of_birth}, \n'
                f'Contact phone number: {self.contact_phone_number} \n'
                f'City: {self.city} \n'
                f'Country: {self.country} \n'
                f'Home address: {self.home_address} \n')
me = Human("Zaichenko Misha Andriovich", "19.10.2006", "098-123-45-67", "Dnipro", "Ukraine","Bebra 87")
print(me)

# Задание 2
# Создайте класс «Город». Необходимо хранить в по-
# лях класса: название города, название региона, название 
# страны, количество жителей в городе, почтовый индекс 
# города, телефонный код города. Реализуйте методы класса 
# для ввода данных, вывода данных, реализуйте доступ к 
# отдельным полям через методы класса.


 
# Задание 3
# Создайте  класс  «Страна».  Необходимо  хранить  в  
# полях класса: название страны, название континента, 
# количество жителей в стране, телефонный код страны, 
# название столицы, название городов страны. Реализуйте
# методы класса для ввода данных, вывода данных, реа-
# лизуйте доступ к отдельным полям через методы класса.



# Задание 4
# Создайте класс «Дробь». Необходимо хранить в полях 
# класса: числитель и знаменатель. Реализуйте методы класса 
# для ввода данных, вывода данных, реализуйте доступ к 
# отдельным полям через методы класса. Также создайте 
# методы класса для выполнения арифметических опера-
# ций (сложение, вычитание, умножение, деление, и т.д.).Практическое задание
