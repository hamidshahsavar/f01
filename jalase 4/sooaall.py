def wordd (word, ignore=False):
    if ignore == False:
        word = (word.lower())


    uniqet_word = word.split()
    return list(set(uniqet_word))
print(wordd('HI word plz listen', True))



