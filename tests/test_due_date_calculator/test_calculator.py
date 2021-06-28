import pytest

from due_date_calculator.calculator import (
    calculate_due_date, check_submit_date_constraints, add_weekdays,
    add_remaining_hours, check_turnaround_time_constraints
)


def test_calculate_due_date(input_datetime_object):
    # Setup
    submit_date, turnaround_time, desired_due_date = input_datetime_object
    # Exercise
    actual_due_date = calculate_due_date(submit_date, turnaround_time)
    # Verify
    assert desired_due_date == actual_due_date


def test_check_submit_date_constraints(bad_submit_date):
    # Setup
    # Exercise + Verify
    with pytest.raises((TypeError, ValueError)):
        check_submit_date_constraints(bad_submit_date)


def test_check_turnaround_time_constraints(bad_turnaround_time):
    # Setup
    # Exercise + Verify
    with pytest.raises((TypeError, ValueError)):
        check_turnaround_time_constraints(bad_turnaround_time)


def test_add_weekdays(input_add_weekdays):
    # Setup
    submit_date, n_weekdays, desired_due_date = input_add_weekdays
    # Exercise
    actual_due_date = add_weekdays(submit_date, n_weekdays)
    assert desired_due_date == actual_due_date


def test_add_remaining_days(input_add_remaining_hours):
    # Setup
    date, hours, desired_due_date = input_add_remaining_hours
    # Exercise
    actual_due_date = add_remaining_hours(date, hours)
    assert desired_due_date == actual_due_date
