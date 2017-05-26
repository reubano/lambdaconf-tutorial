#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercises

# 1: Display the total number of watchers per language (ignore repos w/o a
#    language). Your output should look something like this:

"""
C# 32
C++ 63
HTML 349
JavaScript 3881
Jupyter Notebook 5481
PHP 201
Python 37007
R 18
"""

# Use the url `https://api.github.com/search/repositories?q=data` for source
# data.

# Your answer
def solution1():
    print('Edit me!')

# Hint
# View meza
from urllib.request import urlopen
from itertools import groupby
from operator import itemgetter
from ijson import items

url2 = 'https://api.github.com/search/repositories?q=data'
f = '???'
repos = '???'

# ...

kwargs = {}
grouped = groupby([], **kwargs)

for key, group in grouped:
    cnt = '???'
    print(key, cnt)

# 2: Display the language with the most number of watchers, per `owner_type`
#    per `has_pages`. Your output should look something like this:

"""
{'has_pages': True,
 'language': 'JavaScript',
 'owner_type': 'Organization',
 'watchers': 128605}
"""

# Use the url `https://api.github.com/search/repositories?q=data` for source
# data.

# Your answer
def solution2():
    print('Edit me!')

# Hint
from urllib.request import urlopen
from operator import itemgetter
from functools import partial
from meza import process as pr, fntools as ft
from meza.io import read_json

url4 = 'https://api.github.com/search/repositories?q=data&sort=stars&order=desc'
f = '???'
records = '???'

# Some of the functions you will use are `ft.flatten`, `pr.pivot`, `pr.normalize`
# `pr.group`, `pr.fillempty`, and `pr.aggregate`. You can view documentation for
# these functions in the doc-blocks at the links below:
#
# https://github.com/reubano/meza/blob/master/meza/process.py
# https://github.com/reubano/meza/blob/master/meza/fntools.py

# ...

keyfunc = lambda x: True
kwargs = {}
grouped = pr.group([], keyfunc, **kwargs)

for key, group in grouped:
    # ...
    pass

if __name__ == "__main__":
    print('-----------')
    print('Solution #1')
    print('-----------')
    solution1()

    print('\n-----------')
    print('Solution #2')
    print('-----------')
    solution2()
