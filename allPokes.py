from functools import lru_cache
import pandas as pd

@lru_cache()
def allPokes():
    with open('data/all_pokes.xlsx', 'rb') as f:
        excel = pd.read_excel(f)
    all_pokes = {}
    for _, series in excel.iterrows():
        series = series.iteritems()
        key, value = next(series)
        assert key == '#'
        poke = {key: value}
        all_pokes[value] = poke
        for key, value in series:
            poke[key] = value
        assert len(poke['type']) < 11
        poke['type'] = eval(poke['type'])
    return all_pokes

@lru_cache()
def allPokesTotalScore():
    acc = 0
    for poke in allPokes().values():
        acc += poke['综合分']
    return acc

if __name__ == '__main__':
    from os import system
    system('chcp 936')
    from pprint import pprint
    pprint(allPokes()[149])
