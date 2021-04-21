n=str(input("輸入:"))
ans=0
list1=list(n)
for i in range(0,len(list1)):
    if "A" in list1:
        list1.remove("A")
        list1.append(14)
    elif "J" in list1:
        list1.remove("J")
        list1.append(11)
    elif "Q" in list1:
        list1.remove("Q")
        list1.append(12)
    elif "K" in list1:
        list1.remove("K")
        list1.append(13)
for m in range(0,len(list1)):
    list1[m]=int(list1[m])
    ans=ans+list1[m]
print(ans)
