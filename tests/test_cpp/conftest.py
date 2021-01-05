import pytest
import subprocess


@pytest.fixture
def app():
    return 'quick'


@pytest.fixture
def data_str(data):
    v = '\n'.join([str(x) for x in data])
    return f'{v}\nq\n'


@pytest.fixture
def key_value_str(data, values):
    v = '\n'.join([f'{k} {v}' for k,v in zip(data, values)])
    return f'{v}\nq\n'


@pytest.fixture
def use_key_value():
    return False


@pytest.fixture
def result(app, data_str, key_value_str, use_key_value):
    return subprocess.check_output(f'cpp/bin/{app}'.split(),
                                   text=True,
                                   input=key_value_str if use_key_value else data_str)
