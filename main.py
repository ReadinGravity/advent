fr=open("calories/calories.txt", "r")

maxelf=0
elf=0
zoz=[]
for row in fr:
    temp=row.strip()
    if temp.isdigit():
       elf+=int(temp)
    else:
       if elf>maxelf:
           maxelf=elf
           zoz.append(elf)
       elf=0

sort=sorted(zoz, reverse=True)
print(sort)
print(sum(sort[0:3:1]))
# print(maxelf)
