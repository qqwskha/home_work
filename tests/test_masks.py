import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number,expected", [
    (7000792289606361, "7000 79** **** 6361"),
    (1234567890123456, "1234 56** **** 3456"),
    (1111222233334444, "1111 22** **** 4444"),
])
def test_get_mask_card_number(card_number: int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [-1234, 0])
def test_get_mask_card_number_invalid(card_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("account_number,expected", [
    (73654108430135874305, "**4305"),
    (987654321, "**4321"),
    (1234, "**1234"),
])
def test_get_mask_account(account_number: int, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", [-1234, 0])
def test_get_mask_account_invalid(account_number: int) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account_number)
