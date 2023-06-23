from oop import AdressBook, Record, Name, Phone


adress_book = AdressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Invalid command. Please try again."
        except ValueError:
            return "Error: Invalid input format. Please try again."
        except IndexError:
            return "Error: Contact not found. Please try again."
    return wrapper


def spliting(args):
    return args.split()


def hello(args):
    return "How can I help you?"


def add_record(args):

    args = spliting(args)

    if len(args) < 1 or len(args) > 2:
        raise ValueError
    name, phone = args
    if name in adress_book.data:
        return "You already have a contact with this name"
    else:
        record = Record(Name(name), Phone(phone))
        adress_book.add_record(record)
        
        return f"Contact {name} with phone number {phone} has been added."
    

def add_phone(args):

    args = spliting(args)

    if len(args) != 2:
        raise ValueError
    name, phone = args
    record = adress_book[name]
    if name in adress_book.data:
        record.add_phone(Phone(phone))

    return f"A number {phone} has been added to a contact {name}"


def change(args):

    args = spliting(args)

    if len(args) != 3:
        raise ValueError
    name, old_phone, new_phone = args
    if name not in adress_book.data:
        return f"You dont have contact with name {name}"
    record = adress_book[name]
    
    for field in record.optional_fields:
        if field.value == old_phone:
            field.value = new_phone
        
    return f"The phone number {old_phone} for contact {name} has been changed to {new_phone}."


def get_phone_number(args):

    args = spliting(args)

    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in adress_book.data:
        record = adress_book[name]
        phones = []
        for field in record.optional_fields:
            phones.append(field.value)
        return f"The phone numbers for contact {name} is {', '.join(phones)}."
    else:
        raise IndexError


def show_all_contacts(args):

    if adress_book.data:
        output = "Contacts:\n"
        for name, record in adress_book.data.items():
            fields = []
            for field in record.optional_fields:
                fields.append(field.value)
            output += f"{name}: {', '.join(fields)}\n"
        return output
    else:
        return "You don't have contacts in your phone book."


COMMANDS = {
    add_record: ["add record"],
    hello: ["hello"],
    change: ["change"],
    get_phone_number: ["phone"],
    show_all_contacts: ["show all"],
    add_phone: ["add phone"]
}


@input_error
def get_func(user_input):
    succesfull_run = False
    user_input_lower = user_input.lower()
    for func, key_words in COMMANDS.items():
        for key in key_words:
            if user_input_lower.startswith(key):
                args = user_input[len(key):].strip()
                result = func(args)
                succesfull_run = True
                break
    if not succesfull_run:
        raise KeyError
    return result


def main_loop():

    while True:

        user_input = input(">>> ")

        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        result = get_func(user_input)
        print(result)


if __name__ == "__main__":
    main_loop()
