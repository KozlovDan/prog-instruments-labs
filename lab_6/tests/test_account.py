import pytest
from unittest.mock import mock_open, patch
from lab_6.account import Account
from lab_6.transaction import Transaction

def test_deposit():
    acc = Account("Alice")
    acc.deposit(100)
    assert acc.get_balance() == 100
    assert acc.transactions[-1].description == "Deposit"

def test_withdraw():
    acc = Account("Bob", 200)
    acc.withdraw(50)
    assert acc.get_balance() == 150
    assert acc.transactions[-1].description == "Withdraw"

def test_withdraw_insufficient():
    acc = Account("Bob", 100)
    with pytest.raises(ValueError):
        acc.withdraw(150)

def test_deposit_negative():
    acc = Account("Alice")
    with pytest.raises(ValueError):
        acc.deposit(-10)

def test_withdraw_negative():
    acc = Account("Alice", 100)
    with pytest.raises(ValueError):
        acc.withdraw(-5)


@pytest.mark.parametrize("initial, deposit, expected", [
    (0, 100, 100),
    (50, 50, 100),
    (200, 0.5, 200.5),
])
def test_deposit_param(initial, deposit, expected):
    acc = Account("Test", initial)
    acc.deposit(deposit)
    assert acc.get_balance() == expected


def test_save_transactions():
    acc = Account("Alice")
    acc.deposit(100)
    m = mock_open()
    with patch("builtins.open", m):
        acc.save_transactions("dummy.json")
    m.assert_called_once_with("dummy.json", "w")

def test_load_transactions():
    mock_data = '[{"description": "Deposit", "amount": 100}]'
    acc = Account("Alice")
    m = mock_open(read_data=mock_data)
    with patch("builtins.open", m):
        acc.load_transactions("dummy.json")
    assert len(acc.transactions) == 1
    assert acc.transactions[0].amount == 100


def test_validate_amount_positive():
    acc = Account("Test")
    acc._validate_amount(10)
    with pytest.raises(ValueError):
        acc._validate_amount(0)
    with pytest.raises(ValueError):
        acc._validate_amount(-5)

def test_validate_funds():
    acc = Account("Test", 50)
    acc._validate_funds(50)
    with pytest.raises(ValueError):
        acc._validate_funds(51)

def test_record_transaction():
    acc = Account("Test")
    acc._record_transaction("Deposit", 100)
    assert isinstance(acc.transactions[-1], Transaction)
    assert acc.transactions[-1].amount == 100
