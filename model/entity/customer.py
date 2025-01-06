from model.entity.person import Person


class Customer(Person):
    def __init__(self, name, family, father_name, national_code,
                 birth_date, phone, username, password):
        super().__init__(name, family, national_code, birth_date, username, password)

        self.father_name = father_name
        self.phone = phone
