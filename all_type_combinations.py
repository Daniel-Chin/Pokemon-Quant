from functools import lru_cache
from allPokes import allPokes
from rule import doubleRule

ALL_TYPES = '普火水草电冰斗毒地飞超虫岩鬼龙恶钢妖'

class TypeCombination:
    def __init__(self, type_tuple) -> None:
        self.type_tuple = type_tuple
        self.high_score = 0
        self.high_score_who = None
        self.total_score = 0
        self.pokes = set()
    
    def __repr__(self):
        s = "".join(self)
        if len(self) == 1:
            s += '  '
        return f'<{s}={round(self.high_score)}:{self.high_score_who}>'
    
    def __hash__(self):
        return hash(self.type_tuple)
    def __len__(self):
        return len(self.type_tuple)
    def __iter__(self):
        return iter(self.type_tuple)
    def __getitem__(self, i):
        return self.type_tuple[i]
    def __lt__(self, other):
        return self.type_tuple < other.type_tuple
    def __eq__(self, other):
        return self.type_tuple == other.type_tuple
    
    def learnAbout(self, poke):
        poke_id = poke['#']
        assert poke_id not in self.pokes
        self.pokes.add(poke_id)
        score = poke['综合分']
        if self.high_score < score:
            self.high_score = score
            self.high_score_who = poke['宝可梦']
        self.total_score += score
    
    @lru_cache(1)
    def hasQuadWeakness(self):
        for t in ALL_TYPES:
            if doubleRule(t, self) == 4:
                return True
        return False

@lru_cache()
def allTypeCombinations():
    all_p = allPokes()
    s = {}
    for poke in all_p.values():
        type_tuple = poke['type']
        try:
            typeCombination = s[type_tuple]
        except KeyError:
            typeCombination = TypeCombination(type_tuple)
            s[type_tuple] = typeCombination
        typeCombination.learnAbout(poke)
    return sorted([*s.values()])

@lru_cache(len(allTypeCombinations()))
def TcsDoubleTo(defe) -> set:
    s = set()
    for offe in allTypeCombinations():
        is_weak = False
        for t in offe:
            if doubleRule(t, defe) >= 2:
                is_weak = True
        if is_weak:
            s.add(offe)
    return s

@lru_cache(len(allTypeCombinations()))
def TypesDoubleTo(defe) -> set:
    s = set()
    for t in ALL_TYPES:
        if doubleRule(t, defe) >= 2:
            s.add(t)
    return s

@lru_cache(18)
def strongTo(t) -> set:
    s = set()
    for defe in allTypeCombinations():
        if doubleRule(t, defe) >= 2:
            s.add(defe)
    return s

def sumTcScores(set_of_tcs):
    return sum([x.total_score for x in set_of_tcs])

if __name__ == '__main__':
    from os import system
    system('chcp 936')
    for tc in allTypeCombinations():
        print(tc)
    print('total:', len(allTypeCombinations()))
