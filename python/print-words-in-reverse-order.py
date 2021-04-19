def print_reverse_words_in_sent(sent):
    print(sent)
    return [word[::-1] for word in sent.split(' ')]

print(print_reverse_words_in_sent('This is my house'))
