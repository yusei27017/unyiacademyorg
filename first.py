str = input("請輸入字串")
result = ""
for s in str[::-1]:
    result += s

print(result)

str2 = input("請輸入字串 含空格")
l = str2.split()
# print(l)
L = []
for i in l:
    k = ""
    for r in i[::-1]:
        k += r
        # print(k)
    L.append(k)
    # print(L)
result2 = " ".join(L)
print(result2)
