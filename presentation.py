# -*- coding: utf-8 -*-

# Presentation

## Naive

"""Reading data
    >>> from urllib.request import urlopen
    >>> from json import loads
    >>>
    >>> BASE = 'https://api.github.com/search'
    >>> _url1 = '{}/repositories?q={}'
    >>> q = 'data&per_page=100'
    >>> url1 = _url1.format(BASE, q)
    >>> f = urlopen(url1)
    >>> data = loads(f.read().decode('utf-8'))
    >>> repos = data['items']
    >>> repos[0]['description']
    'Data and code behind the stories and interactives at FiveThirtyEight'

    >>> repos[0]['full_name']
    'fivethirtyeight/data'
"""

"""Processing data
    >>> def rate(repos):
    ...     rated = []
    ...
    ...     for repo in repos:
    ...         rated.append(repo['watchers'] * 2)
    ...
    ...     return rated
    >>> rate(repos)[:5]
    [11142, 5556, 396, 438, 128]

    >>> # Infinite data
    >>> from itertools import count
    >>>
    >>> inf_repos = ({'watchers': c} for c in count())
    >>> # Don't actually run the below code since it will hang forever
    >>> # rate(inf_repos)
    >>>
    >>> # Expensive data
    >>> from time import sleep
    >>>
    >>> def exp_rate(repos):
    ...     rated = []
    ...
    ...     for repo in repos:
    ...         sleep(1)
    ...         rated.append(repo['watchers'] * 2)
    ...
    ...     return rated
    >>>
    >>> exp_rate(repos)[:5]
    [11142, 5556, 396, 438, 128]
"""

## Lazy evaluation

"""
    >>> eager_list = list(range(5))
    >>> eager_list
    [0, 1, 2, 3, 4]

    >>> lazy_list = iter(eager_list)
    >>> lazy_list
    <list_iterator at 0x10f97bcc0>

    >>> next(lazy_list)
    0

    >>> list(lazy_list)
    [1, 2, 3, 4]

    >>> next(lazy_list)
    ---------------------------------------------------------------------------
    StopIteration                             Traceback (most recent call last)
    <ipython-input-16-898b6387b693> in <module>()
    ----> 1 next(lazy_list)

    StopIteration:
"""

"""Reading data
    >>> from ijson import items
    >>>
    >>> f = urlopen(url1)
    >>> repos = items(f, 'items.item')
    >>> repos
    <generator object items at 0x10f9677d8>

    >>> repo = next(repos)
    >>> repo['full_name']
    'fivethirtyeight/data'
"""

"""Processing data
    >>> def gen_rates(repos):
    ...     for repo in repos:
    ...         yield repo['watchers'] * 2
    >>>
    >>> gen_rates(repos)
    <generator object gen_rates at 0x10f98d048>

    >>> rates = gen_rates(repos)
    >>> next(rates)
    5556

    >>> next(rates)
    396

    >>> # Infinite data
    >>> rates = gen_rates(inf_repos)
    >>> next(rates)
    0

    >>> # Expensive data
    >>> def gen_exp_rates(repos):
    ...     for repo in repos:
    ...         sleep(1)
    ...         yield repo['watchers'] * 2

    >>> from itertools import islice
    >>>
    >>> rates = gen_exp_rates(repos)
    >>> result = islice(rates, 5)
    >>> list(result)
    [438, 128, 684, 348, 1356]

    >>> next(rates)
    648
"""

## Grouping data

"""
    >>> f = urlopen(url1)
    >>> repos = items(f, 'items.item')
    >>> repo = next(repos)
    >>> repo.keys()
    dict_keys(['id', 'name', 'full_name', 'owner', ...]

    >>> repo['has_issues']
    True

    >>> import itertools as it
    >>> from operator import itemgetter
    >>>
    >>> keyfunc = itemgetter('has_issues')
    >>> sorted_repos = sorted(repos, key=keyfunc)
    >>> grouped = it.groupby(sorted_repos, keyfunc)
    >>> data = ((key, len(list(group))) for key, group in grouped)
    >>> next(data)
    (False, 3)

    >>> next(data)
    (True, 96)
"""

## Memoization

"""Processing data
    >>> def calc_rate(watchers):
    ...     sleep(1)
    ...     return watchers * 2
    >>>
    >>> def gen_exp_rates(repos):
    ...     for repo in repos:
    ...         yield calc_rate(repo['watchers'])
    >>>
    >>> repos = it.repeat({'watchers': 5})
    >>> rates = gen_exp_rates(repos)
    >>> result = islice(rates, 5)
    >>> list(result)
    [10, 10, 10, 10, 10]

    >>> from functools import lru_cache
    >>>
    >>> def _calc_rate(watchers):
    ...     sleep(1)
    ...     return watchers * 2
    >>>
    >>> cacher = lru_cache()
    >>> calc_rate = cacher(_calc_rate)
    >>>
    >>> def gen_exp_rates(repos):
    ...     for repo in repos:
    ...         yield calc_rate(repo['watchers'])
    >>>
    >>> repos = it.repeat({'watchers': 5})
    >>> rates = gen_exp_rates(repos)
    >>> result = islice(rates, 5)
    >>> list(result)
    [10, 10, 10, 10, 10]

    >>> @lru_cache()
    ... def calc_rate(watchers):
    ...     sleep(1)
    ...     return watchers * 2
    >>>
    >>> def gen_exp_rates(repos):
    ...     for repo in repos:
    ...         yield calc_rate(repo['watchers'])
    >>>
    >>> repos = it.repeat({'watchers': 5})
    >>> rates = gen_exp_rates(repos)
    >>> result = islice(rates, 5)
    >>> list(result)
    [10, 10, 10, 10, 10]
"""

## Introducing meza

"""Reading data
    >>> from urllib.request import urlopen
    >>> from meza.io import read_json
    >>>
    >>> url2 = '{}/repositories?q=data'.format(BASE)
    >>> f = urlopen(url2)
    >>> records = read_json(f, path='items.item')
    >>> repo = next(records)
    >>> repo['full_name']
    'fivethirtyeight/data'

    >>> len(list(records))
    29

    >>> from io import StringIO
    >>> from meza.io import read_csv
    >>>
    >>> f = StringIO('greeting,location\nhello,world\n')
    >>> next(read_csv(f))
    {'greeting': 'hello', 'location': 'world'}

    >>> from os import path as p
    >>> from meza.io import join
    >>>
    >>> url3 = '{}&page=2'.format(url2)
    >>> files = map(urlopen, [url2, url3])
    >>> records = join(*files, ext='json', path='items.item')
    >>> repo = next(records)
    >>> repo['full_name']
    'fivethirtyeight/data'

    >>> repo['language']
    'Jupyter Notebook'

    >>> len(list(records))
    59
"""

"""Transforming data
    >>> from meza.process import merge
    >>>
    >>> records = [{'a': 200}, {'b': 300}, {'c': 400}]
    >>> merge(records)
    {'a': 200, 'b': 300, 'c': 400}

    >>> from meza.process import group
    >>>
    >>> records = [
    ...     {'item': 'a', 'amount': 200},
    ...     {'item': 'a', 'amount': 200},
    ...     {'item': 'b', 'amount': 400}]
    >>>
    >>> grouped = group(records, 'item')
    >>> key, _group = next(grouped)
    >>> key
    'a'

    >>> _group
    [{'amount': 200, 'item': 'a'}, {'amount': 200, 'item': 'a'}]

    >>> from meza import process as pr
    >>>
    >>> f = urlopen(url2)
    >>> raw = read_json(f, path='items.item')
    >>> fields = ['full_name', 'language', 'watchers', 'score', 'has_wiki']
    >>> cut = pr.cut(raw, fields)
    >>> cut
    <generator object cut.<locals>.<genexpr> at 0x11020ae08>

    >>> cut, preview = pr.peek(cut)
    >>> cut
    <itertools.chain at 0x11025f4a8>

    >>> len(preview)
    5

    >>> preview[0]
    {'full_name': 'fivethirtyeight/data',
     'has_wiki': True,
     'language': 'Jupyter Notebook',
     'score': Decimal('120.396454'),
     'watchers': 5572}

    >>> filled = pr.fillempty(raw, value='', fields=['language'])
    >>> pivoted = pr.pivot(filled, 'score', 'language', rows=['has_wiki'], op=min)
    >>> next(pivoted)
    {'HTML': Decimal('73.19426'),
     'JavaScript': Decimal('54.46375'),
     'Python': Decimal('50.188396'),
     'has_wiki': False}

    >>> next(pivoted)
    {'': Decimal('44.635494'),
     'C#': Decimal('47.918125'),
     'HTML': Decimal('68.96914'),
     'JavaScript': Decimal('44.16988'),
     'PHP': Decimal('44.0172'),
     'Python': Decimal('44.73296'),
     'R': Decimal('45.959583'),
     'has_wiki': True}
"""
