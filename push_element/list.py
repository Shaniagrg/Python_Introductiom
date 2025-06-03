#syntax is .append()
aa:list[int] = []
aa.append(10)
aa.append(11)
print(aa)
print(len(aa))  #len = to find length of the list

#nested list
ab:list[list[int]] = []
ab.append([10,11,12])
ab.append([20,21,22])
print(ab)