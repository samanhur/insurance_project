from model.da.da import Da


class ActiveInsuranceDa(Da):

    def save(self, active_insurance):
        self.connect()
        self.cursor.execute(
            "INSERT INTO ACTIVE_INSURANCE (insurance_id, service, number_of_duration, duration_period, cost, expire_date, customer_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            [active_insurance.insurance_id, active_insurance.service, active_insurance.number_of_duration,
             active_insurance.duration_period,
             active_insurance.cost, active_insurance.expire_date, active_insurance.customer_id]
        )
        self.connection.commit()
        self.disconnect()

    # def expire(self, active_insurance_id):
    #     self.connect()
    #     self.cursor.execute(
    #         "UPDATE ACTIVE_INSURANCE SET STATUS=%s WHERE INSURANCE_ID=%s",
    #         [0, active_insurance_id]
    #     )
    #     self.connection.commit()
    #     self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM ACTIVE_INSURANCE")
        active_insurances_list = self.cursor.fetchall()
        self.disconnect()
        return active_insurances_list

    def find_by_insurance_id(self, insurance_id):
        self.connect()
        self.cursor.execute("SELECT * FROM ACTIVE_INSURANCE WHERE INSURANCE_ID=%s", [insurance_id])
        active_insurance = self.cursor.fetchone()
        self.disconnect()
        return active_insurance

    def find_by_active_insurance_id(self, active_insurance_id):
        self.connect()
        self.cursor.execute("SELECT * FROM ACTIVE_INSURANCE WHERE ACTIVE_INSURANCE_ID=%s", [active_insurance_id])
        active_insurance = self.cursor.fetchone()
        self.disconnect()
        return active_insurance

    def find_by_customer_id(self, customer_id):
        self.connect()
        self.cursor.execute("SELECT * FROM ACTIVE_INSURANCE WHERE CUSTOMER_ID=%s", [customer_id])
        active_insurances_list = self.cursor.fetchall()
        self.disconnect()
        return active_insurances_list

    # def find_active_insurances(self, customer_id, status=1):
    #     self.connect()
    #     self.cursor.execute(
    #         "SELECT SERVICE, NUMBER_OF_DURATION, DURATION_PERIOD, EXPIRE_DATE FROM ACTIVE_INSURANCE WHERE CUSTOMER_ID = %s AND STATUS=%s",
    #         [customer_id, status])
    #     active_insurances_list = self.cursor.fetchall()
    #     self.disconnect()
    #     return active_insurances_list
