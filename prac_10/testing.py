import doctest


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.

    >>> repeat_string('hi', 2)
    'hi hi'
    >>> repeat_string('hello', 3)
    'hello hello hello'
    """
    # FIX: join with spaces, not just multiply
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """Determine if word is as long or longer than length.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifragilisticexpialidocious")
    True
    """
    return len(word) >= length


def phrase_to_sentence(phrase):
    """Format a phrase as a sentence starting with a capital and ending with a single full stop.

    >>> phrase_to_sentence("hello")
    'Hello.'
    >>> phrase_to_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> phrase_to_sentence("this is cool")
    'This is cool.'
    """
    phrase = phrase.strip()
    # Capitalise first letter
    phrase = phrase[0].upper() + phrase[1:]
    # Ensure it ends with one '.'
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase


# Tests for repeat_string
assert repeat_string('hi', 2) == 'hi hi'

# Tests for Car fuel setting
from car import Car  # assuming Car class is from earlier pracs
assert Car("Test", 0).fuel == 0
assert Car("Test", 10).fuel == 10

# Run doctests
doctest.testmod()
