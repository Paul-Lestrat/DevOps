import pytest
from utils import simple_add

def test_1():
    added = simple_add(3, 5)
    assert added == 9
    
def test_2():
    added = simple_add(7, 9)
    assert added == 16
