import mysql.connector


class Da:
    @classmethod
    def __init__(cls):
        cls.connection = None
        cls.cursor = None

    @classmethod
    def connect(cls):
        cls.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="saman20",
            database="insurance_project"
        )
        cls.cursor = cls.connection.cursor()

    @classmethod
    def disconnect(cls):
        cls.cursor.close()
        cls.connection.close()
