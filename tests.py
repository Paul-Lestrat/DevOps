import pytest
from utils import simple_add

def test_1():
    added = simple_add(3, 5)
    assert added == 8
