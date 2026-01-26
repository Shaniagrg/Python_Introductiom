'''
sort letters according to high letter

eg: "apple"
ans: ["p" , "a", "e" , "l"]

"p" first cuz it has 2 letter
"a", "e" , "l" whichever can come after cuz there's only 1 letter of these alphabet

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
'''
    for key in store_letter:
        if count > store_letter[key]:
            count = store_letter[key]
    print(store_letter)
    return store_letter
'''
    
def highest_letterTest(expected:list[str], actual:list[str]) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, addition is wrong"
    
