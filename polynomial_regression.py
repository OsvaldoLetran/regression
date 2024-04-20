import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score


frecuencia = [540, 560, 580, 600, 630, 660, 690, 710, 750, 780, 830, 870, 920, 990, 1040, 1100, 1200, 1300, 1400, 1600]
resistencia = [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
periodo = []
for i in frecuencia:
    periodo.append(1 / i)


def funct_f(x, c):
    return 1 / (2 * math.pi * x * c)


def funct_t(x_2, c):
    return x_2 / (2 * math.pi * c)


x = np.array(frecuencia)
x_2 = np.array(periodo)
y = np.array(resistencia)

coeff = np.polyfit(x, y, 2)
f = np.poly1d(coeff)

coeffs = np.polyfit(x_2, y, 1)
f_2 = (coeffs[0] * x_2) + coeffs[1]

fit, cov = curve_fit(funct_f, x, y)
print(f'Capacitancia C [R vs f] = {fit[0]} +/- {cov[0, 0]}')
print(f'Eq. resistencia R = 1 / (2 * {math.pi:.4f} * f * {fit[0]:.4e})')

fit_2, cov_2 = curve_fit(funct_t, x_2, y)
print(f'Capacitancia C [R vs T] = {fit_2[0]} +/- {cov_2[0, 0]}')
print(f'Eq. resistencia R = T / (2 * {math.pi:.4f} * {fit_2[0]:.4e})')

r2 = r2_score(y, f(x))
print(f'Coef. determinacion [R vs f]: {r2}')

r = np.corrcoef(x_2, y)[0, 1]
print(f'Coef. correlación [R vs T]: {r}')


fig, ax = plt.subplots()
ax.plot(x, f(x), 'r-')
ax.scatter(x, y)
ax.set(xlabel = 'Frecuecia [Hz]', ylabel = 'Resistencia')
plt.show()


fig, ax_1 = plt.subplots()
ax_1.plot(x_2, f_2, 'r-')
ax_1.scatter(x_2, y)
ax_1.set(xlabel = 'Periodo [T]', ylabel = 'Resistencia')
plt.show()