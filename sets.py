j=set()
m=set("kobylamamalybok")
j.add("z")
j.add("z") #stale iba jedno z
j.add("a")
j.add(9)
print(j)
if 9 in j:
    print ("je tam")
else:
    print("neni tam")
print(m)
c=m.intersection(j) #alebo m.union
print(c)
