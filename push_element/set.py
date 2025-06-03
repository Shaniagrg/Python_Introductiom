#syntax is .add()

#aa:set[int] = {} won't work cuz {} This creates an empty **dictionary**, not a set!
#use set() to start an empty set, not {}
aa:set[int] = set()
aa.add(2)
aa.add(4)
print(aa)
print(len(aa))

bb:set[str] = {"hay","grass","lemon"}
bb.add("thorn")
bb.add("lemon")
bb.add("dry")
print(bb)