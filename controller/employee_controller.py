from model.da.employee_da import EmployeeDa
from model.entity.employee import Employee


class EmployeeController:

    @classmethod
    def save(cls, name, family, national_code, birth_date, username, password, status, role, salary):
        employee = Employee(name, family, national_code, birth_date, username, password, status, role, salary)
        EmployeeDa.save(employee)
        return True, f"Employee({employee}) saved successfully"

    @classmethod
    def edit(cls, person_id, name, family, national_code, birth_date, username, password, status, role, salary):
        employee = Employee(name, family, national_code, birth_date, username, password, status, role, salary)
        employee.person_id = person_id
        EmployeeDa.edit(employee)
        return True, f"Employee({employee}) edited successfully"

    @classmethod
    def remove(cls, person_id):
        EmployeeDa.remove(person_id)
        return True, f"Employee({person_id}) removed successfully"

    @classmethod
    def find_all(cls):
        return True, EmployeeDa.find_all()

    @classmethod
    def find_by_id(cls, person_id):
        return True, EmployeeDa.find_by_id(person_id)

    @classmethod
    def find_by_username(cls, username):
        return True, EmployeeDa.find_by_username(username)
