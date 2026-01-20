'''
Get the sum of the row
eg: [[4,1],[5,2],[6,3]]
ans: 5,7 & 9
'''

def sum_row (a:list[int]) -> list[int]:
    sum:list[int] = []
    for row in range(len(a)):
        total:int = 0
        for column in range(len(a[row])):
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
        
print (addTest([5,7,9] , sum_row([[4,1],[5,2],[6,3]])))
print (addTest([6,4,3] , sum_row([[3,3],[2,2],[2,1]])))
    