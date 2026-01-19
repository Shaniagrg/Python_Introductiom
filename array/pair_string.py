'''
a = "abcd"
ans = "ad" "ab"
'''

def get_value (a:str) -> list[str]:
    alphabet:list[str] = []
    
    for i in range(len(a)):
        if i % 2 == 1: #check for odd number 
            pair:str = a[0] + a[i]
            alphabet.append(pair)
        
    return alphabet

def addTest(expected:list[str], actual:list[str]) -> str:
    for i in range(len(expected)):
        if expected[i] == actual[i]:
            return "correct"

        else:
            return "incorrect, addition is wrong"
    
print(addTest(['ab','ad'], get_value('abcd')))
print(addTest(['ef','eh'], get_value('efgh')))