import pytest
import random
import subprocess


@pytest.fixture
def num_values():
    return 100

@pytest.fixture
def max_value():
    return 1000

@pytest.fixture
def values(num_values, max_value):
    return [random.randint(0, max_value) for _ in range(num_values)]

@pytest.fixture
def value_str(values):
    v = '\n'.join([str(x) for x in values])
    return f'{v}\nq\n'

@pytest.fixture
def app():
    return 'quick'


@pytest.fixture
def result(app, value_str):
    return subprocess.check_output(f'bin/{app}'.split(), text=True, input=value_str)
