from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.customer import Customer
from model.entity.insurances import Insurances
from model.tools.validation import Validator
from model.entity.base import Base


class ActiveInsurance(Insurances, Base):
    __tablename__ = "active_insurance"
    active_insurance_id = Column(Integer, primary_key=True, autoincrement=True)
    service = Column(String(30), nullable=False)
    number_of_duration = Column(Integer, nullable=False)
    duration_period = Column(String(7), nullable=False)
    cost = Column(Integer, nullable=False)
    expire_date = Column(Date, nullable=False)

    customer_id = Column(Integer, ForeignKey("customers.person_id"))
    insurance_id = Column(Integer, ForeignKey("insurances.insurance_id"))

    customer = relationship(Customer)
    insurance = relationship(Insurances)

    def __init__(self, insurance_id, service, number_of_duration, duration_period, cost, customer_id):
        super().__init__(service, number_of_duration, duration_period, cost)
        self.insurance_id = insurance_id
        self.customer_id = customer_id
        self.expire_date = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        if Validator.amount_validator(customer_id):
            self._customer_id = customer_id

    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        if Validator.date_validator(expire_date):
            self._expire_date = expire_date
