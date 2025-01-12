from model.da.da import Da


class InsuranceListDa(Da):

    @classmethod
    def find_all(cls):
        cls.connect()
        cls.cursor.execute("SELECT * FROM INSURANCE_LIST")
        insurances_list = cls.cursor.fetchall()
        cls.disconnect()
        return True, insurances_list

    @classmethod
    def find_by_status(cls, customer_id, status=1):
        cls.connect()
        cls.cursor.execute("SELECT * FROM INSURANCE_LIST WHERE CUSTOMER_ID=%s AND STATUS=%s", [customer_id, status])
        insurances_list = cls.cursor.fetchall()
        cls.disconnect()
        return True, insurances_list
