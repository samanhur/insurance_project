from datetime import date

from model.tools.validation import Validator


class Person:
    def __init__(self, name, family, national_code, birth_date, username, password, status=True):
        self.person_id = None
        self.name = name
        self.family = family
        self.national_code = national_code
        self.birth_date = birth_date
        self.username = username
        self.password = password
        self.status = status

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
    def national_code(self):
        return self._national_code

    @national_code.setter
    def national_code(self, national_code):
        self._national_code = Validator.national_code_validator(national_code)

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = Validator.date_validator(birth_date)

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

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, bool):
            self._status = status
        elif isinstance(status, int) and status in (1,0):
            self._status = 1 if status == 1 else 0

#
# person = Person("saman", "ghasemi", "1234567890", "2004-07-31", "samanhur",
#                 "S@man_G0510")
#
# print(list(person.__dict__.values()))
