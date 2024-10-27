from collections import UserDict


class Field():
    # Базовий клас для полів запису.

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)    



class Name(Field):
    #  Клас для зберігання імені контакту.
    pass

name1 = Name('Bob')
name2 = Name('Suizi')
print(name1)
print(name2)


class Phone(Field):
    # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value   

    @value.setter    
    def value(self, value):
        if not value.isdigit():
            raise TypeError("Phone number should contains digits only, with no other characters")
        if (len(value) != 10):
            raise ValueError("Number should be equal to 10 digits")
        self._value = value 



class Record():
    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів
    def __init__(self, name):
        self.name = Name(name)
        self.phone = []

    def add_phone(self, phone):
        pass

    def remove_phone(self, name):
        pass

    def edit_phone(self, name):
        pass

    def find_phone(self, name):
        pass


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict):
    # Клас для зберігання та управління записами.

    def __init__(self):
        pass

    def add_record():
        # self.data Реалізовано метод add_record, який додає запис до self.data.
        pass

    def find(name: str) -> Record:
        pass

    def delete(name: str):
        pass



# book = AddressBook()
# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")    

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555


# # Видалення запису Jane
# book.delete("John")








# ____________________________________________
# phone1 = Phone('0639992511')
# phone2 = Phone('0991252525')
# phone3 = Phone('099125200001212')
# phone4 = Phone('oneonetwo')
# print(phone1)
# print(phone2)
# print(phone3)
# print(phone4)
# phone2.value = '12345678900'
# print(phone2)
# phone2.value = '0639444aaa'
# print(phone2)