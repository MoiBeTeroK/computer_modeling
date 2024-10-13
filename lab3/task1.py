n, r0 = 6, 0.583
num=[]
r=r0
for i in range(n):
    sq=str(r**2)
    middle = sq[4:8]

    r=int(middle)/10000.0
    num.append(r)

print("Сгенерированные случайные числа:", num)