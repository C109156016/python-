n=int(input("輸入一整數:"))
for i in range(-1,n):
    print(" "*(-i+(n-1)),"*"*(n-(-i)*(n-1)))
for m in range(-1,(n-1)):
    print(" "*(m+(n-1)),"*"*(n+(n-1)*(-m)))