# insurances_controller.py test passed!

# from controller.insurances_controller import InsurancesController


# InsurancesController.save("sport", 1, "year", 500)
# InsurancesController.edit(3, "car", 1, "year", 450)
# InsurancesController.remove(3)
# print(InsurancesController.find_all())
# print(InsurancesController.find_by_id(6))
# print(InsurancesController.find_by_service("car"))


# --------------------------------------------------------------------------
# employee_controller test

from controller.employee_controller import EmployeeController
from datetime import date

#
# EmployeeController.save("saman", "ghasemi", "1234567890", date(2004, 7, 31),
#                         "samanhur", "saman123", 1, "employee", 60000)
#
# EmployeeController.save("mohammad", "ghasemi", "1234567809", date(1990, 12, 10),
#                         "mghasemi", "101255", 1, "boss", 100000)

EmployeeController.remove(3)
EmployeeController.remove(4)

# print(EmployeeController.find_all())
# print(EmployeeController.find_by_id(4))
# print(EmployeeController.find_by_id(1))
# print(EmployeeController.find_by_username("samanhur"))