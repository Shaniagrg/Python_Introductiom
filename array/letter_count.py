'''
return each letter count

eg: "hello"

ans = h:1 e:1 l:2 o:1
'''

def highest_letter (a:str) -> list[str]:
    letter:str =  ""
    count:int = 0
    store_letter:dict[str,int] = {}
    
    if len(a) == 0:
        store_letter[a] = count
        print(store_letter)
        return store_letter
    
    else:
        for i in range(len(a)):
            letter = a[i]
            count = 0
            
            for each_letter_index in range(len(a)):
                if letter == a[each_letter_index]:
                    count = count + 1
            store_letter[letter] = count

    print(store_letter)
    return store_letter
    
def highest_letterTest(expected:dict[str,int], actual:dict[str,int]) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, addition is wrong"
    
print(highest_letterTest({'h':1, 'e':1, 'l':2, 'o':1},highest_letter("hello")))
print(highest_letterTest({'':0},highest_letter('')))
