import datetime
from unittest import mock
from unittest.mock import MagicMock
from app.main import outdated_products


@mock.patch("app.main.datetime.date.today")
def test_one_outdated_products(mock_date_today: MagicMock) -> None:
    mock_date_today.return_value = datetime.date(2022, 2, 1)
    result = outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }])
    assert result == ["duck"]


@mock.patch("app.main.datetime.date.today")
def test_all_outdated_products(mock_date_today: MagicMock) -> None:
    mock_date_today.return_value = datetime.date(2022, 2, 11)
    result = outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }])
    assert result == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime.date.today")
def test_no_outdated_products(mock_date_today: MagicMock) -> None:
    mock_date_today.return_value = datetime.date(2022, 1, 1)
    result = outdated_products([
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }])
    assert result == []
