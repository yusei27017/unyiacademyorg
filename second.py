x = int(input("請輸入整數"))
L=[]
for i in range(1, x+1):

    if i % 3 != 0:
             if i % 5 != 0:
                    L.append(i)
    if i % 15 == 0:
        L.append(i)

print(len(L))
