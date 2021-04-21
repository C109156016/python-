n=int(input("請輸入度數:"))
summer=0
nsummer=0
if n>=701:
    summer=(n-700)*5.63+200*4.97+170*4.39+210*3.02+120*2.10
    nsummer=(n-700)*4.50+200*4.01+170*3.61+210*2.68+120*2.10
elif n<701 and n>=501:
    summer=(n-500)*4.97+170*4.39+210*3.02+120*2.10
    nsummer=(n-500)*4.01+170*3.61+210*2.68+120*2.10
elif n<501 and n>=331:
    summer=(n-330)*4.39+210*3.02+120*2.10
    nsummer=(n-330)*3.61+210*2.68+120*2.10
elif n<331 and n>=121:
    summer=(n-120)*3.02+120*2.10
    nsummer=(n-120)*2.68+120*2.10
elif n<121:
    summer=n*2.10
    nsummer=n*2.10
print("Summer months:",summer,"\nNon-Summer months:",nsummer)