import pytest
from funkcije import *

def test_sabiranje():
    assert sabiranje(2,3) == 5

def test_mnozenje():
    assert mnozenje(2,3) == 6
