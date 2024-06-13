import requests
import csv
import dataclasses

from tqdm import tqdm
import pinyin

from shared import *

ZZ_FIELDS = ('HP', '攻击', '防御', '特攻', '特防', '速度')

def url(pokeAbs: PokeAbstract):
    return 'https://wiki.52poke.com/wiki/' + pokeAbs.name

def getPage(pokeAbs: PokeAbstract):
    response = requests.get(url(pokeAbs))
    assert response.status_code == 200, f'{response.status_code} {response.reason}'
    return response.content.decode('utf-8')

def onePoke(pokeAbs: PokeAbstract):
    results = []
    page = getPage(pokeAbs)
    with open('temp.html', 'w', encoding='utf-8') as f:
        f.write(page)
    parseContext = ParseContext(page, [
        'h3', 'table', 'tr', 'span', 
    ], [
        'class', 
    ])
    while True:
        data = parseContext.seekTagAndConsumeForData('h3')
        if data == ['种族值']:
            break
    while True:
        with parseContext.seekAndEnterTag('table') as table_sentinel:
            try:
                for field_name in ZZ_FIELDS:
                    with parseContext.seekAndEnterTag('tr', class_='bgl-' + field_name):
                        with parseContext.seekAndEnterTag('span'):
                            pass
                        value, = parseContext.seekTagAndConsumeForData('span')
                    results.append(int(value))
            except UnexpectedEndTag as e:
                assert e.sentinel == table_sentinel, (e, table_sentinel)
                continue
            else:
                break
    return results

def main():
    all_abs = {a.name: a for a in allAbs()}
    header = [
        *dataclasses.asdict(next(iter(all_abs.values()))).keys(), 
        'pinyin', 
        *ZZ_FIELDS, 
    ]
    try:
        with open('zz.csv', 'r', encoding='utf-8') as f:
            dReader = csv.DictReader(f)
            acc = 0
            for row in dReader:
                all_abs.pop(row['name'])
                acc += 1
            print('Skipping', acc, 'pokes already scraped.')
    except FileNotFoundError:
        pass
    with open('zz.csv', 'a', encoding='utf-8', newline='') as f:
        dWriter = csv.DictWriter(f, fieldnames=header)
        dWriter.writeheader()
        for name, pokeAbs in tqdm(all_abs.items()):
            zz = onePoke(pokeAbs)
            dWriter.writerow({
                **dataclasses.asdict(pokeAbs),
                **dict(zip(ZZ_FIELDS, zz)),
                'pinyin': pinyin.get(name, format='strip'), 
            })

if __name__ == '__main__':
    main()
