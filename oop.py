from collections import UserDict


class Field:

    def __init__(self, value):

        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:

    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.optional_fields = []

        if phone:
            self.optional_fields.append(phone)

    def add_phone(self, phone: Phone):

        self.optional_fields.append(phone)

    def remove_phone(self, phone: Phone):
        for field in self.optional_fields:
            if not isinstance(field, Phone):
                continue
            if field.value == phone.value:
                self.optional_fields.remove(field)

    def edit_phone(self, phone: Phone, new_phone_number):
        for field in self.optional_fields:
            if not isinstance(field, Phone):
                continue
            if field.value == phone.value:
                field.value = new_phone_number


class AdressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record
