from model.entity.person import Person
from model.tools.validation import Validator


class Customer(Person):
    def __init__(self, name, family, father_name, national_code,
                 birth_date, phone, username, password, status):
        super().__init__(name, family, national_code, birth_date, username, password, status)

        self.father_name = father_name
        self.phone = phone

    @property
    def father_name(self):
        return self._father_name

    @father_name.setter
    def father_name(self, father_name):
        self._father_name = Validator.name_validator(father_name)

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = Validator.phone_validator(phone)
