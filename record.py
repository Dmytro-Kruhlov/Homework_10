from name import Name
from phone import Phone


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.optional_fields = []
    
    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.optional_fields.append(phone)
    
    def remove_phone(self, phone_number):
        for field in self.optional_fields:
            if not isinstance(field, Phone):
                continue
            if field.value == phone_number:
                self.optional_fields.remove(field)
                
    def edit_phone(self, phone_number, new_phone_number):
        for field in self.optional_fields:
            if not isinstance(field, Phone):
                continue
            if field.value == phone_number:
                field.value = new_phone_number
