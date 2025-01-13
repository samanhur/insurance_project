from model.entity.insurances import Insurances
from model.tools.validation import Validator


class ActiveInsurance(Insurances):
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
