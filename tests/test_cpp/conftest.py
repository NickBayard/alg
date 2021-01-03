import pytest
import subprocess


@pytest.fixture
def data_str(data):
    v = '\n'.join([str(x) for x in data])
    return f'{v}\nq\n'

@pytest.fixture
def app():
    return 'quick'


@pytest.fixture
def data_result(app, value_str):
    return subprocess.check_output(f'cpp/bin/{app}'.split(), text=True, input=data_str)
