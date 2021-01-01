import pytest
import random
from pathlib import Path


@pytest.fixture
def data_len():
    return 10

@pytest.fixture
def data_max():
    return 100

@pytest.fixture
def data(data_len,data_max):
    return [random.randint(0, data_max) for _ in range(data_len)]

@pytest.fixture
def unique_data(data_len, data_max):
    return random.sample(list(range(data_max)), k=data_len)


@pytest.fixture(scope='session')
def all_words():
    p = Path('/usr/share/dict/american-english')
    assert p.is_file()
    with p.open() as f:
        words = f.readlines()

    return [w.strip() for w in words]


@pytest.fixture
def values(data_len, all_words):
    return random.choices(all_words, k=data_len)
