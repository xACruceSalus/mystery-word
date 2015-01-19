from mystery_word import get_random_word


def test_does_word_return():
    assert type(get_random_word(1)) == str

def test_difficulty_easy():
    word_length = len(get_random_word(1))
    assert word_length >= 4 and word_length <= 6

def test_difficulty_medium():
    word_length = len(get_random_word(2))
    assert word_length >= 6 and word_length <= 10

def test_difficulty_hard():
    assert len(get_random_word(3)) >= 10

def test_other_difficulty():
    assert len(get_random_word('hi')) > 15

def test_no_value_return():
    assert len(get_random_word(89)) > 1
