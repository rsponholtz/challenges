from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as myfile:
        words = myfile.read().splitlines()
    return words

def calc_word_value(thestr):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    letter_scores = [LETTER_SCORES.get(char.upper(), 0) for char in thestr]
    return sum(letter_scores)

def max_word_value(wordlist=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(wordlist, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
