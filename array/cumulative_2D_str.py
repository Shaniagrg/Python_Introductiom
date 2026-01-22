'''
eg: "cow"

ans: [['c','co', 'cow'], ['o', 'ow'], ['w']]
'''


def get_cumulative_str (a:str) -> list[str]:
    store_add:list[list[str]] = []
    if len(a) == 0:
        store_add.append([a])
        return store_add
    else:
        for i in range(len(a)):
            value = ""
            add:list[str] = []
            for j in range(i, len(a)): 
                value = value + a[j]  
                add.append(value)
            store_add.append(add)
              
    return store_add

def addTest(expected:list[list[str]], actual:list[list[str]]) -> str:
    print(actual)
    for i in range(len(expected)):
        if expected[i] == actual[i]:
            return "correct"
        else:
            return "incorrect, addition is wrong"
            

print(addTest([['c','co', 'cow'], ['o', 'ow'], ['w']], get_cumulative_str("cow") ))
print(addTest([['p','pe', 'pen'], ['e', 'en'], ['n']], get_cumulative_str("pen") ))
print(addTest([['']], get_cumulative_str('') ))

#[['']], ('')

