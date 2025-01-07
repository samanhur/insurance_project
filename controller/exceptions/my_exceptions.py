class InvalidNameError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "Name entered is not valid!")


class InvalidNationalCodeError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "National code entered is not valid!")


class InvalidDateError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "Date entered is not valid!")


class InvalidPhoneError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "Phone number entered is not valid!")


class InvalidUsernameError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "Username entered is not valid!")


class InvalidPasswordError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "Password entered is not valid!")


class InvalidAmountError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "Amount entered is not valid!")


class InvalidTimeDurationError(Exception):
    def __init__(self, *args):
        super().__init__(*args, "Time duration entered is not valid!\nIt's must be from(days, month, year, years)")
