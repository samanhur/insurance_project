from model.tools.validation import Validator


class Admin:
    def __init__(self, name, family, username, password):
        self.admin_id = None
        self.name = name
        self.family = family
        self.username = username
        self.password = password

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validator.name_validator(name)

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validator.name_validator(family)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = Validator.username_validator(username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = Validator.password_validator(password)
