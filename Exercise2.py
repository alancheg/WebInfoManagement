import requests
# import re


# 查找元素，返回的是匹配的信息，或者是False
def find_elements(element_name, match_line):

    # count = len(element_name)
    list = []
    content = ''
    start = False

    if element_name in match_line:
        # content = ''
        for item in match_line:
            if item == '"' and content == '':
                start = True
            elif item != '"' and start == True:
                content += item
            elif item == '"' and content != '':
                list.append(content)
                content = ''

    if len(list) == 0:
        return None
    else:
        return list


def find_title(this_content):

    title = ''
    start = False

    # print('this content')
    # print(this_content)

    for match_line in this_content.splitlines():

        # print('match_line')
        # print(match_line)
        # print('----------------------')

        if '<title>' in match_line:

            # print('match_line')
            # print(match_line)
            # print('----------------------')

            for item in match_line:
                if item == '>' and title == '':
                    start = True
                elif item != '<' and start == True:
                    title += item
                elif item == '<' and title != '':
                    return title

    return None


if __name__ == "__main__":

    seed_url = 'http://english.whut.edu.cn/'

    hyperlinks = []

    response = requests.get(seed_url)
    content = response.text

    # print('now content')
    # print(content)

    element_name = 'href'
    for line in content.splitlines():
        # match = pattern.match(line)
        # if match:
        #     print(match.group())

            # print(content)

        # print('now line')
        # print(line)

        if find_elements(element_name, line) is not None:
            url_list = find_elements(element_name, line)
            for item in url_list:
                hyperlinks.append(item)

    # for item in hyperlinks:
    #     print('url ')
    #     print(item )

    content_element = 'title'

    print('网址数目')
    print(len(hyperlinks))

    useful_count = 0
    for url in hyperlinks:

        if 'http' not in url:
            now_url = seed_url + str(url).replace('./', '/')
            # print(now_url)
        else:
            now_url = url

        url_content = requests.get(now_url).text

        # print('new_content')
        # print(url_content)

        if find_title(url_content) is not None:

            print('当前的网址为：')
            print(now_url)
            print('当前的网址标题为：')
            print(find_title(url_content))
            print('----------------------------')
            useful_count += 1

    print('count ')
    print(useful_count)