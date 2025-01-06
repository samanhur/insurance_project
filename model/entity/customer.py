from model.entity.person import Person


class Customer(Person):
    def __init__(self, name, family, father_name, national_code,
                 birth_date, phone, username, password, status):
        super().__init__(name, family, national_code, birth_date, username, password, status)

        self.father_name = father_name
        self.phone = phone
