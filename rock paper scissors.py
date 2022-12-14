fr=open("calories/rockpaperscissors.txt")
# x=1 14184
# y=2
# a=3
# a+x=3+1
# a+y=2+6
game={("A","X"):3,("A","Y"):4, ("A","Z"):8, ("B","X"):1, ("B","Y"):5, ("B","Z"):9, ("C","X"):7, ("C","Y"):2,("C","Z"):6}
#game={("A","X"):4,("A","Y"):8, ("A","Z"):3, ("B","X"):2, ("B","Y"):5, ("B","Z"):9, ("C","X"):7, ("C","Y"):2,("C","Z"):6}
sum=0
for row in fr:
    chars=row.strip().split()
    sum+=game[(chars[0], chars[1])]     #game=kukam do dict, prvy chars[0]=1. pismenko, chars[1]=2.pismenko
print(sum)



