import csv
from functools import lru_cache
import pickle

ALL_TYPES = '普火水草电冰斗毒地飞超虫岩鬼龙恶钢妖'
MAP = {
    '一般' : '普', 
    '格斗' : '斗', 
    '地面' : '地', 
    '飞行' : '飞', 
    '超能力' : '超', 
    '岩石' : '岩', 
    '幽灵' : '鬼', 
    '妖精' : '妖', 
}

@lru_cache()
def mapType(x):
    if not x:
        return None
    try:
        y = MAP[x]
    except KeyError:
        y = x
    assert y in ALL_TYPES
    return y

@lru_cache()
def sequentialize(t0, t1):
    if ALL_TYPES.index(t0) < ALL_TYPES.index(t1):
        return ( t0, t1 )
    else:
        return ( t1, t0 )

def main():
    t_map = {}
    with open('51_types.csv', 'r', encoding='utf-8') as f:
        c = csv.DictReader(f)
        for line in c:
            i = line['id']
            if i:
                i = int(i.lstrip('#'))
                t0 = mapType(line['t0'])
                t1 = mapType(line['t1'])
                if t1 is None:
                    t = ( t0, )
                else:
                    t = sequentialize(t0, t1)
                t_map[i] = t
    s = {}
    with open('51_database.csv', 'r', encoding='utf-8') as f:
        c = csv.DictReader(f)
        for line in c:
            i = int(line['#'])
            try:
                line['type'] = t_map[i]
            except KeyError:
                continue
            s[i] = line
    with open('all_pokes.pickle', 'wb') as f:
        pickle.dump(s, f)
    print(len(s))

main()
