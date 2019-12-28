from sort.insertion import insertion_sort
from tests.test_sort.common import validate_sorted

def test_insertion_sort(data):
    new_data = insertion_sort(data)
    validate_sorted(new_data)
