import datetime

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    today_date = datetime.date.today()
    today_datetime = datetime.datetime(
        today_date.year,
        today_date.month,
        today_date.day,
        10,
        10
    )
    tomorrow_datetime = today_datetime + datetime.timedelta(days=1)

    assert compose_datetime_from('', '10:10') == today_datetime
    assert compose_datetime_from('tomorrow', '10:10') == tomorrow_datetime
