from Exercise1 import word_list


def generate_dict():
    path = "./E1/"

    file_dict = {}
    term_dict = {}
    # dict_list = []


    for i in range(1, 4):

        file_name = "D" + str(i)
        term_list = word_list(str(open(path + file_name, 'r').read()))
        print(term_list)
        file_dict.setdefault(file_name, term_list)

        for word in term_list:
            if word in term_dict.keys():
                if file_name not in term_dict[word]:
                    term_dict[word].append(file_name)
            else:
                term_dict.setdefault(word, [])
                term_dict[word].append(file_name)

    print(file_dict)
    return file_dict


def and_query(file_dict):

    x = input('please input x: ')
    y = input('please input y: ')

    answer = []
    if x is not None and y is not None:
        for key in file_dict.keys():
            if x in file_dict[key] and y in file_dict[key]:
                answer.append(str(key))

    if answer == []:
        print('no answer')
    else:
        print(answer)

def and_not_query(file_dict):

    x = input('please input x: ')
    y = input('please input y: ')
    z = input('please input z: ')


    answer = []
    if x is not None and y is not None and z is not None:
        for key in file_dict.keys():
            if x in file_dict[key] and y in file_dict[key] and z not in file_dict[key]:
                answer.append(str(key))

    if answer == []:
        print('no answer')
    else:
        print(answer)



if __name__ == '__main__':

    file_dict = generate_dict()
    print('and query')
    print('include x and y')
    and_query(file_dict)

    print('and not query')
    print('include x and y and not include z')
    and_not_query(file_dict)