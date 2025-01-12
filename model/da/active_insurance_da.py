from model.da.da import Da


class ActiveInsuranceDa(Da):

    @classmethod
    def save(cls, active_insurance):
        cls.connect()
        cls.cursor.execute(
            "INSERT INTO ACTIVE_INSURANCE (service, number_of_duration, duration_period, cost, expire_date, status) VALUES (%s, %s, %s, %s, %s, %s)",
            [active_insurance.service, active_insurance.number_of_duration, active_insurance.duration_period,
             active_insurance.cost, active_insurance.expire_date, active_insurance.status]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def expire(cls, active_insurance_id):
        cls.connect()
        cls.cursor.execute(
            "UPDATE ACTIVE_INSURANCE SET STATUS=%s WHERE INSURANCE_ID=%s",
            [0, active_insurance_id]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def find_all(cls):
        cls.connect()
        cls.cursor.execute("SELECT * FROM ACTIVE_INSURANCE")
        active_insurances_list = cls.cursor.fetchall()
        cls.disconnect()
        return active_insurances_list

    @classmethod
    def find_by_id(cls, active_insurance_id):
        cls.connect()
        cls.cursor.execute("SELECT * FROM ACTIVE_INSURANCE WHERE INSURANCE_ID=%s", [active_insurance_id])
        active_insurance = cls.cursor.fetchone()
        cls.disconnect()
        return active_insurance

    @classmethod
    def find_by_customer_id(cls, customer_id):
        cls.connect()
        cls.cursor.execute("SELECT * FROM ACTIVE_INSURANCE WHERE CUSTOMER_ID=%s", [customer_id])
        active_insurances_list = cls.cursor.fetchall()
        cls.disconnect()
        return active_insurances_list

    @classmethod
    def find_active_insurances(cls, customer_id, status=1):
        cls.connect()
        cls.cursor.execute(
            "SELECT SERVICE, NUMBER_OF_DURATION, DURATION_PERIOD, EXPIRE_DATE FROM ACTIVE_INSURANCE WHERE CUSTOMER_ID = %s AND STATUS=%s",
            [customer_id, status])
        active_insurances_list = cls.cursor.fetchall()
        cls.disconnect()
        return active_insurances_list


