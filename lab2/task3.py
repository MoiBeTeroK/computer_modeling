import matplotlib.pyplot as plt
import random
import numpy as np
import math

r=6
n=2000
theta = np.linspace(0, 2 * np.pi, 100)

x_main = r * np.cos(theta)
y_main = r * np.sin(theta)

x_points = []
y_points = []
inside_x = []
inside_y = []
count=0
#Поиск точек внутри и вне окружности
for _ in range(n):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    if (x)**2 + (y)**2 <r**2:
        count += 1
        inside_x.append(x)
        inside_y.append(y)
    else:
        x_points.append(x)
        y_points.append(y)

PI = round(4 * count/n,4)
print(f"Площадь: {PI}")

#Погрешности
print(f"PI: {math.pi}")
abs_error = round(abs(math.pi-PI),4)
otn_error = round(abs_error/math.pi,4)*100
print(f"Абсолютная погрешность: {abs_error}")
print(f"Относительная погрешность: {otn_error}")

plt.plot(x_main, y_main, color='r', label='Окружность')
plt.scatter(inside_x, inside_y, color='b', alpha=0.5, label='Точки внутри окружности')
plt.scatter(x_points, y_points, color='g', alpha=0.5, label='Точки вне окружности')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод Монте-Карло для вычисления числа пи')
plt.legend()
plt.grid()
plt.show()