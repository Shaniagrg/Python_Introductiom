'''
a = "abcd"
ans: "a" "ab" "abc" "abcd"
'''

def get_cumulative_str (a:str) -> list[str]:
    add:list[str] = []
    value:str = ""
    for i in range(len(a)):
        value = value + a[i]
        add.append(value)
    return add

def addTest(expected:list[str], actual:list[str]):
    if expected == actual:
        return "correct"

    else:
        return "incorrect, addition is wrong"

print(addTest(['a','ab','abc','abcd'], get_cumulative_str("abcd") ))
print(addTest(['e','ef','efg','efgh'], get_cumulative_str("efgh") ))
