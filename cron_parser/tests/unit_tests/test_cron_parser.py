import pytest
from cron_parser.src.models import CronExpression


def test_valid_cron_minute_step():
    cron_string = "*/10 * * * * /usr/bin/find"
    cron = CronExpression.parse_cron(cron_string)
    expanded_cron = cron.expand()
    assert expanded_cron['minute'] == '0 10 20 30 40 50'


def test_valid_cron_hour_range():
    cron_string = "0 9-17 * * * /usr/bin/find"
    cron = CronExpression.parse_cron(cron_string)
    expanded_cron = cron.expand()
    assert expanded_cron['hour'] == '9 10 11 12 13 14 15 16 17'


def test_valid_cron_day_of_month_increment():
    cron_string = "0 0 */5 * * /usr/bin/find"
    cron = CronExpression.parse_cron(cron_string)
    expanded_cron = cron.expand()
    assert expanded_cron['day_of_month'] == '1 6 11 16 21 26 31'


def test_valid_cron_month_list():
    cron_string = "0 0 1 1-3 1,3,5 /usr/bin/find"
    cron = CronExpression.parse_cron(cron_string)
    expanded_cron = cron.expand()
    assert expanded_cron['month'] == '1 2 3'


def test_valid_cron_day_of_week_step():
    cron_string = "0 0 * * */2 /usr/bin/find"
    cron = CronExpression.parse_cron(cron_string)
    expanded_cron = cron.expand()
    assert expanded_cron['day_of_week'] == '1 3 5 7'


def test_invalid_cron_string_length():
    cron_string = "*/15 0 1,15 * 1-5"
    with pytest.raises(ValueError, match="Cron string must have 6 parts"):
        CronExpression.parse_cron(cron_string)


def test_invalid_cron_field_value():
    cron_string = "*/70 0 1,15 * 1-5 /usr/bin/find"
    with pytest.raises(ValueError, match=r"Value error, minute: Step value out of range: 70 "
                                         r"\(expected between 1 and 59\)"):
        CronExpression.parse_cron(cron_string)


def test_missing_command():
    cron_string = "*/15 0 1,15 * 1-5 "
    with pytest.raises(ValueError, match="Cron string must have 6 parts"):
        CronExpression.parse_cron(cron_string)


def test_star_field_expansion():
    cron = CronExpression.parse_cron("* * * * * /usr/bin/find")
    expanded_cron = cron.expand()
    assert expanded_cron['minute'] == ' '.join(map(str, range(60)))
    assert expanded_cron['hour'] == ' '.join(map(str, range(24)))
    assert expanded_cron['day_of_month'] == ' '.join(map(str, range(1, 32)))
    assert expanded_cron['month'] == ' '.join(map(str, range(1, 13)))
    assert expanded_cron['day_of_week'] == ' '.join(map(str, range(1, 8)))


if __name__ == '__main__':
    pytest.main()
