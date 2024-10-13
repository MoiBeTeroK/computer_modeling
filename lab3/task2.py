n, r0, r1 = 6, 0.5836, 0.2176
num=[]
for i in range(n):
    r=str(r0*r1)
    middle = r[4:8]

    r=int(middle)/10000.0
    num.append(r)
    r0=r1
    r1=r
    
print("Сгенерированные случайные числа:", num)