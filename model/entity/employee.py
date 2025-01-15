from sqlalchemy import Column, Integer, String, Date, Boolean

from model.entity.person import Person
from model.tools.validation import Validator
from model.entity.base import Base


class Employee(Person, Base):
    __tablename__ = "employees"
    person_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    national_code = Column(String(10), unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(30), nullable=False)
    status = Column(Boolean, default=True)
    role = Column(String(20))
    salary = Column(Integer)

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
