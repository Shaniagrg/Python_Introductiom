'''
a = "abcd"
ans: "a" "ab" "abc" "abcd" "b" "bc" "bcd" "c" "cd" "d"

range(i, len(a)) generates numbers starting from i up to (but not including) len(a). 
This allows the loop to access each character starting from index i to the end of the string.
For example:
If i = 0: range(0, 4) produces 0, 1, 2, 3 (which corresponds to "a", "ab", "abc", "abcd").
If i = 1: range(1, 4) produces 1, 2, 3 (which corresponds to "b", "bc", "bcd").
If i = 2: range(2, 4) produces 2, 3 (which corresponds to "c", "cd").
If i = 3: range(3, 4) produces 3 (which corresponds to "d").

'''

def get_cumulative_str (a:str) -> list[str]:
    add:list[str] = []
    if len(a) == 0:
        add.append(a)
        return add
    
    else:
        for i in range(len(a)):
            value = ""
            for j in range(i, len(a)): 
                value = value + a[j]  
                add.append(value)  
        return add

def addTest(expected:list[str], actual:list[str]) -> str:
    print(actual)
    for i in range(len(expected)):
        if expected[i] == actual[i]:
            return "correct"

        else:
            return "incorrect, addition is wrong"

print(addTest(['a','ab','abc','abcd','b','bc','bcd','c','cd','d'], get_cumulative_str("abcd") ))
print(addTest(['e','ef','efg','efgh','f','fg','fgh','g','gh','h'], get_cumulative_str("efgh") ))
print(addTest([''], get_cumulative_str('') ))
