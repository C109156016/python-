str1=str(input("輸入第一陣列:"))
list1=list(str1)
c=int(list1[0])
r=int(list1[1])
list11=[]
list22=[]
ans=[]
m=int(list1[0])*int(list1[1])
for column in range(0,c):
    for row in range(0,r):
        list11.append(str(input("輸入第一陣列數值")))
str2=str(input("輸入第二陣列:"))
list2=list(str2)
c2=int(list2[0])
r2=int(list2[1])
for column2 in range(0,c2):
    for row2 in range(0,r2):
        list22.append(str(input("輸入第二陣列數值")))
for i in range(0,m):
    ans.append(int(list11[i])+int(list22[i]))
print(ans)