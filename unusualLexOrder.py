def unusualLexOrder(words):
    return sorted(words, key=lambda x:x[::-1])
