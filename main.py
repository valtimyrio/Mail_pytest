import pytest


def test_dict_diff_value():
    a = {
        "имя": "петя",
        "возраст": 13
    }
    b = {
        "имя": "петя",
        "возраст": 13
    }

    assert a == b


a = {
    "Имя": "петя",
    "возраст": 13
}
b = {
    "Ымя": "Пэтя",
    "возраст": 13
}


@pytest.mark.parametrize("a,b,result", [(a, a, True), (a, b, False)])
def test_dict_diff_key(a, b, result):
    assert (a == b) == result


def test_dict_call():
    a = {
        "Имя": "петя",
        "возраст": 13
    }
    assert a.get("Имя") == "петя"


def test_set_copy():
    a = {"1", 2, "abc"}
    b = a.copy()
    print(type(a))
    assert a == b


def test_set_equal():
    a = {"1", 2, "abc"}
    b = {"abc", 2, "1"}
    assert a == b


def test_set_negative():
    a = {1, 2, 3}
    b = "Петя"
    try:
        assert a in b
    except TypeError:
        pass
