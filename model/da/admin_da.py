from model.da.da import Da


class AdminDa(Da):
    def save(self, admin):
        self.connect()
        self.cursor.execute(
            "INSERT INTO ADMINS (name, family, username, password) VALUES (%s, %s, %s, %s)",
            [admin.name, admin.family, admin.username, admin.password]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, admin):
        self.connect()
        self.cursor.execute(
            "UPDATE ADMINS SET PASSWORD=%s WHERE ADMIN_ID=%s",
            [admin.password, admin.admin_id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, admin_id):
        self.connect()
        self.cursor.execute(
            "DELETE FROM ADMINS WHERE ADMIN_ID=%s",
            [admin_id]
        )
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM ADMINS")
        admins_list = self.cursor.fetchall()
        self.disconnect()
        return admins_list

    def find_by_id(self, admin_id):
        self.connect()
        self.cursor.execute("SELECT * FROM ADMINS WHERE ADMIN_ID=%s", [admin_id])
        admin = self.cursor.fetchone()
        self.disconnect()
        return admin

    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("SELECT * FROM ADMINS WHERE USERNAME=%s", [username])
        admins_list = self.cursor.fetchall()
        self.disconnect()
        return admins_list

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("SELECT * FROM ADMINS WHERE USERNAME=%s AND PASSWORD=%s", [username, password])
        admin = self.cursor.fetchone()
        self.disconnect()
        return admin
