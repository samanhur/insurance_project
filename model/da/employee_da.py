from model.da.da import Da


class EmployeeDa(Da):
    @classmethod
    def save(cls, employee):
        cls.connect()
        cls.cursor.execute(
            "INSERT INTO EMPLOYEES (name, family, national_code, birth_date, username, password, status, role, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [employee.name, employee.family, employee.national_code, employee.birth_date, employee.username,
             employee.password, employee.status, employee.role, employee.salary]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def edit(cls, employee):
        cls.connect()
        cls.cursor.execute(
            "UPDATE EMPLOYEES SET NAME=%s, FAMILY=%s, PASSWORD=%s, STATUS=%s, ROLE=%s, SALARY=%s  WHERE PERSON_ID=%s",
            [employee.name, employee.family, employee.password, employee.status, employee.role, employee.salary,
             employee.person_id]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def remove(cls, person_id):
        cls.connect()
        cls.cursor.execute(
            "DELETE FROM EMPLOYEES WHERE PERSON_ID=%s",
            [person_id]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def find_all(cls):
        cls.connect()
        cls.cursor.execute("SELECT * FROM EMPLOYEES")
        employees_list = cls.cursor.fetchall()
        cls.disconnect()
        return employees_list

    @classmethod
    def find_by_id(cls, person_id):
        cls.connect()
        cls.cursor.execute("SELECT * FROM EMPLOYEES WHERE PERSON_ID=%s", [person_id])
        employee = cls.cursor.fetchone()
        cls.disconnect()
        return employee

    @classmethod
    def find_by_username(cls, username):
        cls.connect()
        cls.cursor.execute("SELECT * FROM EMPLOYEES WHERE USERNAME=%s", [username])
        employees_list = cls.cursor.fetchall()
        cls.disconnect()
        return employees_list

    @classmethod
    def find_by_national_code(cls, national_code):
        cls.connect()
        cls.cursor.execute("SELECT * FROM EMPLOYEES WHERE NATIONAL_CODE=%s", [national_code])
        employee = cls.cursor.fetchone()
        cls.disconnect()
        return employee
