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

    # make a variable  
    words = text_string.split()
    #split words
    for word in range(len(words)- 1):
        keys = (words[word], words[word + 1])


        if keys in chains:
        # if words[word] and words[word + 2]:
            try:
                chains[keys].append(words[word + 2])
            except:
                print()
        else:
            try:
                chains[keys] = [words[word + 2]]
            except:
                print()

    #loop in pairs, for loop with range of len(text)-1
    #make tuples
    #set as keys in dictionary

    #for each key find in words and save the next word as a value for that key


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    # get a random key and convert to a list
    # add that to the words list
    # get a random word from the values for that key
    # get a random key that starts with the second element of the previous key
    
    upper_keys = []
    for key in list(chains.keys()):
        if key[0][0].isupper():
            upper_keys.append(key)
    
    punctuation = (".", "!", "?")
    current_key = choice(upper_keys)

    while True:
        for key in current_key:
            words.append(key)

        next_link = choice(chains[current_key])
        if next_link.endswith(punctuation):
            words.append(next_link)
            break

        possibilities = []
        for key in list(chains.keys()):
            if key[0] == next_link:
                possibilities.append(key)

        print(current_key)
        
        
        if current_key[1].endswith(punctuation):
            break

        elif len(possibilities) > 0:
            current_key = choice(possibilities)

        else:
            # words.append(next_link)
            break

    return ' '.join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
