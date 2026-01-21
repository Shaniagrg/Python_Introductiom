'''
a = "abcd"
ans = "ad" "ab"
'''

def get_value (a:str) -> list[str]:
    alphabet:list[str] = []
    
    for i in range(len(a)):
        for odd_index in range(len(a)):
            if odd_index % 2 == 1: #check for odd number 
                pair:str = a[i] + a[odd_index]
                alphabet.append(pair)
        
    return alphabet

def addTest(expected:list[str], actual:list[str]) -> str:
    print(actual)
    for i in range(len(expected)):
        if expected[i] == actual[i]:
            return "correct"

        else:
            return "incorrect, addition is wrong"
    
print(addTest(['ab','ad','bb','bd','cb','cd'], get_value('abcd')))
print(addTest(['ef','eh','ff','fh','gf','gh','hf','hh'], get_value('efgh')))