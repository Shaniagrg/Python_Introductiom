'''
Get sum of the column
eg: [[4,1],[5,2],[6,3]]
ans: 15 & 6

edge case []
'''

def sum_column(a:list[int]) -> list[int]:
    sum:list[int] = [] 
    if len(a) == 0:
        sum.append(a)
        return sum
    else:
        total_column:int = len(a[0])  
        for column in range(total_column):
            total:int = 0
            
            for row in range(len(a)):
                total = total + a[row][column]
                
            sum.append(total)
            
        return sum

def addTest(expected:list[int], actual:list[int]) -> str:
    print(actual)
    for i in range(len(expected)):
        if expected[i] == actual[i]:
            return "correct"

        else:
            return "incorrect, addition is wrong"

print(addTest([15,6], sum_column([[4,1],[5,2],[6,3]])))
print(addTest([8,10], sum_column([[4,1],[2,5],[2,4]])))
print(addTest([[]], sum_column([])))
            
       

