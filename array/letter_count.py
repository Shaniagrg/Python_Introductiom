'''
return each letter count

eg: "hello"

ans = h:1 e:1 l:2 o:1
'''

def highest_letter (a:str) -> list[str]:
    store_letter:dict[str,int] = {}
    
    if len(a) == 0:
        store_letter[a] = 0
        print(store_letter)
        return store_letter
    
    else:
        for i in range(len(a)):
            if a[i] in store_letter:
                store_letter[a[i]] = store_letter[a[i]] + 1
            else:
                store_letter[a[i]] = 1
       
    print(store_letter)
    return store_letter


    
def highest_letterTest(expected:dict[str,int], actual:dict[str,int]) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, addition is wrong"
    
print(highest_letterTest({'h':1, 'e':1, 'l':2, 'o':1},highest_letter("hello")))
print(highest_letterTest({'':0},highest_letter('')))
