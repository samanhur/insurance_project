from model.da.da import Da


class CustomerDa(Da):

    def save(self, customer):
        self.connect()
        self.cursor.execute(
            "INSERT INTO CUSTOMERS (name, family, father_name, national_code, birth_date, phone, username, password, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [customer.name, customer.family, customer.father_name, customer.national_code, customer.birth_date,
             customer.phone, customer.username,
             customer.password, customer.status]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, customer):
        self.connect()
        self.cursor.execute(
            "UPDATE CUSTOMERS SET PHONE=%s, PASSWORD=%s, STATUS=%s  WHERE PERSON_ID=%s",
            [customer.phone, customer.password, customer.status, customer.person_id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, person_id):
        self.connect()
        self.cursor.execute(
            "DELETE FROM CUSTOMERS WHERE PERSON_ID=%s",
            [person_id]
        )
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM CUSTOMERS")
        customers_list = self.cursor.fetchall()
        self.disconnect()
        return customers_list

    def find_by_status(self, status):
        self.connect()
        self.cursor.execute("SELECT * FROM CUSTOMERS WHERE STATUS=%s", [status])
        customers_list = self.cursor.fetchall()
        self.disconnect()
        return customers_list

    def find_by_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM CUSTOMERS WHERE PERSON_ID=%s", [person_id])
        customer = self.cursor.fetchone()
        self.disconnect()
        return customer

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("SELECT * FROM CUSTOMERS WHERE USERNAME=%s", [username])
        customer = self.cursor.fetchone()
        self.disconnect()
        return customer

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("SELECT * FROM CUSTOMERS WHERE USERNAME=%s AND PASSWORD=%s", [username, password])
        customer = self.cursor.fetchone()
        self.disconnect()
        return customer

    def find_by_national_code(self, national_code):
        self.connect()
        self.cursor.execute("SELECT * FROM CUSTOMERS WHERE NATIONAL_CODE=%s", [national_code])
        customer = self.cursor.fetchone()
        self.disconnect()
        return customer
