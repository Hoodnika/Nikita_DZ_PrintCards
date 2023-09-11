
from funcs.utils import load_operations, sorted_operations, censored_sender, cencored_addressee, new_time_format

def test_load_operations():
    assert load_operations("test.json")[0] ==  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

def test_sorted_operations():
    assert sorted_operations("test.json")[0] == {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

def test_new_time_format():
    assert new_time_format("test.json",2) == "04.04.2019"

def test_censored_sender():
    assert censored_sender("test.json", 0) == "Maestro 1596 83** **** 5199 ->"
    assert censored_sender("test.json", 3) == "Счет **6952 ->"
    assert censored_sender("test.json", 5) == "На"
    assert censored_sender("test.json", 4) == "Visa Gold 5999 41** **** 6353 ->"

def test_cencored_addressee():
    assert cencored_addressee("test.json", 0) == "Счет **9589"

