#simple way to mix up the letters in a word
#can be used for word games/ puzzles like anograms

def scramble(word):
    return ''.join(sorted(list(word)))
