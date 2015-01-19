from mystery_word import incorrect_guess


def bad_guess_handling():
    assert incorrect_guess(5, '5', 'hello') == True

def good_letter_guess():
    assert incorrect_guess(3, 'r', 'hola') == 2

def symbols_should_be_removed():
    assert incorrect_guess(4, '%', 'hola') == 3
