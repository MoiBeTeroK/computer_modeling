n, r0, g = 5, 0.585, 927

y=[]
for i in range(n):
    y_new=round((r0*g) % 1, 4)  #дробная часть
    y.append(y_new)
    r0=y_new

print(y)