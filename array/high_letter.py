'''
sort letters according to high letter

eg: "apple"
ans: ["p" , "a", "e" , "l"]

"p" first cuz it has 2 letter
"a", "e" , "l" whichever can come after cuz there's only 1 letter of these alphabet

'''

def highest_letter (a:str) -> list[str]:
    
    store_letter:dict[str,int] = {}
    store_count:list[int] = []
    rearrange_letter:list[str] = []
    added_letters:list[str] = set()
    
    if len(a) == 0:
        rearrange_letter.append(a)
        print(rearrange_letter)
        return rearrange_letter
    
    else:
        for i in range(len(a)):
            if a[i] in store_letter:
                store_letter[a[i]] = store_letter[a[i]] + 1
            else:
                store_letter[a[i]] = 1
    
    for value in store_letter.values():
        store_count.append(value)
    
    print(store_letter)
    store_count = sorted(store_count, reverse=True)
    print(store_count)
    
    for i in store_count:
        for key,value in store_letter.items():
            if value == i and key not in added_letters:
                rearrange_letter.append(key)
                added_letters.add(key)
   
    print(rearrange_letter)
    return rearrange_letter
     
     
def highest_letterTest(expected:list[str], actual:list[str]) -> str:
    if expected == actual:
        return "correct"

    else:
        return "incorrect, addition is wrong"
    
print(highest_letterTest(['p','a', 'l', 'e' ],highest_letter("apple")))
print(highest_letterTest(['c','m', 'a', 'g', 'i'],highest_letter("magicccc")))
print(highest_letterTest([''],highest_letter('')))
    
