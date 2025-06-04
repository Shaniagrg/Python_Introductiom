#dict.pop(key)
bb:dict[str,int] = {'apple': 1,"banana": 2, "carrot":3}
bb.pop('apple')          
print(bb)

#dict.popitem()
bc:dict[str,int] = {'apple': 1,"banana": 2, "carrot":3}
bc.popitem()
print(bc)

#del dict[key]
bd:dict[str,int] = {'apple': 1,"banana": 2, "carrot":3}
del bd['banana']
print(bd)

#dict.clear()
be:dict[str,int] = {'apple': 1,"banana": 2, "carrot":3}
be.clear()
print(be)