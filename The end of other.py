def checkio(words_set):
    words_set = list(words_set)
    if len(words_set) <= 1:
        return False
    for i, outer in enumerate(words_set):
        for j, inner in enumerate(words_set):
            if i == j:
                continue
            if outer.endswith(inner):
                return True
    return False

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
