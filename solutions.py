#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercises

# 1: Display the total number of watchers per language (ignore repos w/o a
#    language).

def solution1():
    from urllib.request import urlopen
    from itertools import groupby
    from operator import itemgetter
    from ijson import items

    url2 = 'https://api.github.com/search/repositories?q=data'
    f = urlopen(url2)
    repos = items(f, 'items.item')

    keyfunc = itemgetter('language')
    cleaned = filter(keyfunc, repos)
    records = sorted(cleaned, key=keyfunc)
    grouped = groupby(records, keyfunc)

    for key, group in grouped:
        cnt = sum(g['watchers'] for g in group)
        print(key, cnt)

# 2: Display the language with the most number of watchers, per `owner_type`
#    per `has_pages`.

def solution2(debug=False):
    # Set `debug` to True if you would like to view debugging statements
    from urllib.request import urlopen
    from operator import itemgetter
    from functools import partial
    from pprint import pprint
    from meza import process as pr, fntools as ft
    from meza.io import read_json

    url4 = 'https://api.github.com/search/repositories?q=data&sort=stars&order=desc'
    f = urlopen(url4)
    records = read_json(f, path='items.item')

    # repos without a language have a value of None, which meza doesn't like
    filled = pr.fillempty(records, value='', fields=['language'])
    filled, preview = pr.peek(filled)
    print(preview[0]) if debug else None

    # meza doesn't do well with nested dicts
    flat = (dict(ft.flatten(r)) for r in filled)
    flat, preview = pr.peek(flat)
    print(preview[0]) if debug else None

    # `watchers` is the pivot field to aggregate by
    # `language` is the pivot field to group by
    args = ('watchers', 'language')

    # the pivot fields we want to include in each row
    rows = ['has_pages', 'owner_type']
    pivotted = pr.pivot(flat, *args, rows=rows, op=sum)
    pivotted, preview = pr.peek(pivotted)
    print(preview[0]) if debug else None

    # `rows` are the fields we don't want to normalize (since `invert` is true)
    kwargs = {'rows': rows, 'invert': True}

    # `watchers` is the field to use for the normalized values
    # `language` is the field to use for the normalized key
    normal = pr.normalize(pivotted, *args, **kwargs)
    normal, preview = pr.peek(normal)
    print(preview[0]) if debug else None

    # aggregate by `watchers`
    agg_keyfunc = itemgetter('watchers')

    # group by `has_pages` and `owner_type`
    group_keyfunc = lambda x: tuple(x[r] for r in rows)
    aggregator = partial(max, key=agg_keyfunc)

    # Only emit the groups, not the group key (since `tupled` is False)
    kwargs = {'tupled': False, 'aggregator': aggregator}
    grouped = pr.group(normal, group_keyfunc, **kwargs)
    grouped, preview = pr.peek(grouped)
    print(preview[0]) if debug else None

    sgrouped = sorted(grouped, key=agg_keyfunc, reverse=True)

    for record in sgrouped:
        pprint(record)


if __name__ == "__main__":
    print('-----------')
    print('Solution #1')
    print('-----------')
    solution1()

    print('\n-----------')
    print('Solution #2')
    print('-----------')
    solution2()
