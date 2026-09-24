maina = "abcdefghijklmnopqrstuvwxyz"

numberss = []

actual = "abc"
rt = [i for i in actual]

ty = [i for i in range(1, 27)]
ty.reverse()


for i in range(1,len(maina)+1):
    charrr = maina[i-1]
    numm   = ty[i-1]


for ch in rt:
    numberss.append(ty[maina.index(ch)])


ew = 1
summ = 0
for i in numberss:
    prod = i*ew
    summ = summ +prod
    ew+=1
print(summ)