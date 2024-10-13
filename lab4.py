import numpy as np
import matplotlib.pyplot as plt

def sequence(n, a=23566, m=1000000, x=0.135):
    seq = []
    for _ in range(n):
        x = (a * x) % m
        x_norm = round(x / m, 4)
        seq.append(x_norm)
    return seq

# Функции для генерации выборок
def generate_uniform_sample(n, low, high):
    seq = sequence(n)
    return [low + (high - low) * x for x in seq]

def generate_exponential_sample(n, lam):
    seq = sequence(n)
    return [-np.log(1 - x) / lam for x in seq]

def generate_normal_sample(n, mu, sigma):
    seq = sequence(n)
    seq = np.array(seq) 
    z1 = np.sqrt(-2 * np.log(seq[:n // 2])) * np.cos(2 * np.pi * seq[n // 2:])
    z2 = np.sqrt(-2 * np.log(seq[:n // 2])) * np.sin(2 * np.pi * seq[n // 2:])
    z = np.concatenate((z1, z2))
    return mu + sigma * z

# Функции для вычисления математического ожидания и дисперсии
def compute_mean_variance(sample):
    mean = sum(sample) / len(sample)
    variance = sum((x - mean) ** 2 for x in sample) / len(sample)
    return mean, variance

# Параметры
N = 1000  # Размер выборки
sample_sizes = [10, 20, 50, 100, 1000]  # Объемы выборок для анализа

# Параметры распределений
uniform_params = (9, 17)  # равномерное распределение
exponential_lambda = 4  # экспоненциальное распределение
normal_params = (0, 5)  # нормальное распределение

# Теоретическое мат. ожидание
math_expectation_uniform = (uniform_params[0] + uniform_params[1]) / 2
math_expectation_exponential = 1 / exponential_lambda
math_expectation_normal = normal_params[0]

# Теоретическая дисперсия
dispersion_uniform = (uniform_params[1] - uniform_params[0]) ** 2 / 12
dispersion_exponential = 1 / exponential_lambda ** 2
dispersion_normal = normal_params[1] ** 2

# Генерация выборок
uniform_sample = generate_uniform_sample(N, *uniform_params)
exponential_sample = generate_exponential_sample(N, exponential_lambda)
normal_sample = generate_normal_sample(N, *normal_params)

# Вычисление оценок для разных объемов выборок
results = {"uniform": [], "exponential": [], "normal": []}
errors = {"uniform": {}, "exponential": {}, "normal": {}}

for n in sample_sizes:
    u_mean, u_var = compute_mean_variance(uniform_sample[:n])
    e_mean, e_var = compute_mean_variance(exponential_sample[:n])
    n_mean, n_var = compute_mean_variance(normal_sample[:n])

    results["uniform"].append((n, u_mean, u_var))
    results["exponential"].append((n, e_mean, e_var))
    results["normal"].append((n, n_mean, n_var))

    # Вычисление погрешностей при n == 100
    if n == 100:
        abs_error_uniform_mean = abs(u_mean - math_expectation_uniform)
        rel_error_uniform_mean = abs(u_mean - math_expectation_uniform) / math_expectation_uniform

        abs_error_exponential_mean = abs(e_mean - math_expectation_exponential)
        rel_error_exponential_mean = abs(e_mean - math_expectation_exponential) / math_expectation_exponential

        abs_error_normal_mean = abs(n_mean - math_expectation_normal)
        rel_error_normal_mean = abs_error_normal_mean

        # Погрешности для дисперсии
        abs_error_uniform_var = abs(u_var - dispersion_uniform)
        rel_error_uniform_var = abs(u_var - dispersion_uniform) / dispersion_uniform

        abs_error_exponential_var = abs(e_var - dispersion_exponential)
        rel_error_exponential_var = abs(e_var - dispersion_exponential) / dispersion_exponential

        abs_error_normal_var = abs(n_var - dispersion_normal)
        rel_error_normal_var = abs(n_var - dispersion_normal) / dispersion_normal

        # Сохраняем погрешности
        errors["uniform"]["mean"] = {"absolute": abs_error_uniform_mean, "relative": rel_error_uniform_mean}
        errors["uniform"]["variance"] = {"absolute": abs_error_uniform_var, "relative": rel_error_uniform_var}

        errors["exponential"]["mean"] = {"absolute": abs_error_exponential_mean, "relative": rel_error_exponential_mean}
        errors["exponential"]["variance"] = {"absolute": abs_error_exponential_var, "relative": rel_error_exponential_var}

        errors["normal"]["mean"] = {"absolute": abs_error_normal_mean, "relative": rel_error_normal_mean}
        errors["normal"]["variance"] = {"absolute": abs_error_normal_var, "relative": rel_error_normal_var}

# Вывод результатов
for dist_name, dist_results in results.items():
    print(f"\nРезультаты для {dist_name}:")
    for (n, mean, var) in dist_results:
        print(f"Объем выборки N={n}: Мат. ожидание = {mean:.4f}, Дисперсия = {var:.4f}")

# Вывод погрешностей для выборки N=100
print("\nПогрешности для выборки N=100:")
for dist_name, error in errors.items():
    print(f"{dist_name.capitalize()} (мат. ожидание):")
    print(f"  Абсолютная погрешность: {error['mean']['absolute']:.4f}")
    print(f"  Относительная погрешность: {error['mean']['relative']:.4%}")
    print(f"{dist_name.capitalize()} (дисперсия):")
    print(f"  Абсолютная погрешность: {error['variance']['absolute']:.4f}")
    print(f"  Относительная погрешность: {error['variance']['relative']:.4%}")

# Графики
fig, axs = plt.subplots(3, 5, figsize=(12, 6))

for i, n in enumerate(sample_sizes):
    # Равномерное распределение
    axs[0, i].hist(uniform_sample[:n], bins=10, density=True, alpha=0.6, color='g')
    low, high = uniform_params
    x_uniform = np.linspace(low, high, 1000)
    axs[0, i].plot(x_uniform, np.ones_like(x_uniform) * (1 / (high - low)), 'r-', lw=2)
    axs[0, i].set_title(f'Равномерное N={n}')
    axs[0, i].grid(True)

    # Экспоненциальное распределение
    axs[1, i].hist(exponential_sample[:n], bins=10, density=True, alpha=0.6, color='b')
    x_exponential = np.linspace(0, np.max(exponential_sample[:n]), 1000)
    axs[1, i].plot(x_exponential, exponential_lambda * np.exp(-exponential_lambda * x_exponential), 'r-', lw=2)
    axs[1, i].set_title(f'Экс-ое N={n}')
    axs[1, i].grid(True)

    # Нормальное распределение
    axs[2, i].hist(normal_sample[:n], bins=10, density=True, alpha=0.6, color='r')
    mu, sigma = normal_params
    x_normal = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    axs[2, i].plot(x_normal, (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_normal - mu) / sigma) ** 2), 'b-', lw=2)
    axs[2, i].set_title(f'Нормальное N={n}')
    axs[2, i].grid(True)
plt.subplots_adjust(hspace=0.5, wspace=0.4)
plt.tight_layout()
plt.show()

# Создание полотна для гистограмм мат. ожидания и дисперсии
fig2, axs2 = plt.subplots(2, 3, figsize=(12, 6))

# Данные для мат. ожидания и дисперсии
means = [result[1] for result in results["uniform"]]
variances = [result[2] for result in results["uniform"]]
means_exp = [result[1] for result in results["exponential"]]
variances_exp = [result[2] for result in results["exponential"]]
means_norm = [result[1] for result in results["normal"]]
variances_norm = [result[2] for result in results["normal"]]

# Гистограммы для мат. ожидания
bar_width = 0.4
x_indexes = np.arange(len(sample_sizes))

axs2[0, 0].bar(x_indexes, means, width=bar_width, alpha=0.6, color='g', align='center')
axs2[0, 0].set_title('Мат. ожидание (равномерное)')
axs2[0, 0].set_xticks(x_indexes)
axs2[0, 0].set_xticklabels(sample_sizes)
axs2[0, 0].grid(True)

axs2[0, 1].bar(x_indexes, means_exp, width=bar_width, alpha=0.6, color='b', align='center')
axs2[0, 1].set_title('Мат. ожидание (экспоненциальное)')
axs2[0, 1].set_xticks(x_indexes)
axs2[0, 1].set_xticklabels(sample_sizes)
axs2[0, 1].grid(True)

axs2[0, 2].bar(x_indexes, means_norm, width=bar_width, alpha=0.6, color='r', align='center')
axs2[0, 2].set_title('Мат. ожидание (нормальное)')
axs2[0, 2].set_xticks(x_indexes)
axs2[0, 2].set_xticklabels(sample_sizes)
axs2[0, 2].grid(True)

# Гистограммы для дисперсии
axs2[1, 0].bar(x_indexes, variances, width=bar_width, alpha=0.6, color='g', align='center')
axs2[1, 0].set_title('Дисперсия (равномерное)')
axs2[1, 0].set_xticks(x_indexes)
axs2[1, 0].set_xticklabels(sample_sizes)
axs2[1, 0].grid(True)

axs2[1, 1].bar(x_indexes, variances_exp, width=bar_width, alpha=0.6, color='b', align='center')
axs2[1, 1].set_title('Дисперсия (экспоненциальное)')
axs2[1, 1].set_xticks(x_indexes)
axs2[1, 1].set_xticklabels(sample_sizes)
axs2[1, 1].grid(True)

axs2[1, 2].bar(x_indexes, variances_norm, width=bar_width, alpha=0.6, color='r', align='center')
axs2[1, 2].set_title('Дисперсия (нормальное)')
axs2[1, 2].set_xticks(x_indexes)
axs2[1, 2].set_xticklabels(sample_sizes)
axs2[1, 2].grid(True)

for ax in axs2.flatten():
    ax.set_xlim(-0.5, len(sample_sizes) - 0.5)

plt.tight_layout()
plt.show()