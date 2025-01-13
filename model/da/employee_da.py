from model.da.da import Da


class EmployeeDa(Da):

    def save(self, employee):
        self.connect()
        self.cursor.execute(
            "INSERT INTO EMPLOYEES (name, family, national_code, birth_date, username, password, status, role, salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [employee.name, employee.family, employee.national_code, employee.birth_date, employee.username,
             employee.password, employee.status, employee.role, employee.salary]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, employee):
        self.connect()
        self.cursor.execute(
            "UPDATE EMPLOYEES SET NAME=%s, FAMILY=%s, PASSWORD=%s, STATUS=%s, ROLE=%s, SALARY=%s  WHERE PERSON_ID=%s",
            [employee.name, employee.family, employee.password, employee.status, employee.role, employee.salary,
             employee.person_id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, person_id):
        self.connect()
        self.cursor.execute(
            "DELETE FROM EMPLOYEES WHERE PERSON_ID=%s",
            [person_id]
        )
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM EMPLOYEES")
        employees_list = self.cursor.fetchall()
        self.disconnect()
        return employees_list

    def find_by_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM EMPLOYEES WHERE PERSON_ID=%s", [person_id])
        employee = self.cursor.fetchone()
        self.disconnect()
        return employee

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("SELECT * FROM EMPLOYEES WHERE USERNAME=%s", [username])
        employees_list = self.cursor.fetchall()
        self.disconnect()
        return employees_list

    def find_by_national_code(self, national_code):
        self.connect()
        self.cursor.execute("SELECT * FROM EMPLOYEES WHERE NATIONAL_CODE=%s", [national_code])
        employee = self.cursor.fetchone()
        self.disconnect()
        return employee

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("SELECT * FROM EMPLOYEES WHERE USERNAME=%s AND PASSWORD=%s", [username, password])
        employee = self.cursor.fetchone()
        self.disconnect()
        return employee
