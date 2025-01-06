# da.py and insurances_da.py test passed!

# from model.entity.insurances import Insurances
# from model.da.insurances_da import InsuranceDa

# test = InsuranceDa()
# insurance = Insurances("car", 3, "month", 800)
# insurance.insurance_id = 4
# InsuranceDa.save(insurance)
# print(InsuranceDa.find_all())
# print(InsuranceDa.find_by_id(1))
# print(InsuranceDa.find_by_service("car"))
# InsuranceDa.edit(insurance)
# InsuranceDa.remove(5)
# print(insurance.__dict__)

# -------------------------------------------------------------------------------------

# employee_da.py test passed!

# from model.entity.employee import Employee
# from model.da.employee_da import EmployeeDa
# from datetime import date

# employee = Employee("saman", "ghasemi", "1234567890", date(2004, 7, 31),
#                      "samanhur", "saman123", 1, "employee", 60000)
# employee.person_id = 1

# employee2 = Employee("mohammad", "ghasemi", "1234567809", date(1990, 12, 10),
#                       "mghasemi", "101255", 1, "boss", 100000)
# employee2.person_id = 2

# EmployeeDa.save(employee)
# EmployeeDa.save(employee2)

# EmployeeDa.edit(employee2)

# EmployeeDa.remove(1)
# EmployeeDa.remove(2)

# print(EmployeeDa.find_all())
# print(EmployeeDa.find_by_id(1))
# print(EmployeeDa.find_by_username("mghasemi"))

# -----------------------------------------------------------
# admin_da.py test passed!

# from model.da.admin_da import AdminDa
# from model.entity.admin import Admin
#
# admin = Admin("saman", "ghasemi", "samanhur", "1234567890")
# admin.admin_id = 1

# AdminDa.save(admin)
# AdminDa.edit(admin)
# AdminDa.remove(1)
#
# print(AdminDa.find_all())
# print(AdminDa.find_by_id(1))
# print(AdminDa.find_by_username("samanhur"))
# print(AdminDa.find_by_username("mehdi"))
