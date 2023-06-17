from adress_book import AdressBook
from record import Record


adress_book = AdressBook()
record = Record("Dima")
record.add_phone("+380934123")
adress_book.add_record(record)
print(adress_book)
print(adress_book.data)

for name, record in adress_book.data.items():
    print(f"{name}: {[r.value for r in record.optional_fields]}")