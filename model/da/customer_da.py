from model.da.da import Da


class CustomerDa(Da):
    @classmethod
    def save(cls, customer):
        cls.connect()
        cls.cursor.execute(
            "INSERT INTO CUSTOMERS (name, family, father_name, national_code, birth_date, phone, username, password, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [customer.name, customer.family, customer.father_name, customer.national_code, customer.birth_date,
             customer.phone, customer.username,
             customer.password, customer.status]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def edit(cls, customer):
        cls.connect()
        cls.cursor.execute(
            "UPDATE CUSTOMERS SET PHONE=%s, PASSWORD=%s, STATUS=%s  WHERE PERSON_ID=%s",
            [customer.phone, customer.password, customer.status, customer.person_id]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def remove(cls, person_id):
        cls.connect()
        cls.cursor.execute(
            "DELETE FROM CUSTOMERS WHERE PERSON_ID=%s",
            [person_id]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def find_all(cls):
        cls.connect()
        cls.cursor.execute("SELECT * FROM CUSTOMERS")
        customers_list = cls.cursor.fetchall()
        cls.disconnect()
        return customers_list

    @classmethod
    def find_by_status(cls, status):
        cls.connect()
        cls.cursor.execute("SELECT * FROM CUSTOMERS WHERE STATUS=%s", [status])
        customers_list = cls.cursor.fetchall()
        cls.disconnect()
        return customers_list


    @classmethod
    def find_by_id(cls, person_id):
        cls.connect()
        cls.cursor.execute("SELECT * FROM CUSTOMERS WHERE PERSON_ID=%s", [person_id])
        customer = cls.cursor.fetchone()
        cls.disconnect()
        return customer

    @classmethod
    def find_by_username(cls, username):
        cls.connect()
        cls.cursor.execute("SELECT * FROM CUSTOMERS WHERE USERNAME=%s", [username])
        customers_list = cls.cursor.fetchall()
        cls.disconnect()
        return customers_list

    @classmethod
    def find_by_national_code(cls, national_code):
        cls.connect()
        cls.cursor.execute("SELECT * FROM CUSTOMERS WHERE NATIONAL_CODE=%s", [national_code])
        customer = cls.cursor.fetchone()
        cls.disconnect()
        return customer
