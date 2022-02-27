THRESHOLD = 100

from functools import lru_cache
from allPokes import allPokes
from rule import doubleRule

ALL_TYPES = '普火水草电冰斗毒地飞超虫岩鬼龙恶钢妖'

class TypeCombination(tuple):
    def __repr__(self):
        name, score = typeCombinationBestScore(self)
        s = "".join(self)
        if len(self) == 1:
            s += '  '
        return f'<{s}={score}:{name}>'

@lru_cache()
def allTypeCombinations():
    all_p = allPokes()
    s = set()
    for poke in all_p.values():
        if int(poke['综合分']) >= THRESHOLD:
            s.add(TypeCombination(poke['type']))
    return sorted([*s])

@lru_cache(171)
def typeCombinationBestScore(tc):
    highscore = 0
    name = None
    for poke in allPokes().values():
        score = int(poke['综合分'])
        if score < highscore:
            continue
        if poke['type'] == tc:
            highscore = score
            name = poke['宝可梦']
    return name, highscore

@lru_cache(len(allTypeCombinations()))
def weakTo(defe) -> set:
    s = set()
    for offe in allTypeCombinations():
        is_weak = False
        for t in offe:
            if doubleRule(t, defe) >= 2:
                is_weak = True
        if is_weak:
            s.add(offe)
    return s

if __name__ == '__main__':
    print(len(allTypeCombinations()))
