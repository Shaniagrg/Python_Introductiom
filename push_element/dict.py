#syntax is dict[key] = value
aa:dict[str,int] = {}
aa["Rita"] = 1
aa["Sam"] = 2
print(aa)
print(len(aa))

#nested map
ab:dict[str,dict[str,str]] = {}
ab["Sam"] = {"height": "153cm","Address":"sf","Age":"32"}
ab["Jerry"] = {"height":"20cm","age":"2"}
print(ab)

#nested list
ac:dict[str,list[int]] = {}
ac["june-expense"] = [200,216,50]
ac["july-expense"] = [13,20]
print(ac)