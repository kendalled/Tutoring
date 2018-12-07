alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def word_rank(txt):
    work = txt.split(' ')
    word_scores = []
    for i in work:
        word_scores.append(score_word(i))
    ind = work.index(max(word_scores))
    print(work[ind])


def score_word(word):
    res = 0
    temp = [*word]
    for i in temp:
        if(i in alphabet):
            res += (alphabet.index(i) + 1)
    return res
