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
