from os import system
system('chcp 936')
import csv
from functools import lru_cache
import pickle

blacklist = [
    '超梦', 
    '梦幻', 
    '洛奇亚', 
    '凤王', 
    '时拉比', 
    '盖欧卡', 
    '固拉多', 
    '烈空坐', 
    '基拉祈', 
    '代欧奇希斯', 
    '洛托姆', 
    '帝牙卢卡', 
    '帕路奇亚', 
    '骑拉帝纳', 
    '霏欧纳', 
    '玛纳霏', 
    '达克莱伊', 
    '谢米', 
    '阿尔宙斯', 
    '拉帝亚斯', 
    '拉帝欧斯', 
    '皮丘', 
]

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
            if line['宝可梦'] in blacklist:
                blacklist.remove(line['宝可梦'])
                continue
            s[i] = line
    if blacklist:
        print('unused blacklist:', blacklist)
    with open('all_pokes.pickle', 'wb') as f:
        pickle.dump(s, f)
    print(len(s))

main()
