
#import django environment

import os

import sys

import django

path = os.path.abspath('/Users/Xiaomin/Desktop/testproject/testproject.settings')

sys.path.append(os.path.abspath(os.path.join(path, os.path.pardir)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")

django.setup()
