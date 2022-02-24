import pytest


def func(x):
    return x + 1

@pytest.mark.mark_test_for_run
def test_answer():
    assert func(3) == 5
