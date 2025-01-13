from datetime import date, timedelta

from controller.exceptions.my_exceptions import InvalidTimeDurationError


def expire_date_calculator(number_of_duration, duration_period):
    """
    This function take to input, number of duration and duration period
    and returns a number that determine this time is how many days later
    """
    if duration_period in ["day", "days"]:
        duration_period_days = 1
    elif duration_period in ["month", "months"]:
        duration_period_days = 30
    elif duration_period in ["season", "seasons"]:
        duration_period_days = 90
    elif duration_period in ["year", "years"]:
        duration_period_days = 365
    else:
        raise InvalidTimeDurationError()

    days_remaining = number_of_duration * duration_period_days

    expire_date = date.today() + timedelta(days=days_remaining)

    return expire_date
