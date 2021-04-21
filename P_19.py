n=int(input("組數為:"))
cost=0
for i in range(0,n):
    m=str(input("輸入票數:"))
    list1=list(m)
    list1[0]=int(list1[0])
    list1[1]=int(list1[1])
    cost=cost+(list1[0]*250+list1[1]*175)
    list1.clear()
    print("第",i+1,"組應收費用",cost)
    cost=0