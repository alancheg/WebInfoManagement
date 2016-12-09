# import os
# D1 = 'I like to watch the sun set with my friend'
# D2 = 'The Best Places To Watch The Sunset'
# D3 = 'My friend watch the sun come up'


# 无视大小写，全部小写
def word_list(seq):

    listofsq = []
    word = ''

    for item in seq:
        if item == ' ' or item == '.':
            # print(item)
            # print(word)
            listofsq.append(word.lower())
            word = ''
        else:
            word += str(item)
    # listofsq.append(word)

    return listofsq


# 严格大小写
def word_list_diff(seq):

    listofsq = []
    word = ''

    for item in seq:
        if item == ' ' or item == '.':
            # print(item)
            # print(word)
            listofsq.append(word)
            word = ''
        else:
            word += str(item)
    # listofsq.append(word)

    return listofsq


def if_only_word():

    print('单词满足，不区分大小写')

    path = './E1/'

    D1str = str(open(path + 'D1', 'r').read())
    # print(D1)
    D2str = str(open(path + 'D2', 'r').read())
    D3str = str(open(path + 'D3', 'r').read())

    D1 = word_list(D1str)
    D2 = word_list(D2str)
    D3 = word_list(D3str)

    a = str(input()).lower()

    ifright = False

    # print(D1)
    # print(D2)
    # print(D3)

    if a in D1:
        print('d1')
        ifright = True

    if a in D2:
        print('d2')
        ifright = True

    if a in D3:
        print('d3')
        ifright = True

    if not ifright:
        print('word not exist')


def if_letter():

    print('只需字符满足，不区分符号')

    path = './E1/'

    D1 = str(open(path + 'D1', 'r').read())
    # print(D1)
    D2 = str(open(path + 'D2', 'r').read())
    D3 = str(open(path + 'D3', 'r').read())

    a = input()

    ifright = False

    if a in D1.lower() or a in D1.upper() or a in D1:
        print('d1')
        ifright = True

    if a in D2.lower() or a in D2.upper() or a in D2:
        print('d2')
        ifright = True

    if a in D3.lower() or a in D3.upper() or a in D3:
        print('d3')
        ifright = True

    if not ifright:
        print('word not exist')


def if_only_word_strict():

    print('严格区分大小写')

    path = './E1/'

    D1str = str(open(path + 'D1', 'r').read())
    # print(D1)
    D2str = str(open(path + 'D2', 'r').read())
    D3str = str(open(path + 'D3', 'r').read())

    D1 = word_list_diff(D1str)
    D2 = word_list_diff(D2str)
    D3 = word_list_diff(D3str)

    a = input()

    ifright = False

    # print(D1)
    # print(D2)
    # print(D3)

    if a in D1 :
        print('d1')
        ifright = True

    if a in D2 :
        print('d2')
        ifright = True

    if a in D3 :
        print('d3')
        ifright = True

    if not ifright:
        print('word not exist')


if __name__ == "__main__":

    # if_letter()
    if_only_word()
    # if_only_word_strict()