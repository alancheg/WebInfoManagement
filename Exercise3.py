# bitwise AND
# inverted index (倒排索引)
from Exercise1 import word_list
from collections import OrderedDict
import time



class DocMatrix:
    def __init__(self):
        # self._matrix = {}
        pass

    # line1 = d1, line2 = d2, line3 = d3
    @staticmethod
    def doc_id_matrix(matrix1, list1, doc_id):

        for term in list1:
            if term in matrix1.keys():
                matrix1[term][doc_id] += 1
            else:
                matrix1.setdefault(term, [0, 0, 0])
                matrix1[term][doc_id] += 1

    # 输出矩阵
    @staticmethod
    def show_matrix(matrix1):

        first_line = 'term\t' + 'd1\t' + 'd2\t' + 'd3\t'
        print(first_line)
        for key in matrix1:
            str_list = str(key) + ' \t' + str(matrix1[key][0]) + ' \t' + str(matrix1[key][1]) + ' \t' + \
                       str(matrix1[key][1]) + ' \t'
            print(str_list)

    # 全程调用
    @staticmethod
    def search():

        path = "./E1/"
        matrix1 = {}

        for i in range(1, 4):
            file_name = "D" + str(i)
            d_id = i - 1

            DocMatrix.doc_id_matrix(matrix1, word_list(str(open(path + file_name, 'r').read())), doc_id=d_id)

        DocMatrix.show_matrix(matrix1)

        print('------------------------------------------------------')

        keyword = input('请输入关键词:')

        if keyword not in matrix1.keys():
            print('sorry! can`t find the word')
            return False
        else:
            key_list = matrix1[keyword]

            out_str = ''
            for i in range(1, 4):
                if key_list[i - 1] != 0:
                    out_str += 'd' + str(i) + ":" + str(key_list[i - 1]) + ' | '
            print(out_str)

    # 全程调用
    @staticmethod
    def multi_search():

        path = "./E1/"
        matrix1 = {}

        for i in range(1, 4):
            file_name = "D" + str(i)
            d_id = i - 1

            DocMatrix.doc_id_matrix(matrix1, word_list(str(open(path + file_name, 'r').read())), doc_id=d_id)

        DocMatrix.show_matrix(matrix1)

        print('------------------------------------------------------')

        num = input('关键词数目')

        key_list = []
        for i in range(0, int(num)):
            keyword = input('请输入关键词:')
            key_list.append(keyword)

        for keyword in key_list:
            if keyword not in matrix1.keys():
                print('sorry! can`t find the word')
                # return False
            else:
                key_list = matrix1[keyword]

                out_str = ''
                for i in range(1, 4):
                    if key_list[i - 1] != 0:
                        out_str += 'd' + str(i) + ":" + str(key_list[i - 1]) + ' | '
                print(out_str)


def old_func():
    path = "./E1/"

    file_dict = {}
    term_dict = {}
    for i in range(1, 4):

        file_name = "D" + str(i)
        term_list = word_list(str(open(path + file_name, 'r').read()))
        file_dict.setdefault(file_name, term_list)

        for word in term_list:
            if word in term_dict.keys():
                if file_name not in term_dict[word]:
                    term_dict[word].append(file_name)
            else:
                term_dict.setdefault(word, [])
                term_dict[word].append(file_name)

    for key in list(term_dict.keys()):
        out = 'KEY: ' + str(key) + ' DOC ID: ' + str(term_dict[key])
        print(out)


if __name__ == "__main__":
    # old_func()

    matrix = DocMatrix()
    # matrix.search()

    matrix.search()