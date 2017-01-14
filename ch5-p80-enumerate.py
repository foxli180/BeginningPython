#-*-coding:utf-8-*- #中文
strings = ['Hello','Helly','Test','Hi']
for index, string in enumerate(strings): #enumerate 返回所有的序号和子串
    if 'll' in string:
        strings[index] = 'Fox'
for index, string in enumerate(strings):
    print index, string
    