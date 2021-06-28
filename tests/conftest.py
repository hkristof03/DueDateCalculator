from datetime import datetime, timedelta

import pytest


'''
1. case: Addition according to the example in the description
2.-3. case: Add 14 days and take into consideration working days
4. case: Add 4 hours and take into consideration working hours
5. case: Add 116 hours to combine case 2. & 4.
'''

input_params = [
    (datetime(2021, 6, 28, 14, 12), 16, datetime(2021, 6, 30, 14, 12)),
    (datetime(2021, 6, 28, 14, 12), 112, datetime(2021, 7, 16, 14, 12)),
    (datetime(2021, 6, 28, 14, 12), 40, datetime(2021, 7, 5, 14, 12)),
    (datetime(2021, 6, 28, 14, 12), 4, datetime(2021, 6, 29, 10, 12)),
    (datetime(2021, 6, 28, 14, 12), 116, datetime(2021, 7, 19, 10, 12)),
]


@pytest.fixture(scope='module', params=input_params)
def input_datetime_object(request):
    return request.param


bad_submit_date_params = [
    '2020.06.28 14:12',
    1624623120.0,
    1624623120,
    datetime(2021, 6, 28, 5),
    datetime(2021, 6, 28, 19),
    datetime(2021, 6, 27, 15)
]


@pytest.fixture(scope='module', params=bad_submit_date_params)
def bad_submit_date(request):
    return request.param


bad_turnaround_time_params = [
    timedelta(hours=16),
    16.0,
    '16',
    -16
]


@pytest.fixture(scope='module', params=bad_turnaround_time_params)
def bad_turnaround_time(request):
    return request.param


add_weekdays_params = [
    (datetime(2021, 6, 28, 14, 12), 0, datetime(2021, 6, 28, 14, 12)),
    (datetime(2021, 6, 28, 14, 12), 4, datetime(2021, 7, 2, 14, 12)),
    (datetime(2021, 6, 28, 14, 12), 14, datetime(2021, 7, 16, 14, 12))
]


@pytest.fixture(scope='module', params=add_weekdays_params)
def input_add_weekdays(request):
    return request.param


add_remaining_hours_params = [
    (datetime(2021, 6, 28, 14, 12), 2, datetime(2021, 6, 28, 16, 12)),
    (datetime(2021, 6, 28, 14, 12), 4, datetime(2021, 6, 29, 10, 12)),
    (datetime(2021, 7, 2, 14, 12), 4, datetime(2021, 7, 5, 10, 12))
]


@pytest.fixture(scope='module', params=add_remaining_hours_params)
def input_add_remaining_hours(request):
    return request.param
