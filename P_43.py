t=int(input("輸入:"))
list1=[]
w=0
for i in range(0,t):
    m=int(input("班級人數:"))
    list1.append(m)
for k in range(0,t):
    for n in range(0,len(list1)-1):
        if list1[n]<list1[n+1]:
            w=list1[n]
            list1[n]=list1[n+1]
            list1[n+1]=w
print(list1[0])