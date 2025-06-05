#Syntax: set.remove(element)
aa:list[str] = ["f","g","y","h"]
aa.remove("g")
print(aa)

''' Doesn't work
#set.discard(element)
ab:list[str] = ["f","g","y","h"]
ab.discard("g")
print(ab)
'''

#set.pop()
ab:list[str] = ["f","g","y","h"]
ab.pop()  #randomly removes any item
print(ab)

#set.clear()
ac:list[str] = ["f","g","y","h"]
ac.clear()  
print(ac)

# del set
ad:list[str] = ["f","g","y","h"]
del ad 
# print(ad) throws error cuz the ad was been completely removed


