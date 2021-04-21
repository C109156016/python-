k=float(input("請輸入路程公里數(km):"))
cost=75
if k<1.5:
    print("所需車資為:",cost)
else:
    if (((k-1.5)*1000)%250)==0:
        cost=cost+(((k-1.5)*1000)//250)*5
    else:
        cost=cost+(((k-1.5)*1000)//250)*5+5
    print("所需車資為:",cost)