a, m, x0 = 265, 129, 122

x=[]
x_new=round((a*x0) % m, 4)
for i in range(5):
    x.append(x_new)
    x0=x_new
    x_new=round((a*x0) % m, 4)

print(x)