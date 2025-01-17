from controller.exceptions.my_exceptions import DuplicateUsernameError, DuplicateNationalCodeError
from model.da.sqlalchemy_da.da import DataAccess
from model.entity.customer import Customer
from model.tools.decorators import exception_handling


class CustomerController:
    da = DataAccess(Customer)

    @classmethod
    @exception_handling
    def save(cls, name, family, father_name, national_code, birth_date, phone, username, password, status=True):
        if CustomerController.find_by_username(username)[1]:
            raise DuplicateUsernameError()
        elif CustomerController.find_by_national_code(national_code)[1]:
            raise DuplicateNationalCodeError()
        else:
            customer = Customer(name, family, father_name, national_code, birth_date, phone, username, password, status)
            cls.da.save(customer)
            return True, f"Customer({customer}) saved successfully"

    @classmethod
    @exception_handling
    def edit(cls, person_id, name, family, father_name, national_code, birth_date, phone, username, password, status):
        customer = Customer(name, family, father_name, national_code, birth_date, phone, username, password, status)
        customer.person_id = person_id
        cls.da.edit(customer)
        return True, f"Customer({customer}) edited successfully"

    @classmethod
    def remove(cls, person_id):
        cls.da.remove(person_id)
        return True, f"Customer({person_id}) removed successfully"

    @classmethod
    def find_all(cls):
        return True, cls.da.find_all()

    @classmethod
    def find_by_status(cls, status):
        return cls.da.find_by(Customer.status == status)

    @classmethod
    def find_by_id(cls, person_id):
        return cls.da.find_by_id(person_id)

    @classmethod
    def find_by_username(cls, username):
        return cls.da.find_by(Customer.username == username)

    @classmethod
    def find_by_national_code(cls, national_code):
        return cls.da.find_by(Customer.national_code == national_code)

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        if cls.da.find_by(Customer.username == username) and cls.da.find_by(Customer.password == password):
            customer_data = cls.da.find_by_id(Customer.person_id)
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
