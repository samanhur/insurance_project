from model.entity.person import Person
from model.tools.validation import Validator


class Employee(Person):
    def __init__(self, name, family, national_code,
                 birth_date, username, password, status, role, salary):
        super().__init__(name, family, national_code, birth_date, username, password, status)

        self.role = role
        self.salary = salary

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        # TODO: I just added name validator for role but we should define some certain roles
        #  and validate role that is correct or not
        self._role = Validator.name_validator(role)

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = Validator.amount_validator(salary)
