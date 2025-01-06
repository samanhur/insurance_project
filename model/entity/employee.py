from model.entity.person import Person


class Employee(Person):
    def __init__(self, name, family, national_code,
                 birth_date, username, password, status, role, salary):
        super().__init__(name, family, national_code, birth_date, username, password, status)

        self.role = role
        self.salary = salary
