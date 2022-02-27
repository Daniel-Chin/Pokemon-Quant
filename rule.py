from functools import lru_cache

DOUBLE = "DOUBLE" 
HALF = "HALF" 
IMMUNE = "IMMUNE" 
NORMAL = "NORMAL" 

EFFECT = {
  DOUBLE : 2, 
  HALF : .5, 
  IMMUNE : 0, 
  NORMAL : 1, 
}

@lru_cache(maxsize = 18 * 171)
def doubleRule(offe, defe):
  s =    EFFECT[RULE[offe][defe[0]]]
  try:
    s *= EFFECT[RULE[offe][defe[1]]]
  except IndexError:
    pass
  return s

RULE = dict(
  普 = dict(
    普 = NORMAL , 
    火 = NORMAL , 
    水 = NORMAL , 
    草 = NORMAL , 
    电 = NORMAL , 
    冰 = NORMAL , 
    斗 = NORMAL , 
    毒 = NORMAL , 
    地 = NORMAL , 
    飞 = NORMAL , 
    超 = NORMAL , 
    虫 = NORMAL , 
    岩 = HALF , 
    鬼 = IMMUNE , 
    龙 = NORMAL , 
    恶 = NORMAL , 
    钢 = HALF , 
    妖 = NORMAL , 
  ), 
  火 = dict(
    普 = NORMAL , 
    火 = HALF , 
    水 = HALF , 
    草 = DOUBLE , 
    电 = NORMAL , 
    冰 = DOUBLE , 
    斗 = NORMAL , 
    毒 = NORMAL , 
    地 = NORMAL , 
    飞 = NORMAL , 
    超 = NORMAL , 
    虫 = DOUBLE , 
    岩 = HALF , 
    鬼 = NORMAL , 
    龙 = HALF , 
    恶 = NORMAL , 
    钢 = DOUBLE , 
    妖 = NORMAL , 
  ), 
  水 = dict(
    普 = NORMAL , 
    火 = DOUBLE , 
    水 = HALF , 
    草 = HALF , 
    电 = NORMAL , 
    冰 = NORMAL , 
    斗 = NORMAL , 
    毒 = NORMAL , 
    地 = DOUBLE , 
    飞 = NORMAL , 
    超 = NORMAL , 
    虫 = NORMAL , 
    岩 = DOUBLE , 
    鬼 = NORMAL , 
    龙 = HALF , 
    恶 = NORMAL , 
    钢 = NORMAL , 
    妖 = NORMAL , 
  ), 
  草 = dict(
    普 = NORMAL , 
    火 = HALF , 
    水 = DOUBLE , 
    草 = HALF , 
    电 = NORMAL , 
    冰 = NORMAL , 
    斗 = NORMAL , 
    毒 = HALF , 
    地 = DOUBLE , 
    飞 = HALF , 
    超 = NORMAL , 
    虫 = HALF , 
    岩 = DOUBLE , 
    鬼 = NORMAL , 
    龙 = HALF , 
    恶 = NORMAL , 
    钢 = HALF , 
    妖 = NORMAL , 
  ), 
  电 = dict(
    普 = NORMAL , 
    火 = NORMAL , 
    水 = DOUBLE , 
    草 = HALF , 
    电 = HALF , 
    冰 = NORMAL , 
    斗 = NORMAL , 
    毒 = NORMAL , 
    地 = IMMUNE , 
    飞 = DOUBLE , 
    超 = NORMAL , 
    虫 = NORMAL , 
    岩 = NORMAL , 
    鬼 = NORMAL , 
    龙 = HALF , 
    恶 = NORMAL , 
    钢 = NORMAL , 
    妖 = NORMAL , 
  ), 
  冰 = dict(
    普 = NORMAL , 
    火 = HALF , 
    水 = HALF , 
    草 = DOUBLE , 
    电 = NORMAL , 
    冰 = HALF , 
    斗 = NORMAL , 
    毒 = NORMAL , 
    地 = DOUBLE , 
    飞 = DOUBLE , 
    超 = NORMAL , 
    虫 = NORMAL , 
    岩 = NORMAL , 
    鬼 = NORMAL , 
    龙 = DOUBLE , 
    恶 = NORMAL , 
    钢 = HALF , 
    妖 = NORMAL , 
  ), 
  斗 = dict(
    普 = DOUBLE , 
    火 = NORMAL , 
    水 = NORMAL , 
    草 = NORMAL , 
    电 = NORMAL , 
    冰 = DOUBLE , 
    斗 = NORMAL , 
    毒 = HALF , 
    地 = NORMAL , 
    飞 = HALF , 
    超 = HALF , 
    虫 = HALF , 
    岩 = DOUBLE , 
    鬼 = IMMUNE , 
    龙 = NORMAL , 
    恶 = DOUBLE , 
    钢 = DOUBLE , 
    妖 = HALF , 
  ), 
  毒 = dict(
    普 = NORMAL , 
    火 = NORMAL , 
    水 = NORMAL , 
    草 = DOUBLE , 
    电 = NORMAL , 
    冰 = NORMAL , 
    斗 = NORMAL , 
    毒 = HALF , 
    地 = HALF , 
    飞 = NORMAL , 
    超 = NORMAL , 
    虫 = NORMAL , 
    岩 = HALF , 
    鬼 = HALF , 
    龙 = NORMAL , 
    恶 = NORMAL , 
    钢 = IMMUNE , 
    妖 = DOUBLE , 
  ), 
  地 = dict(
    普 = NORMAL , 
    火 = DOUBLE , 
    水 = NORMAL , 
    草 = HALF , 
    电 = DOUBLE , 
    冰 = NORMAL , 
    斗 = NORMAL , 
    毒 = DOUBLE , 
    地 = NORMAL , 
    飞 = IMMUNE , 
    超 = NORMAL , 
    虫 = HALF , 
    岩 = DOUBLE , 
    鬼 = NORMAL , 
    龙 = NORMAL , 
    恶 = NORMAL , 
    钢 = DOUBLE , 
    妖 = NORMAL , 
  ), 
  飞 = dict(
    普 = NORMAL , 
    火 = NORMAL , 
    水 = NORMAL , 
    草 = DOUBLE , 
    电 = HALF , 
    冰 = NORMAL , 
    斗 = DOUBLE , 
    毒 = NORMAL , 
    地 = NORMAL , 
    飞 = NORMAL , 
    超 = NORMAL , 
    虫 = DOUBLE , 
    岩 = HALF , 
    鬼 = NORMAL , 
    龙 = NORMAL , 
    恶 = NORMAL , 
    钢 = HALF , 
    妖 = NORMAL , 
  ), 
  超 = dict(
    普 = NORMAL , 
    火 = NORMAL , 
    水 = NORMAL , 
    草 = NORMAL , 
    电 = NORMAL , 
    冰 = NORMAL , 
    斗 = DOUBLE , 
    毒 = DOUBLE , 
    地 = NORMAL , 
    飞 = NORMAL , 
    超 = HALF , 
    虫 = NORMAL , 
    岩 = NORMAL , 
    鬼 = NORMAL , 
    龙 = NORMAL , 
    恶 = IMMUNE , 
    钢 = HALF , 
    妖 = NORMAL , 
  ), 
  虫 = dict(
    普 = NORMAL , 
    火 = HALF , 
    水 = NORMAL , 
    草 = DOUBLE , 
    电 = NORMAL , 
    冰 = NORMAL , 
    斗 = HALF , 
    毒 = HALF , 
    地 = NORMAL , 
    飞 = HALF , 
    超 = DOUBLE , 
    虫 = NORMAL , 
    岩 = NORMAL , 
    鬼 = HALF , 
    龙 = NORMAL , 
    恶 = DOUBLE , 
    钢 = HALF , 
    妖 = HALF , 
  ), 
  岩 = dict(
    普 = NORMAL , 
    火 = DOUBLE , 
    水 = NORMAL , 
    草 = NORMAL , 
    电 = NORMAL , 
    冰 = DOUBLE , 
    斗 = HALF , 
    毒 = NORMAL , 
    地 = HALF , 
    飞 = DOUBLE , 
    超 = NORMAL , 
    虫 = DOUBLE , 
    岩 = NORMAL , 
    鬼 = NORMAL , 
    龙 = NORMAL , 
    恶 = NORMAL , 
    钢 = HALF , 
    妖 = NORMAL , 
  ), 
  鬼 = dict(
    普 = IMMUNE , 
    火 = NORMAL , 
    水 = NORMAL , 
    草 = NORMAL , 
    电 = NORMAL , 
    冰 = NORMAL , 
    斗 = NORMAL , 
    毒 = NORMAL , 
    地 = NORMAL , 
    飞 = NORMAL , 
    超 = DOUBLE , 
    虫 = NORMAL , 
    岩 = NORMAL , 
    鬼 = DOUBLE , 
    龙 = NORMAL , 
    恶 = HALF , 
    钢 = NORMAL , 
    妖 = NORMAL , 
  ), 
  龙 = dict(
    普 = NORMAL , 
    火 = NORMAL , 
    水 = NORMAL , 
    草 = NORMAL , 
    电 = NORMAL , 
    冰 = NORMAL , 
    斗 = NORMAL , 
    毒 = NORMAL , 
    地 = NORMAL , 
    飞 = NORMAL , 
    超 = NORMAL , 
    虫 = NORMAL , 
    岩 = NORMAL , 
    鬼 = NORMAL , 
    龙 = DOUBLE , 
    恶 = NORMAL , 
    钢 = HALF , 
    妖 = IMMUNE , 
  ), 
  恶 = dict(
    普 = NORMAL , 
    火 = NORMAL , 
    水 = NORMAL , 
    草 = NORMAL , 
    电 = NORMAL , 
    冰 = NORMAL , 
    斗 = HALF , 
    毒 = NORMAL , 
    地 = NORMAL , 
    飞 = NORMAL , 
    超 = DOUBLE , 
    虫 = NORMAL , 
    岩 = NORMAL , 
    鬼 = DOUBLE , 
    龙 = NORMAL , 
    恶 = HALF , 
    钢 = NORMAL , 
    妖 = HALF , 
  ), 
  钢 = dict(
    普 = NORMAL , 
    火 = HALF , 
    水 = HALF , 
    草 = NORMAL , 
    电 = HALF , 
    冰 = DOUBLE , 
    斗 = NORMAL , 
    毒 = NORMAL , 
    地 = NORMAL , 
    飞 = NORMAL , 
    超 = NORMAL , 
    虫 = NORMAL , 
    岩 = DOUBLE , 
    鬼 = NORMAL , 
    龙 = NORMAL , 
    恶 = NORMAL , 
    钢 = HALF , 
    妖 = DOUBLE , 
  ), 
  妖 = dict(
    普 = NORMAL , 
    火 = HALF , 
    水 = NORMAL , 
    草 = NORMAL , 
    电 = NORMAL , 
    冰 = NORMAL , 
    斗 = DOUBLE , 
    毒 = HALF , 
    地 = NORMAL , 
    飞 = NORMAL , 
    超 = NORMAL , 
    虫 = NORMAL , 
    岩 = NORMAL , 
    鬼 = NORMAL , 
    龙 = DOUBLE , 
    恶 = DOUBLE , 
    钢 = HALF , 
    妖 = NORMAL , 
  ), 
) 

