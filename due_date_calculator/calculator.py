import datetime

# Time range for working hours
WH_FROM = 9
WH_TO = 17


def calculate_due_date(
        submit_date: datetime.datetime,
        turnaround_time: int
) -> datetime.datetime:
    """Calculates due date for a ticket for an issue tracking system.

    :param submit_date: Date when the issue is submitted
    :param turnaround_time: Time for the issue to be solved in hours
    :return: Date until the issue should be solved
    """
    check_submit_date_constraints(submit_date)
    check_turnaround_time_constraints(turnaround_time)

    n_weekdays, hours = divmod(turnaround_time, 8)

    due_date = add_weekdays(submit_date, n_weekdays)
    due_date = add_remaining_hours(due_date, hours)

    return due_date


def check_submit_date_constraints(submit_date: datetime.datetime) -> None:
    """Passes if the defined constraints are met for submit date, otherwise 
    raises an exception.

    :param submit_date: Date when the issue is submitted
    :return:
    """
    if not isinstance(submit_date, datetime.datetime):
        raise TypeError("Submit date should be datetime object!")
    if submit_date.weekday() > 4:
        raise ValueError("Issues can not be reported on weekends!")
    if submit_date.hour < WH_FROM or submit_date.hour > WH_TO:
        raise ValueError(
            "Issues can not be reported outside of working hours!"
        )
    

def check_turnaround_time_constraints(turnaround_time: int) -> None:
    """Passes if the defined constraints are met for turnaround time, otherwise
    raises an exception.
    
    :param turnaround_time: Time for the issue to be solved
    :return: 
    """
    if not isinstance(turnaround_time, int):
        raise TypeError("Turnaround time should be integer!")
    if turnaround_time < 0:
        raise ValueError("Turnaround time should be greater than zero!")


def add_weekdays(
        submit_date: datetime.datetime,
        n_weekdays: int
) -> datetime.datetime:
    """Adds a given number of weekdays to submit date taking into consideration
    the working days constraint.

    :param submit_date: Date when the issue is submitted
    :param n_weekdays: Number of working days to add to submit_date
    :return: Resulting datetime object
    """
    if n_weekdays:
        n_weeks, n_remaining_days = divmod(n_weekdays, 5)
        n_days = n_weeks * 7 + n_remaining_days
        td = datetime.timedelta(days=n_days)

        return submit_date + td
    else:
        return submit_date


def add_remaining_hours(
        date: datetime.datetime,
        hours: int
) -> datetime.datetime:
    """Adds remaining number of hours to submit date taking into consideration
    the working hours and working days constraints.

    :param date: Date to which add number of hours
    :param hours: Hours remaining in range of [0, 7]
    :return: Calculated due date based on working hours and days
    """
    if hours:
        if date.hour + hours > WH_TO:
            remaining_hours = WH_FROM + hours - (WH_TO - date.hour)
            due_date = date.replace(hour=remaining_hours)
            due_date += datetime.timedelta(days=1)

            if due_date.weekday() > 4:
                due_date += datetime.timedelta(days=2)
        else:
            due_date = date + datetime.timedelta(hours=hours)

        return due_date
    else:
        return date
