
#import django environment

import os

import sys

import django

path = os.path.abspath('/Users/Xiaomin/Desktop/testproject/testproject.settings')

sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")

django.setup()





git pull remotetest master       #update and merge from the remote, you must clean your git in your local
https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches
https://help.github.com/articles/fetching-a-remote/
