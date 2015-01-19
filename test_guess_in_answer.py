from mystery_word import guess_in_answer


def correct_guess_not_win():
    assert guess_in_answer('hola', ['o'], 7) == ['o']
