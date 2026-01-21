'''
a = "abcd"
ans -> a b c d
'''

def get_value (a:str) -> list[str]:
    alphabet:list[str] = []
    
    for i in range(len(a)):
        alphabet.append(a[i])  
        
    return alphabet

def addTest(expected:list[str], actual:list[str]) -> str:
    for i in range(len(expected)):
        if expected[i] != actual[i]:
            return "incorrect, addition is wrong"
    return "correct"

    
print(addTest(['a','b','c','d'], get_value('abcd')))
print(addTest(['e','f','g','h'], get_value('efgh')))
print(addTest([], get_value(''))) #edge cases like empty array and string
