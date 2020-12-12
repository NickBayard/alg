import pytest

from sort import key_index_sort


@pytest.fixture
def data():
    return [(2, 'Anderson'),
            (3, 'Brown'),
            (3, 'Davis'),
            (4, 'Garcia'),
            (1, 'Harris'),
            (3, 'Jackson'),
            (4, 'Johnson'),
            (3, 'Jones'),
            (1, 'Martin'),
            (2, 'Martinez'),
            (2, 'Miller'),
            (1, 'Moore'),
            (2, 'Robinson'),
            (4, 'Smith'),
            (3, 'Taylor'),
            (4, 'Thomas'),
            (4, 'Thompson'),
            (2, 'White'),
            (3, 'Williams'),
            (4, 'Wilson')]

def test_key_index_sort(data):
    print(key_index_sort.sort(data, 5))
