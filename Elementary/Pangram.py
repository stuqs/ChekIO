import string


def check_pangram(text):
    text = text.lower()
    for letter in string.ascii_lowercase:
        if text.count(letter) < 1:
            return False
    return True

if __name__ == '__main__':
    pass
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog.") == True
    assert check_pangram("ABCDEF.") == False