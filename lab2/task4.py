import matplotlib.pyplot as plt
import random
import math
import numpy as np

def r(phi):
    return math.sqrt(17*math.cos(phi)**2+5*math.sin(phi)**2)

n=2000
a = math.sqrt(17)
b = math.sqrt(5)
inside_x = []
inside_y = []
outside_x = []
outside_y = []

#Границы прямоугольника, который содержит фигуру
phi_values = np.linspace(0, 2 * np.pi, 1000)
x_figure = [r(phi) * math.cos(phi) for phi in phi_values]
y_figure = [r(phi) * math.sin(phi) for phi in phi_values]

min_x = min(x_figure)-1
max_x = max(x_figure)+1
min_y = min(y_figure)-1
max_y = max(y_figure)+1

#Генерация случайных точек в пределах прямоугольника
count = 0
for i in range(n):
    x_i = random.uniform(min_x, max_x)
    y_i = random.uniform(min_y, max_y)
    
    # Преобразование декартовых координат в полярные
    ri = math.sqrt(x_i**2 + y_i**2)
    phi_i = math.atan2(y_i, x_i)
    
    # Радиус для данного угла
    ro = r(phi_i)
    
    # Проверка, находится ли точка внутри фигуры
    if ri < ro:
        count += 1
        inside_x.append(x_i)
        inside_y.append(y_i)
    else:
        outside_x.append(x_i)
        outside_y.append(y_i)

S = count / n * (max_x-min_x) * (max_y-min_y)
print(f"Площадь фигуры равна {S}")

#Погрешности
f_val = (17+5)*math.pi/2
print(f"Точная площадь: {f_val}")
abs_error = round(abs(f_val-S),4)
otn_error = round(abs_error/abs(f_val),4)*100
print(f"Абсолютная погрешность: {abs_error}")
print(f"Относительная погрешность: {otn_error}")

#Построение фигуры
x_figure, y_figure=[], []
phi_values = np.linspace(0, 2 * np.pi, 1000)
for i in phi_values:
    r_values = r(i)
    x_figure.append(r_values * np.cos(i))
    y_figure.append(r_values * np.sin(i))
    

plt.plot(x_figure, y_figure, color='blue', label='Фигура S') 
plt.scatter(inside_x, inside_y, color='green', label='Внутри фигуры', s=1)
plt.scatter(outside_x, outside_y, color='red', label='Вне фигуры', s=1)
plt.title('Точки внутри и вне фигуры')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()