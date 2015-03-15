__author__ = 'Xiaomin'


import re
import os



def function1():
    path = os.path.abspath('/Users/Xiaomin/Desktop/testproject/superqq/superqq/cs210.txt')
    file = open(path, 'r')

    lines = re.split('\d+', file.read())
    print lines


    path = os.path.abspath('/Users/Xiaomin/Desktop/testproject/superqq/superqq/cs210after.txt')


    wr = open(path, 'wb')
    i = -1
    for line in lines:
        wr.write(str(i) + line + '\n\n\n\n')
        print(str(i) + line + '\n\n\n\n')
        i+=1




def function2():
    path = os.path.abspath('/Users/Xiaomin/Desktop/testproject/superqq/superqq/cs210notes.txt')
    file = open(path, 'r')
    # words = file.read().split()
    # mystr = ''
    # for word in words:
    #     mystr += word + ' '
    # print mystr
    paragraphs = re.split(r'@', file.read())

    #paragraphs = mystr.split(u'\u2022')
    for para in paragraphs:
        print para + '\n'



function2()



