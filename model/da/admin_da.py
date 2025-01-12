from model.da.da import Da


class AdminDa(Da):
    @classmethod
    def save(cls, admin):
        cls.connect()
        cls.cursor.execute(
            "INSERT INTO ADMINS (name, family, username, password) VALUES (%s, %s, %s, %s)",
            [admin.name, admin.family, admin.username, admin.password]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def edit(cls, admin):
        cls.connect()
        cls.cursor.execute(
            "UPDATE ADMINS SET PASSWORD=%s WHERE ADMIN_ID=%s",
            [admin.password, admin.admin_id]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def remove(cls, admin_id):
        cls.connect()
        cls.cursor.execute(
            "DELETE FROM ADMINS WHERE ADMIN_ID=%s",
            [admin_id]
        )
        cls.connection.commit()
        cls.disconnect()

    @classmethod
    def find_all(cls):
        cls.connect()
        cls.cursor.execute("SELECT * FROM ADMINS")
        admins_list = cls.cursor.fetchall()
        cls.disconnect()
        return admins_list

    @classmethod
    def find_by_id(cls, admin_id):
        cls.connect()
        cls.cursor.execute("SELECT * FROM ADMINS WHERE ADMIN_ID=%s", [admin_id])
        admin = cls.cursor.fetchone()
        cls.disconnect()
        return admin

    @classmethod
    def find_by_username(cls, username):
        cls.connect()
        cls.cursor.execute("SELECT * FROM ADMINS WHERE USERNAME=%s", [username])
        admins_list = cls.cursor.fetchall()
        cls.disconnect()
        return admins_list

    @classmethod
    def find_by_username_and_password(cls, username, password):
        cls.connect()
        cls.cursor.execute("SELECT * FROM ADMINS WHERE USERNAME=%s AND PASSWORD=%s", [username, password])
        admin = cls.cursor.fetchone()
        cls.disconnect()
        return admin
