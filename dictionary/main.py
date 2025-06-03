#dict AKA map
#variable [key,value]
a:dict[str,int]= {'john':1}
print(a)
print(a['john']) #to get value of john

x:dict[str,int] = {"Ant":1, "Bird":2, "Cat":3}
print(x)
#print(x[0]) won't work cuz dictionaries(map) are indexed by their keys not numbers like list(array)
print(x["Bird"])

r:dict[int,list[str]] = {12:["hello", "ni-hao", "cao"]}
print(r)
print(r[12][0])

b:dict[int,dict[str,int]]= {2000:{'kyle':1,'tim':2,'kendal':3}}
print(b[2000]['kendal'])

j:dict[str,dict[str,list[float]]] = {"san-francisco":{"time-zone":[10.2,6.8,4.26]}}
print(j)
print(j["san-francisco"])
print(j["san-francisco"]["time-zone"])
print(j["san-francisco"]["time-zone"][1])