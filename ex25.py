def break_words(stuff):
    """This function will break up words for us."""
    print(">>>> break_words", repr(stuff))
    words = stuff.split(' ')
    print("-----words=", words)
    print("<< exit break_words")
    return words

def sort_words(words):
    """Sorts the words."""
    print(">>>> sort_words", repr(words))
    print('-----sorted words',sorted(words))
    print("<< exit sort_words")
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    print(">>>>>sort_sentence=", repr(sentence))
    words = break_words(sentence)
    print(">>words", words)
    print(">>sort_words",sort_words(words))
    print("<<<<<exit sort_sentence")
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
