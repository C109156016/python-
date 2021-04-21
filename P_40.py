n=int(input("搭了幾次電梯:"))
list1=[]
cost=0
for i in range(0,n):
    m=int(input("樓層:"))
    list1.append(m)
for w in range(0,n-1):
    if list1[w]>list1[w+1]:
        cost=cost+((list1[w]-list1[w+1])*10)
    elif list1[w]<list1[w+1]:
        cost=cost+((list1[w+1]-list1[w])*20)
cost=cost+(list1[0]-1)*20
print(cost,"元")
1