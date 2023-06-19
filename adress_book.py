from collections import UserDict
from record import Record

class AdressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
