import matplotlib.pyplot as plt
import math

def det(a,b,c,d):
    return a*d-b*c

def det3(a,b,c,d,e,f,g,h,i):
    return a*e*i + d*h*c + b*f*g - c*e*g - h*f*a - b*d*i

def linear_func(x, y, n):
    x_sum = sum(x)
    y_sum = sum(y)
    x1_sum = round(sum(i ** 2 for i in x), 4)
    yx_sum = round(sum(x[i] * y[i] for i in range(n)), 4)

    D = round(det(x1_sum, x_sum, x_sum, n), 4)
    D1 = round(det(yx_sum, x_sum, y_sum, n), 4)
    D2 = round(det(x1_sum, yx_sum, x_sum, y_sum), 4)

    a = round(D1 / D, 2)
    b = round(D2 / D, 2)

    return a, b

def pow_func(x, y, n):
    log_x = [round(math.log(i), 4) for i in x]
    log_y = [round(math.log(i), 4) for i in y]
    a, b = linear_func(log_x, log_y, n)
    b = round(math.exp(b), 2)

    return a, b

def exp_func(x, y, n):
    log_y = [round(math.log(i),4) for i in y]
    a, b = linear_func(x, log_y, n)
    b = round(math.exp(b), 2)

    return a, b

def quadratic_func(x, y, n):
    x1_sum = sum(x)
    x2_sum = round(sum(i ** 2 for i in x), 4)
    x3_sum = round(sum(i ** 3 for i in x), 4)
    x4_sum = round(sum(i ** 4 for i in x), 4)
    
    y_sum = sum(y)
    yx1_sum = round(sum(x[i] * y[i] for i in range(n)), 4)
    yx2_sum = round(sum(x[i]**2 * y[i] for i in range(n)), 4)

    D = round(det3(x4_sum, x3_sum, x2_sum, x3_sum,x2_sum,x1_sum,x2_sum,x1_sum,n), 4)
    D1 = round(det3(yx2_sum, x3_sum, x2_sum, yx1_sum,x2_sum,x1_sum,y_sum,x1_sum,n), 4)
    D2 = round(det3(x4_sum, yx2_sum, x2_sum, x3_sum,yx1_sum,x1_sum,x2_sum,y_sum,n), 4)
    D3 = round(det3(x4_sum, x3_sum, yx2_sum, x3_sum,x2_sum,yx1_sum,x2_sum,x1_sum,y_sum), 4)

    a = round(D1 / D, 2)
    b = round(D2 / D, 2)
    c = round(D3 / D, 2)
    return a,b,c

def error(y1,y2):
    sum=0
    for i in range(len(y1)):
        sum +=(y1[i]-y2[i])**2
    return sum


x = [1, 4, 7, 10, 13, 16]
y = [3.0, 7.6, 11.2, 13.8, 17.1, 19.5]
n = len(x)

a, b = linear_func(x, y, n)
a1, b1 = pow_func(x,y,n)
a2,b2 = exp_func(x,y,n)
a3, b3, c = quadratic_func(x,y,n)
print(a, b)

y_new, y_new1, y_new2, y_new3 = [], [], [],[]
for i in range(0, n):
    y_new.append(a*x[i]+b)
    y_new1.append(b1*x[i]**a1)
    y_new2.append(b2*math.exp(a2*x[i]))
    y_new3.append(a3*x[i]**2 + b3*x[i] + c)

p1=round(error(y, y_new), 4)
p2=round(error(y, y_new1),4)
p3=round(error(y, y_new2),4)
p4=round(error(y, y_new3), 4)
print(p1, p2, p3, p4)
minimal_exp = min(p1, p2, p3, p4)
print("Линейная: ", p1)
print("Степенная: ", p2)
print("Показательная: ", p3)
print("Квадратичная: ", p4)
print("Минимальная погрешность: ", minimal_exp)

plt.title("Лаба1")
plt.xlabel("ось абсцисс")
plt.ylabel("ось ординат")
plt.plot(x, y, 'ro', color ='b',label = 'Экспериментальные точки')
plt.plot(x, y_new, color ='r',label = 'y=ax+b')
plt.plot(x, y_new1, color ='k',label = 'y=ax^b')
plt.plot(x, y_new2, color ='g',label = 'y=be^bx')
plt.plot(x, y_new3, color ='y',label = 'y=ax^2+bx+c')
plt.legend()
plt.grid()
plt.show()


