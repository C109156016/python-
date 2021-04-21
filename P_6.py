list1=[]
n=1
str1 = ""
str2 = ""
while n<6:
    n=n+1
    list1.append(str(input("輸入值為:")))
t=0
for x in range(0,4):
    for i in range(0,4):
        if list1[i]>list1[i+1]:
            t=list1[i+1]
            list1[i+1]=list1[i]
            list1[i]=t
for w in range(len(list1)):
	str1=str1+list1[w]
for m in range(0,4):
    for k in range(0,4):
        if list1[k]<list1[k+1]:
            t=list1[k+1]
            list1[k+1]=list1[k]
            list1[k]=t
for p in range(len(list1)):
	str2=str2+list1[p]
print(int(str2)-int(str1))