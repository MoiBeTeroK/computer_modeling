import math
import matplotlib.pyplot as plt
import random

def f(x):
    return math.sqrt(11-6*math.sin(x)**2)

a, b = 5, math.sqrt(11)
n, n_xy=2000, 100
#Построение графика
y_main, x_main=[],[]
step = a / (n_xy - 1) 
for j in range(n_xy):
    x_value = j * step
    x_main.append(x_value)
    y_main.append(f(x_value))

x_points = []
y_points = []
inside_x = []
inside_y = []
count=0
#Поиск точек внутри и вне функции
for _ in range(n):
    x = random.uniform(0, a)
    y = random.uniform(0, b)
    if y < f(x) and y > 0:
        count += 1
        inside_x.append(x)
        inside_y.append(y)
    else:
        x_points.append(x)
        y_points.append(y)
    
S = round((count / n) * a*b, 4)
print(f"Интеграл по методу Монте-Карло: {S}")

pr = 0
for x in range(a):
    pr+=f(x)
print(f"Точная площадь: {pr}")

#Погрешности
abs_error = round(abs(pr-S),4)
otn_error = round(abs_error/abs(pr),4)*100
print(f"Абсолютная погрешность: {abs_error}")
print(f"Относительная погрешность: {otn_error}")

plt.plot(x_main, y_main, 'r-', label='Функция')
plt.plot(inside_x, inside_y, 'ro', color ='b', alpha=0.5, label = 'Точки внутри интеграла')
plt.plot(x_points, y_points, 'ro', color ='g', alpha=0.5, label = 'Точки вне интеграла')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод Монте-Карло для вычисления интеграла')
plt.legend()
plt.grid()
plt.show()