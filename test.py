from oop import Record
from oop import Name
from oop import AdressBook
from oop import Phone


adress_book = AdressBook()
name = Name("Dima")
phone = Phone("+1234")
record = Record(name)
record.add_phone(Phone("+380934123"))

adress_book.add_record(record)
# print(adress_book)
print(adress_book.data)
print(record.optional_fields)
for name, record in adress_book.data.items():
    print(f"{name}: {[r.value for r in record.optional_fields]}")
