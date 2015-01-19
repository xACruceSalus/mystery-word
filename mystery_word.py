import random


guesses = 8


def mystery_game_process(playing_again=False):
    """This function triggers the mystery_game. A user is presented
    with a random word. The user is then shown the word with blank spaces
    and told how many chars there are. Then the user must begin guessing."""

    if not playing_again:
        help_docs()

    word_answer = get_random_word(user_difficulty_choice())

    partial_answer_string = fancy_view_word(word_answer)
    print("  {}      {} guesses left.".format(partial_answer_string,
                                              guesses))
    user_guess_process(word_answer)

    return True


def user_difficulty_choice():
    """This function asks the user what difficulty they'd like."""

    difficulty = 0

    try:
        difficulty = int(input("""
        What difficulty would you like to play at:
        Type '1' for easy
        Type '2' for medium
        Type '3' for hard
        Type difficulty level here -->> """))
    except:
        print("Please only enter 1, 2, or 3 for difficulty.")
        return user_difficulty_choice()
    return difficulty


def get_random_word(difficulty):
    """Produces a word at random from the dictionary hosted on
    your local computer. If a difficulty values is passed in, then
    the game will adjust accordingly."""

    with open('/usr/share/dict/words') as file:
        read_lines = file.read()
        words_list = read_lines.split()

        if difficulty == 3:
            eli_word_list = [word for word in words_list if len(word) >= 10]
            final_word = random.choice(eli_word_list).lower()
        elif difficulty == 2:
            eli_word_list = [word for word in words_list if len(word) >= 6
                             and len(word) <= 10]
            final_word = random.choice(eli_word_list).lower()
        elif difficulty == 1:
            eli_word_list = [word for word in words_list if len(word) >= 4
                             and len(word) <= 6]
            final_word = random.choice(eli_word_list).lower()
        else:
            eli_word_list = [word for word in words_list if len(word) > 15]
            final_word = random.choice(eli_word_list).lower()

    return(final_word)


def user_guess_process(answer_string):
    """This function defines the flow a user goes through when playing
    the mystery game. User gets n number of guesses to figure out the
    given word."""

    guessed_char_list = []
    counter = guesses

    while counter > 0:
        guess = user_live_guess()

        if guess == 'quit':
            return quit()
        elif guess == 'help':
            help_docs()
        elif guess == 'view':
            partial_answer_string = fancy_view_word(word_answer)
            print("  {}      {} guesses left.".format(partial_answer_string,
                                                      counter))
        elif guess in guessed_char_list:
            print("You already guessed that.")
        elif len(guess) > 1:
            print("One letter at a time please.")

        elif guess in list(answer_string):
            guessed_char_list.append(guess)
            guessed_char_list = guess_in_answer(answer_string,
                                                guessed_char_list,
                                                counter)
        else:
            counter = incorrect_guess(counter, guess, answer_string)
            guessed_char_list.append(guess)

    return True


def user_live_guess():
    guess = input("What letter do you guess? ").lower()

    return guess


def guess_in_answer(answer_string, guessed_char_list, counter):
    """This function denotes the process a user goes through if they
    guess a correct letter."""

    partial_answer_string = fancy_view_word(answer_string,
                                            guessed_char_list)

    if '_' not in partial_answer_string:
        print(partial_answer_string)
        print("You Won!!!")
        return play_again_request()

    else:
        print("You got a letter!\n  {}      {}"
              " guesses left.".format(partial_answer_string,
                                                  counter))

    return guessed_char_list

def incorrect_guess(counter, a_guess, answer_string):
    """This function denotes the process a user goes through if they
    guess an incorrect letter."""

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    partial_answer_string = fancy_view_word(answer_string)


    if a_guess in alphabet and counter > 0:
        counter -= 1
        if counter == 0:
            print("You are out of guesses and therefore lose.")
            print("The word was '{}'.".format(answer_string.upper()))
            return play_again_request()

        else:
            print("Nope, please try again! You have {} guesses left"
                  .format(counter))
            return counter
    else:
        print('That is not a valid character.')
        return counter


def fancy_view_word(answer_string, guessed_char_list=[]):
    """This function shows the user how many characters the
    passed in word has along with a visualization of the letters
    with underscores."""

    partial_answer_string = ''

    for char in answer_string:
        if char in guessed_char_list:
            partial_answer_string += char + ' '
        else:
            partial_answer_string += '_ '

    return partial_answer_string


def play_again_request():
    """This function allows the user to choose play again or
    not when it's called."""

    play_again_request = input("Would you like "
                               "to play again? (y/n) ")
    if play_again_request.lower() == 'y':
        return mystery_game_process(True)
    else:
        return quit()


def help_docs():
    """ When called, this function provides the help docs
    to the user."""

    print("""
    Thanks for playing the GUESS game! To win the GUESS
    game, you must guess the letters in the word. If you
    run out of your {} guesses before you can guess the
    word, then you lose.

    Type "help" for these instructions again.
    Type "view" to see to see the word so far.
    Type "quit" to exit.
          """.format(guesses))
    print(('=' * 60))
    print(('=' * 60))

    return True

# mystery_game_process()
