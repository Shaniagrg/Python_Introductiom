'''
Get sum of the column
eg: [[4,1],[5,2],[6,3]]
ans: 15 & 6
'''

def sum_column(a:list[int]) -> list[int]:
    sum:list[int] = []
    total_column:int = len(a[0])  
    
    for column in range(total_column):
        total:int = 0
        
        for index in range(len(a)):
            total = total + a[index][column]
            
        sum.append(total)
        
    return sum

def addTest(expected:list[int], actual:list[int]):
    if expected == actual:
        return "correct"

    else:
        return "incorrect, addition is wrong"

print(addTest([15,6], sum_column([[4,1],[5,2],[6,3]])))
print(addTest([8,10], sum_column([[4,1],[2,5],[2,4]])))
            
       

