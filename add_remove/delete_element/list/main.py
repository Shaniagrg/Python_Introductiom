#list.remove(element)
aa:list[int] = [1,2,3,4,5,6]
aa.remove(4)
print(aa)

#list.pop() or list.pop(index)
ab:list[int] = [1,2,3,4,5,6]
ab.pop()    #removes the last element 6
print(ab)
ab.pop(1)   #removes ab[1] which is 2
print(ab)

# del list[index]
ac:list[int] = [1,2,3,4,5,6]
del ac[0]
print(ac)

# del list[index(from) : index(to)]
del ac[1:3]
print(ac)

# list.clear()
ad:list[int] = [1,2,3,4,5,6]
ad.clear()
print(ad)   #only container remains