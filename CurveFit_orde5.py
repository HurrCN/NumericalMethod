from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def objective(x, a, b, c, d, e, f):
	return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f

url = 'https://raw.githubusercontent.com/HurrCN/PemrogramanTeknik02/MyProject/MetrinTedi2.csv'
dataframe = read_csv(url, header=None, sep=';')
data = dataframe.values
x, y = data[:, 0], data[:, -1]
print(dataframe.head(12))
"""
popt, _ = curve_fit(objective, x, y)

a, b, c, d, e, f = popt
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

plt.scatter(x, y)
x_line = arange(min(x), max(x), 1)
y_line = objective(x_line, a, b, c, d, e, f)
plt.plot(x_line, y_line, '--', color='red')
plt.xlabel('Jam')
plt.ylabel('Suhu [deg C]')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.1)
plt.show()
"""