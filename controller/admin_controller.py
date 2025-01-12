from controller.exceptions.my_exceptions import DuplicateUsernameError
from model.da.admin_da import AdminDa
from model.entity.admin import Admin


class AdminController:

    @classmethod
    def save(cls, name, family, username, password):
        if AdminController.find_by_username(username)[0]:
            raise DuplicateUsernameError()
        else:
            admin = Admin(name, family, username, password)
            AdminDa.save(admin)
            return True, f"Admin({admin}) saved successfully"

    @classmethod
    def edit(cls, name, family, username, password, person_id):
        admin = Admin(name, family, username, password)
        admin.person_id = person_id
        AdminDa.edit(admin)
        return True, f"Admin({admin}) edited successfully"

    @classmethod
    def remove(cls, person_id):
        AdminDa.remove(person_id)
        return True, f"Admin({person_id}) removed successfully"

    @classmethod
    def find_all(cls):
        return True, AdminDa.find_all()

    @classmethod
    def find_by_id(cls, person_id):
        return True, AdminDa.find_by_id(person_id)

    @classmethod
    def find_by_username(cls, username):
        return True, AdminDa.find_by_username(username)

    @classmethod
    def find_by_username_and_password(cls, username, password):
        if AdminDa.find_by_username_and_password(username, password):
            return True
