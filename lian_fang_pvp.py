'''
For PVP. 
'''
from os import system
system('chcp 936')
import pickle
import csv
from itertools import combinations
from scipy.special import comb
from softmax import softmax, softmin
from keepTop import KeepTop
from graphic_terminal import printTable
from allPokes import allPokesTotalScore
from all_type_combinations import allTypeCombinations, TcsDoubleTo
from jdt import jdtIter

HOW_MANY = 5

def sumScores(tc_set):
    acc = 0
    for tc in tc_set:
        acc += tc.total_score
    return acc

def main():
    # with open('ex_safety_2.pickle', 'rb') as f:
    #     ex_safety = pickle.load(f)
    keepTop = KeepTop(200, lambda x : x[HOW_MANY + 1] - x[HOW_MANY] * .5)
    n_all_tc = len(allTypeCombinations())
    for team in jdtIter(combinations(
        allTypeCombinations(), HOW_MANY, 
    ), UPP = 1024, goal = comb(n_all_tc, HOW_MANY, exact=True)):
        losses = []
        for offe in allTypeCombinations():
            can_stand = 0
            for defe in team:
                if offe not in TcsDoubleTo(defe):
                    can_stand += 1
            losses.append((
                (HOW_MANY - can_stand) / HOW_MANY, 
                offe.total_score, 
            ))
        loss = softmax(losses, .001)
        score = softmin(
            [x.high_score for x in team], 
            coldness = .0001, 
        )
        keepTop.eat((
            *team, 
            loss, 
            score, 
            # ex_safety[team], 
        ))
    header = [f'宝可梦 {x}' for x in range(1, HOW_MANY + 1)]
    header += ['防盲', '综分']
    formatter = [None] * HOW_MANY
    formatter += [round, round]
    with open('lianfang_6.csv', 'w', encoding='utf-8', newline='') as f:
        c = csv.writer(f)
        c.writerow(header)
        c.writerows(keepTop.getList())
    printTable(
        keepTop.getList(), 
        header = header, 
        formatter = formatter, 
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
