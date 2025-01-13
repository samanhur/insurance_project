from model.da.da import Da


class InsuranceDa(Da):

    def save(self, insurance):
        self.connect()
        self.cursor.execute(
            "INSERT INTO INSURANCES (service, number_of_duration, duration_period, cost) VALUES (%s, %s, %s, %s)",
            [insurance.service, insurance.number_of_duration, insurance.duration_period, insurance.cost]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, insurance):
        self.connect()
        self.cursor.execute(
            "UPDATE INSURANCES SET NUMBER_OF_DURATION=%s, DURATION_PERIOD=%s, COST=%s WHERE INSURANCE_ID=%s",
            [insurance.number_of_duration, insurance.duration_period, insurance.cost, insurance.insurance_id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, insurance_id):
        self.connect()
        self.cursor.execute(
            "DELETE FROM INSURANCES WHERE INSURANCE_ID=%s",
            [insurance_id]
        )
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM INSURANCES")
        insurances_list = self.cursor.fetchall()
        self.disconnect()
        return insurances_list

    def find_by_id(self, insurance_id):
        self.connect()
        self.cursor.execute("SELECT * FROM INSURANCES WHERE INSURANCE_ID=%s", [insurance_id])
        insurance = self.cursor.fetchone()
        self.disconnect()
        return insurance

    def find_by_service(self, service):
        self.connect()
        self.cursor.execute("SELECT * FROM INSURANCES WHERE SERVICE=%s", [service])
        insurances_list = self.cursor.fetchall()
        self.disconnect()
        return insurances_list
