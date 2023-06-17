from collections import UserDict
from record import Record

class AdressBook(UserDict):
    
    #def add_record(self, name):
        
    # Create new record with name
    # Add record to self.data    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
