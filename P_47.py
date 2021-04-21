n=int(input("輸入筆數n:"))
dict1={}
for i in range(0,n):
    m=str(input("輸入值"))
    dict1[m]=input("輸入值:")
s=str(input("輸入欲查詢單字:"))
print(s,"中文意思為:",dict1[s])