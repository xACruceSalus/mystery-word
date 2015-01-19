from mystery_word import fancy_view_word


def test_first_bad_guess():
    assert fancy_view_word('hola') == '_ _ _ _ '


def test_finished_result():
    assert fancy_view_word('hola', ['h', 'o', 'l',
                                    'a', 'r']) == 'h o l a '


def test_no_right_answers():
    assert fancy_view_word('hola', ['q', 'w', 'r']) == '_ _ _ _ '
