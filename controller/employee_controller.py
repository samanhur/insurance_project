from controller.exceptions.my_exceptions import DuplicateUsernameError, DuplicateNationalCodeError
from model.da.employee_da import EmployeeDa
from model.entity.employee import Employee


class EmployeeController:
    employee_da = EmployeeDa()

    @classmethod
    def save(cls, name, family, national_code, birth_date, username, password, status, role, salary):
        if EmployeeController.find_by_username(username)[0]:
            raise DuplicateUsernameError()
        elif EmployeeController.find_by_national_code(national_code)[0]:
            raise DuplicateNationalCodeError()
        employee = Employee(name, family, national_code, birth_date, username, password, status, role, salary)
        cls.employee_da.save(employee)
        return True, f"Employee({employee}) saved successfully"

    @classmethod
    def edit(cls, person_id, name, family, national_code, birth_date, username, password, status, role, salary):
        employee = Employee(name, family, national_code, birth_date, username, password, status, role, salary)
        employee.person_id = person_id
        cls.employee_da.edit(employee)
        return True, f"Employee({employee}) edited successfully"

    @classmethod
    def remove(cls, person_id):
        cls.employee_da.remove(person_id)
        return True, f"Employee({person_id}) removed successfully"

    @classmethod
    def find_all(cls):
        return True, cls.employee_da.find_all()

    @classmethod
    def find_by_id(cls, person_id):
        return True, cls.employee_da.find_by_id(person_id)

    @classmethod
    def find_by_username(cls, username):
        return True, cls.employee_da.find_by_username(username)

    @classmethod
    def find_by_national_code(cls, national_code):
        return True, cls.employee_da.find_by_national_code(national_code)

    @classmethod
    def find_by_username_and_password(cls, username, password):
        if cls.employee_da.find_by_username_and_password(username, password):
            return True
