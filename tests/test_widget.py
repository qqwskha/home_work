import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("data,expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(data: str, expected: str) -> None:
    assert mask_account_card(data) == expected


@pytest.mark.parametrize("data", [
    "Некорректные данные",
    "Visa Platinum",
    "Счет",
    "Visa Platinum 12345a",
    "Счет abc123",
])
def test_mask_account_card_invalid(data: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(data)


@pytest.mark.parametrize("date_str,expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-25T15:30:00", "25.12.2023"),
])
def test_get_date(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected


@pytest.mark.parametrize("date_str", [
    "Некорректная строка",
    "2024-13-01T00:00:00",
    "2024-03-32",
    "",
])
def test_get_date_invalid(date_str: str) -> None:
    with pytest.raises(ValueError):
        get_date(date_str)
