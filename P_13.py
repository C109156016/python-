str1=str(input("輸入一字元為:"))
list1=list(str1)
ans=""
for i in range(0,len(list1)//2):
    if list1[i]==list1[-(i+1)]:
        ans=ans+"1"
    else:
        ans=ans+"2"
if "2" in ans:
    print("NO")
else:
    print("YES")

