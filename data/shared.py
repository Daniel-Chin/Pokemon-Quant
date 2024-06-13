import os
from dataclasses import dataclass
import typing as tp
import pickle

try:
    from my_html_parser import ParseContext, UnexpectedEndTag
except ImportError as e:
    module_name = str(e).split('No module named ', 1)[1].strip().strip('"\'')
    if module_name in (
        'my_html_parser', 
    ):
        print(f'Missing module {module_name}. Please download at')
        print(f'https://github.com/Daniel-Chin/Python_Lib')
        input('Press Enter to quit...')
    raise e

os.system('chcp 936')

ALL_TYPES = [*'普火水草电冰斗毒地飞超虫岩鬼龙恶钢妖']

@dataclass(frozen=True)
class PokeAbstract:
    id: str
    name: str
    types: tp.List[str]
    gen: int

def allAbs() -> tp.List[PokeAbstract]:
    with open('abs.pickle', 'rb') as f:
        return pickle.load(f)
