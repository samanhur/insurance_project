import datetime

from model.entity.active_insurance import ActiveInsurance
from model.da.active_insurance_da import ActiveInsuranceDa
from model.tools.decorators import exception_handling
from model.tools.expire_date_calculator import expire_date_calculator


class ActiveInsuranceController:
    active_insurance_da = ActiveInsuranceDa()

    @classmethod
    @exception_handling
    def save(cls, insurance_id, service, number_of_duration, duration_period, cost, customer_id):
        active_insurance = ActiveInsurance(insurance_id, service, number_of_duration, duration_period, cost, customer_id)
        active_insurance.expire_date = expire_date_calculator(number_of_duration, duration_period)
        cls.active_insurance_da.save(active_insurance)
        return True

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.active_insurance_da.find_all()

    @classmethod
    @exception_handling
    def find_by_insurance_id(cls, insurance_id):
        return True, cls.active_insurance_da.find_by_id(insurance_id)

    @classmethod
    @exception_handling
    def find_by_active_insurance_id(cls, active_insurance_id):
        return True, cls.active_insurance_da.find_by_id(active_insurance_id)

    @classmethod
    @exception_handling
    def find_by_customer_id(cls, customer_id):
        return True, cls.active_insurance_da.find_by_customer_id(customer_id)

    @classmethod
    @exception_handling
    def find_by_expire_date(cls, customer_id):
        active_insurances_list = []
        # print(cls.active_insurance_da.find_by_customer_id(customer_id))
        for active_insurance in cls.active_insurance_da.find_by_customer_id(customer_id):
            if not active_insurance[5] < datetime.date.today():
                active_insurances_list.append(tuple(active_insurance))
        return True, active_insurances_list
