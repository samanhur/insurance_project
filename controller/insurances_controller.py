from model.da.insurances_da import InsuranceDa
from model.entity.insurances import Insurances


class InsurancesController:

    @classmethod
    def save(cls, service, number_of_duration, duration_period, cost):
        insurance = Insurances(service, number_of_duration, duration_period, cost)
        InsuranceDa.save(insurance)
        return True, f"Insurance({insurance}) saved successfully"

    @classmethod
    def edit(cls, insurance_id, service, number_of_duration, duration_period, cost):
        insurance = Insurances(service, number_of_duration, duration_period, cost)
        insurance.insurance_id = insurance_id
        InsuranceDa.edit(insurance)
        return True, f"Insurance({insurance}) edited successfully"

    @classmethod
    def remove(cls, insurance_id):
        InsuranceDa.remove(insurance_id)
        return True, f"Insurance({insurance_id}) saved successfully"

    @classmethod
    def find_all(cls):
        return True, InsuranceDa.find_all()

    @classmethod
    def find_by_id(cls, insurance_id):
        return True, InsuranceDa.find_by_id(insurance_id)

    @classmethod
    def find_by_service(cls, service):
        return True, InsuranceDa.find_by_service(service)
