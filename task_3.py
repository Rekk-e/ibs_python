# Main solution
def find_in_different_registers(words: list) -> list or None:
    """
    returns unique case-sensitive words in lowercase in one instance
    """

    duplicates = set()
    words_in_lower = {}

    for word in words:
        if word in words_in_lower:
            duplicates.add(word.lower())
        else:
            words_in_lower[word] = word.lower()

    return list(set(words_in_lower.values()) - duplicates)


# Other solution
def _find_in_different_registers(words: list) -> list:
    """
    returns unique case-sensitive words in lowercase in one instance
    """

    unique_words = set(map(str.lower, words))
    l = len(words)
    for i in range(l):
        lower_word = words[i].lower()
        for j in range(i + 1, l):
            if words[i] == words[j] and lower_word in unique_words:
                unique_words.remove(lower_word)
                break

    return list(unique_words)

'''
words = ['Мама', 'МАМА', 'Мама',
         'папа', 'ПАПА', 'Мама',
         'ДЯдя', 'брАт', 'Дядя',
        'Дядя', 'Дядя']

print(find_in_different_registers(words))
'''

