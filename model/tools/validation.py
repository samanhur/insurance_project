import re
from model.tools.decorators import exception_handling
from controller.exceptions.my_exceptions import *
from datetime import date, datetime


class Validator:
    @classmethod
    @exception_handling
    def name_validator(cls, name):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,45}$", name):
            return name
        else:
            raise InvalidNameError()

    @classmethod
    @exception_handling
    def national_code_validator(cls, national_code):
        if isinstance(national_code, str):
            if re.match(r"^[0-9]{10}$", national_code):
                return national_code
            elif re.match(r"^[0-9]{3}-[0-9]{6}-[0-9]{1}$", national_code):
                return national_code
            else:
                raise InvalidNationalCodeError()
        else:
            raise InvalidNationalCodeError()

    @classmethod
    @exception_handling
    def date_validator(cls, date_):
        if isinstance(date_, date) and (date_ < date.today()):
            return date_
        elif isinstance(date_, str):
            date_ = date_.replace("/", "-")
            try:
                date_ = datetime.strptime(date_, "%Y-%m-%d").date()
            except Exception:
                raise InvalidDateError()
            else:
                if date_ < date.today():
                    return date_
        else:
            raise InvalidDateError()

    @classmethod
    @exception_handling
    def phone_validator(cls, phone):
        if isinstance(phone, str):
            if re.match(r"^09[0-9]{2}[\-]?[0-9]{7}$", phone):
                return phone
            elif re.match(r"^\+989[0-9]{9}$", phone):
                return phone
            else:
                raise InvalidPhoneError()
        else:
            raise InvalidPhoneError()

    @classmethod
    @exception_handling
    def username_validator(cls, username):
        if isinstance(username, str) and re.match(r"^[a-zA-Z_]{1,}[a-zA-Z0-9_]*$", username):
            return username
        else:
            raise InvalidUsernameError()

    @classmethod
    @exception_handling
    def password_validator(cls, password):
        if isinstance(password, str) and re.match(
                r"^(?=.+[A-Z])(?=.+[a-z])(?=.+[0-9])(?=.+[@#$%^&+=_\s])[A-Za-z0-9@#$%^&+=_\s]{8,}$", password):
            return password
        else:
            raise InvalidPasswordError(())

    @classmethod
    @exception_handling
    def amount_validator(cls, amount):
        if isinstance(amount, int) and amount >= 0:
            return amount
        else:
            raise InvalidAmountError()

    @classmethod
    @exception_handling
    def time_duration_validator(cls, time_duration):
        if isinstance(time_duration, str) and time_duration in ("days", "month", "year", "years"):
            return time_duration
        else:
            raise InvalidTimeDurationError()