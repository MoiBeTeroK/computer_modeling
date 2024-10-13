import matplotlib.pyplot as plt
import random
def f1(x):
    return (10*x)/6
def f2(x):
    return 10*(x-20)/(6-20)

a = 6 
x_min, y_min = 0, 0
x_max, y_max = 20,10
n=2000

x_points = []
y_points = []
inside_x = []
inside_y = []
count=0
#Поиск точек внутри и вне треугольника
for _ in range(n):
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    if y < f1(x) and y < f2(x) and y > 0:
        count += 1
        inside_x.append(x)
        inside_y.append(y)
    else:
        x_points.append(x)
        y_points.append(y)

S = round((count / n) * x_max*y_max, 4)
print(f"Площадь треугольника по методу Монте-Карло: {S}")

#Проверка через интегралы
pr1, pr2=0,0
for x in range(a):
    pr1+=f1(x)
for x in range(a, x_max):
    pr2+=f2(x)
print(f"Точная площадь: {pr1+pr2}")

#Погрешности
abs_error = round(abs(pr1+pr2-S), 4)
otn_error = round(abs_error/abs(pr1+pr2),4)*100
print(f"Абсолютная погрешность: {abs_error}")
print(f"Относительная погрешность: {otn_error}")


plt.plot([0, 6, 20, 0], [0, 10, 0, 0], 'r-', label='Треугольник')
plt.plot(inside_x, inside_y, 'ro', color ='b', alpha=0.5, label = 'Точки внутри треугольника')
plt.plot(x_points, y_points, 'ro', color ='g', alpha=0.5, label = 'Точки вне треугольника')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод Монте-Карло для вычисления площади треугольника')
plt.legend()
plt.grid()
plt.show()