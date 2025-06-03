#used for storing unique values
#eg: [1,1,1,2,2,2,3,4,4,4,5,5,1,3,3,3] => {1,2,3,4,5} or {2,4,5,1,3} removes duplicate, unordered and doesn't have index
x:set = {1,7,8,5}
print(x)
#a:list[int] = set([1,2,2,3,2]) this works but 1st: it will create set whcih is [1,2,3] and we know set doesnt have index
#then 2nd as a:list[int] it will turn the set to list by adding index
a:set[int] = set([1,2,2,3,2])
print(a)
#print(a[1]) not valid cuz it's unindexed (we don't know which duplicates were removed) 
if 1 in a:
    print(1) 

b = set(a)
print(b)

aa:list[int] = set([1,2,2,3,2,5,7])
print(aa)

if 0 in aa: #0 doesn't exist which is FALSE so doesn't go inside this block and goes to line 21
    print(0)

if 5 in aa: #5 exist which is TRUE so creates C1:PO block
    print(3)


#nested array 
#you:set[set[int]] = set([[1,6,3,3],[7,7,9,4,2,2]]) WON'T work cuz you have to specify SET to each
you:set[set[int]] = [set([1, 6, 3, 3]), set([7, 7, 9, 4, 2, 2])]
print(you)