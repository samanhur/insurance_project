from model.tools.validation import Validator


class Insurances:
    def __init__(self, service, number_of_duration, duration_period, cost):
        self.insurance_id = None
        self.service = service
        self.number_of_duration = number_of_duration
        self.duration_period = duration_period
        self.cost = cost

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, service):
        self._service = Validator.name_validator(service)

    @property
    def number_of_duration(self):
        return self._number_of_duration

    @number_of_duration.setter
    def number_of_duration(self, number_of_duration):
        self._number_of_duration = Validator.amount_validator(number_of_duration)

    @property
    def duration_period(self):
        return self._duration_period

    @duration_period.setter
    def duration_period(self, duration_period):
        self._duration_period = Validator.time_duration_validator(duration_period)

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = Validator.amount_validator(cost)
