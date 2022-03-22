"""Generate Markov text from text files."""

from random import choice


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
    current_key = choice(list(chains.keys()))
    i = 0
    while current_key in chains:
        for key in current_key:
            words.append(key)

        next_link = choice(chains[current_key])
        words.append(next_link)

        possibilities = []
        for key in list(chains.keys()):
            if key[0] == next_link:
                possibilities.append(key)

        print(current_key)
        print(i)
        i += 1

        if len(possibilities) > 0:
            current_key = choice(possibilities)

    print(possibilities)

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
