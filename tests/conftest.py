import pytest
import random

@pytest.fixture
def data_len():
    return 10

@pytest.fixture
def data_max():
    return 100

@pytest.fixture
def data(data_len,data_max):
    return [random.randint(0, data_max) for _ in range(data_len)]

