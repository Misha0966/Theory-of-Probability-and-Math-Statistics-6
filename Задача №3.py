# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего
# роста родителей и детей.

import numpy as np
from scipy import stats

H_d = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
H_m = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
a = 1 - 0.95
ta_2 = 1 - a / 2
n1 = len(H_d)
n2 = len(H_m)
n = n1 # объем выборки
D1 = np.var(H_d, ddof=1)
D2 = np.var(H_m, ddof=1)
D = (D1 + D2) / 2 # сред дисперсия двух выборок
print('D=', round(D, 3)) # D = 75.583
M1 = np.mean(H_d)
M2 = np.mean(H_m)
delta = M1 - M2 # Дельта
SE = np.sqrt(D/n1 + D/n2) # стандартн ошибка разности средних
print('SE=', round(SE, 3))
df = 2 * (n - 1)
print("M1=", round(M1, 3), "M2=", round(M2, 3)) # M1 = 166.2 M2 = 168.1
print('delta=', round(delta, 3)) # delta = -1.9
t = stats.t.ppf(ta_2, df) # t = 2.101
print('t=', round(t, 3))
Low = delta - t * SE # ниж граница интервала
Up = delta + t * SE # верх граница интервала
print(f"доверительный интервал для разности среднего: [{round(Low, 3)} : {round(Up, 3)}] ")
# доверительный интервал для разности среднего: [-10.068 : 6.268]