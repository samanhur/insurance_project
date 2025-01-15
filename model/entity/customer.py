from sqlalchemy import Column, Integer, String, Date, Boolean

from model.entity.person import Person
from model.tools.validation import Validator
from model.entity.base import Base


class Customer(Person, Base):
    __tablename__ = "customers"
    person_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    family = Column(String(30), nullable=False)
    father_name = Column(String(30), nullable=False)
    national_code = Column(String(10), unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)
    phone = Column(String(12))
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(30), nullable=False)
    status = Column(Boolean, default=True)

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
