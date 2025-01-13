from model.da.customer_da import CustomerDa
from model.entity.customer import Customer
from model.tools.decorators import exception_handling
from controller.exceptions.my_exceptions import DuplicateUsernameError, DuplicateNationalCodeError


class CustomerController:

    @classmethod
    @exception_handling
    def save(cls, name, family, father_name, national_code, birth_date, phone, username, password, status=True):
        if CustomerController.find_by_username(username)[1]:
            raise DuplicateUsernameError()
        elif CustomerController.find_by_national_code(national_code)[1]:
            raise DuplicateNationalCodeError()
        else:
            customer = Customer(name, family, father_name, national_code, birth_date, phone, username, password, status)
            CustomerDa.save(customer)
            return True, f"Customer({customer}) saved successfully"

    @classmethod
    @exception_handling
    def edit(cls, person_id, name, family, father_name, national_code, birth_date, phone, username, password, status):
        customer = Customer(name, family, father_name, national_code, birth_date, phone, username, password, status)
        customer.person_id = person_id
        CustomerDa.edit(customer)
        return True, f"Customer({customer}) edited successfully"

    @classmethod
    def remove(cls, person_id):
        CustomerDa.remove(person_id)
        return True, f"Customer({person_id}) removed successfully"

    @classmethod
    def find_all(cls):
        return True, CustomerDa.find_all()

    @classmethod
    def find_by_status(cls, status):
        return True, CustomerDa.find_by_status(status)

    @classmethod
    def find_by_id(cls, person_id):
        return True, CustomerDa.find_by_id(person_id)

    @classmethod
    def find_by_username(cls, username):
        return True, CustomerDa.find_by_username(username)

    @classmethod
    def find_by_national_code(cls, national_code):
        return True, CustomerDa.find_by_national_code(national_code)

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        if CustomerDa.find_by_username_and_password(username, password):
            customer_data = CustomerDa.find_by_username_and_password(username, password)
            customer = Customer(
                customer_data[1],
                customer_data[2],
                customer_data[3],
                customer_data[4],
                customer_data[5],
                customer_data[6],
                customer_data[7],
                customer_data[8],
                customer_data[9]
            )
            customer.person_id = customer_data[0]
            return True, customer

# print(CustomerController.find_by_username_and_password("samanhovar", "saman123"))
