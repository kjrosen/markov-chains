"""Generate Markov text from text files."""

from curses.ascii import isupper
from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    input_text = open(file_path).read()

    return str(input_text)


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    
    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    
    chains = {}
    input_text = text_string.split()

    for num in range(len(input_text) - 1):
        keys = (input_text[num], input_text[num + 1])

        if keys in chains:
            try:
                chains[keys].append(input_text[num + 2])
            except:
                pass
        else:
            try:
                chains[keys] = [input_text[num + 2]]
            except:
                pass

    return chains


def make_text(chains):
    """Return text from chains."""

    builded_text = []
    upper_keys = []
    punctuation = (".", "!", "?")

    for key in list(chains.keys()):
        if key[0][0].isupper():
            upper_keys.append(key)
    
    current_key = choice(upper_keys)
    sentences = 0

    while True:
        for key in current_key:
            builded_text.append(key)

        next_link = choice(chains[current_key])
        possibilities = []

        for key in list(chains.keys()):
            if key[0] == next_link:
                possibilities.append(key)
        
        if current_key[1].endswith(punctuation):
            # sentences += 1
            break
        elif len(possibilities) == 0:
            if not current_key[1].endswith(punctuation):
                builded_text.append(next_link)
            break

        current_key = choice(possibilities)


    return ' '.join(builded_text)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# Get a Markov chain
chains = make_chains(input_text)
# Produce random text
random_text = make_text(chains)

print(random_text)
