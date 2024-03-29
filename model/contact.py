from model.phone_number import PhoneNumber

class Contact:
    id_count = 1

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.numbers = []
        self.id = Contact.id_count
        Contact.id_count += 1

    def add_new_number(self, phone_number, phone_type):
        phone_number = PhoneNumber(phone_number, phone_type)
        self.numbers.append(phone_number)

    def __str__(self):
        str_rep = f'\tID: {self.id}\n\tname: {self.name}\n\tsurname: {self.surname}'
        for number in self.numbers:
            str_rep += f'\t\t\n{number}'
        return str_rep

