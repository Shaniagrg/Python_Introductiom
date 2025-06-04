#Use Update. Syntax .update({key:value})
bb:dict[str,int] = {}
bb.update({'apple': 1})                #doesn't exist so push value
bb.update({"banana": 2, "carrot":3})   #doesn't exist so push value
bb.update({"apple":10})                #"apple" exists so replace the 1 with new value "apple":10
print(bb)



#Using assignment operator where syntax is dict[key] = value
aa:dict[str,int] = {"Rita": 245}
aa["Rita"] = 1  #"Rita" exists so relace 245 with new value 1
aa["Sam"] = 2   #"Sam" doesn't exist so adds "Sam":2
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

#Using setdefault() syntax .setdefault(key,value)
ca:dict[str,int] = {}
ca.setdefault("a",22) # "a" doesn't exist to add inside container
ca.setdefault("b",33) # "b" doesn't exist to add inside container
ca.setdefault("a",4)  # "a" EXIST so doens't cahnge the value
print(ca)