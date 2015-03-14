__author__ = 'Xiaomin'








import os
path = os.path.abspath('/Users/Xiaomin/Desktop/testproject/superqq/superqq/cs210.txt')
file = open(path, 'r')
import re

lines = re.split('\d+', file.read())
print lines


path = os.path.abspath('/Users/Xiaomin/Desktop/testproject/superqq/superqq/cs210after.txt')


wr = open(path, 'wb')
i = -1
for line in lines:
    wr.write(str(i) + line + '\n\n\n\n')
    print(str(i) + line + '\n\n\n\n')
    i+=1








