from model.da.da import Da


class InsuranceDa(Da):
    @classmethod
    def save(cls, insurance):
        cls.connect()
        cls.cursor.execute(
            "INSERT INTO INSURANCES (service, number_of_duration, duration_period, cost) VALUES (%s, %s, %s, %s)",
            [insurance.service, insurance.number_of_duration, insurance.duration_period, insurance.cost]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def edit(cls, insurance):
        cls.connect()
        cls.cursor.execute(
            "UPDATE INSURANCES SET NUMBER_OF_DURATION=%s, DURATION_PERIOD=%s, COST=%s WHERE INSURANCE_ID=%s",
            [insurance.number_of_duration, insurance.duration_period, insurance.cost, insurance.insurance_id]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def remove(cls, insurance_id):
        cls.connect()
        cls.cursor.execute(
            "DELETE FROM INSURANCES WHERE INSURANCE_ID=%s",
            [insurance_id]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def find_all(cls):
        cls.connect()
        cls.cursor.execute("SELECT * FROM INSURANCES")
        insurances_list = cls.cursor.fetchall()
        cls.disconnect()
        return insurances_list

    @classmethod
    def find_by_id(cls, insurance_id):
        cls.connect()
        cls.cursor.execute("SELECT * FROM INSURANCES WHERE INSURANCE_ID=%s", [insurance_id])
        insurance = cls.cursor.fetchone()
        cls.disconnect()
        return insurance

    @classmethod
    def find_by_service(cls, service):
        cls.connect()
        cls.cursor.execute("SELECT * FROM INSURANCES WHERE SERVICE=%s", [service])
        insurances_list = cls.cursor.fetchall()
        cls.disconnect()
        return insurances_list
