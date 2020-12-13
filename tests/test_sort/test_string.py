import pytest
import random

from sort.key_index_sort import sort, multi_sort, Alphabet


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
    print(sort(data, 5))


@pytest.fixture
def suit_prims():
    return ['C', 'D', 'H', 'S']


@pytest.fixture
def card_prims():
    return [str(i) for i in range(2, 10)] + ['J', 'Q', 'K', 'A']


@pytest.fixture
def mixed_deck(suit_prims, card_prims):
    deck = [f'{suit}{num}' for suit in suit_prims for num in card_prims]
    random.shuffle(deck)
    return deck


def test_deck(mixed_deck, suit_prims, card_prims):
    multi_sort(mixed_deck, 2, alphabets=[Alphabet(suit_prims), Alphabet(card_prims)])
    print(mixed_deck)
