from mystery_word import user_guess_process
from mystery_word import guess_in_answer
from mystery_word import incorrect_guess


def test_correct_guess_not_win():
    assert guess_in_answer('hola', ['o'], 7) == ['o']


def test_bad_guess_handling():
    assert incorrect_guess(5, '5', 'hello') == 5


def test_good_letter_guess():
    assert incorrect_guess(3, 'r', 'hola') == 2


def test_symbols_should_be_removed():
    assert incorrect_guess(4, '%', 'hola') == 4
