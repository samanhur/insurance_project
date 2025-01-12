from model.entity.customer import Customer
from model.entity.insurances import Insurances


class ActiveInsurance(Customer, Insurances):
    pass
