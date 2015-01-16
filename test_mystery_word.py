from mystery_word import get_random_word


def test_does_word_return():
    assert type(get_random_word(1)) == str

def test_difficulty_easy():
    assert len(get_random_word(1)) < 5

def test_difficulty_medium():
    assert len(get_random_word(1)) < 5

def test_difficulty_hard():
    assert len(get_random_word(1)) < 5
