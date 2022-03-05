from os import system
system('chcp 936')
import pickle
from softmax import softmin
from graphic_terminal import printTable
from allPokes import allPokesTotalScore
from all_type_combinations import allTypeCombinations, TcsDoubleTo
from jdt import jdtIter

def sumScores(tc_set):
    acc = 0
    for tc in tc_set:
        acc += tc.total_score
    return acc

def main():
    with open('ex_safety.pickle', 'rb') as f:
        ex_safety = pickle.load(f)
    s = []
    n_all_tc = len(allTypeCombinations())
    for a_i in jdtIter(range(n_all_tc), UPP = 4):
        a = allTypeCombinations()[a_i]
        if a.hasQuadWeakness():
            continue
        for b_i in range(a_i + 1, n_all_tc):
            b = allTypeCombinations()[b_i]
            if b.hasQuadWeakness():
                continue
            for c_i in range(b_i + 1, n_all_tc):
                c = allTypeCombinations()[c_i]
                if c.hasQuadWeakness():
                    continue
                loss = 0
                a_w = TcsDoubleTo(a)
                b_w = TcsDoubleTo(b)
                c_w = TcsDoubleTo(c)
                ab_w = a_w.intersection(b_w)
                loss += sumScores(ab_w)
                loss += sumScores(a_w.intersection(c_w))
                loss += sumScores(b_w.intersection(c_w))
                # loss /= allPokesTotalScore()
                common_w = ab_w.intersection(c_w)
                score = softmin((
                    a.high_score,
                    b.high_score,
                    c.high_score,
                ), coldness = .1)
                team = tuple(sorted((a, b, c)))
                s.append((
                    *team, 
                    loss, 
                    score, 
                    ex_safety[team], 
                    common_w, 
                ))
    s.sort(
        reverse = True, 
        # key = lambda x : x[2] * (1 - x[1] * 10), 
        key = lambda x : (x[4] - x[3] * .5) / x[5], 
    )
    printTable(
        s[:80], 
        header=[
            '宝可梦 1', '宝可梦 2', '宝可梦 3', 
            '防盲', '综分', '替换', '', 
        ], 
        formatter=[
            None, 
            None, 
            None, 
            # lambda x : format(x, '02.2%'), 
            round, 
            round, 
            lambda x : format(x, '4.0%'), 
            lambda x : len(x) if x else '', 
        ], 
        delimiter = ' ', padding = 0, 
    )
    # for team, loss, common_w in s[:20]:
    #     buffer = [*team, round(loss)]
    #     if common_w:
    #         buffer.append('团灭 from')
    #         buffer.append(common_w)
    #     print(*buffer)
    #     print()

main()
