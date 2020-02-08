'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, index=0):
    target = "th"
    instances = 0
    index = 0
    # If string len = 0 return 0
    if word == "":
        return instances
    elif target in word and index <= len(word):
        index = word.find(target, index) + 2
        new_word = word[index:]
        instances += 1
        return instances + count_th(new_word, index)
    # If string does not contain substring return 0
    else:
        return instances
