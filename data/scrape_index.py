import requests
import typing as tp
from itertools import count
import pickle

from chinese_converter import to_simplified

from shared import *

URL = 'https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89'

CACHE_INDEX = 'cache_index.html'

TYPE_CAST = {
    **{t: t for t in ALL_TYPES},
    '[[{{{6}}}（属性）|{{{6}}}]]': None, 
    '一般': '普',
    '飞行': '飞',
    '超能力': '超',
    '地面': '地',
    '妖精': '妖',
    '格斗': '斗',
    '岩石': '岩',
    '幽灵': '鬼',
}

def getPage():
    try:
        with open(CACHE_INDEX, 'rb') as f:
            content = f.read()
        print('Cache found. Use? Y/N')
        if input().lower() != 'y':
            raise FileNotFoundError
    except FileNotFoundError:
        print('Getting page...')
        response = requests.get(URL)
        print('Got page.')
        assert response.status_code == 200, f'{response.status_code} {response.reason}'
        content = response.content
        with open(CACHE_INDEX, 'wb') as f:
            f.write(content)
    return content

class BadRow(Exception): pass

def main():
    parseContext = ParseContext(getPage().decode('utf-8'), [
        'h2', 'table', 'tr', 'td', 
    ], [
        'class', 
    ])
    def parseRow(gen: int):
        with parseContext.seekAndEnterTag('tr') as tr_sentinel:
            try:
                poke_id, = parseContext.seekTagAndConsumeForData('td', class_='rdexn-id')
                assert poke_id.startswith('#'), poke_id
                poke_id = poke_id[1:].strip()
                # print(f'{poke_id = }')
                poke_name,  = parseContext.seekTagAndConsumeForData('td', class_='rdexn-name')
                # print(f'{poke_name = }')
                poke_types = [
                    TYPE_CAST[to_simplified(parseContext.seekTagAndConsumeForData(
                        'td', class_=f'rdexn-type{i}', 
                    )[0])] 
                    for i in (1, 2)
                ]
                poke_types = [t for t in poke_types if t is not None]
                for type_ in poke_types:
                    assert type_ in ALL_TYPES, repr(type_)
            except UnexpectedEndTag as e:
                assert e.sentinel == tr_sentinel, (e, tr_sentinel)
                raise BadRow()
        return PokeAbstract(poke_id, poke_name, poke_types, gen)

    allAbs: tp.List[PokeAbstract] = []
    for gen in count(1):
        try:
            h2, = parseContext.seekTagAndConsumeForData('h2')
        except StopIteration:
            break
        if not (h2.startswith('第') and h2.endswith('世代宝可梦')):
            print('Warning! Invalid <h2>:', h2)
            continue
        print('Using id', gen, 'for', h2)
        with parseContext.seekAndEnterTag('table') as table_sentinel:
            in_heading = True
            while True:
                try:
                    pokeAbs = parseRow(gen)
                except UnexpectedEndTag as e:
                    assert e.tag == 'table', e
                    assert e.sentinel == table_sentinel, (e, table_sentinel)
                    break
                except BadRow:
                    if in_heading:
                        # print('bad row in heading')
                        continue
                    raise
                else:
                    in_heading = False
                    allAbs.append(pokeAbs)
                    # print(pokeAbs)
    
    with open('abs.pickle', 'wb') as f:
        pickle.dump(allAbs, f)
    
    print('ok')

if __name__ == '__main__':
    main()
