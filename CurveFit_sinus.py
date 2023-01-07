from numpy import sin
from numpy import sqrt
from numpy import arange
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot

# Definisi fungsi
def objective(x, a, b, c):
	return a * sin(b - x) + c

# data dalam bentuk CSV
url = 'https://raw.githubusercontent.com/HurrCN/PemrogramanTeknik02/MyProject/Plot_Metrin_Tedi_Orde5.csv'
dataframe = read_csv(url, header=None, sep=';')
data = dataframe.values
x, y = data[:, 0], data[:, -1]

# curve fit
popt, _ = curve_fit(objective, x, y)
a, b, c = popt
print(popt)

pyplot.scatter(x, y)

x_line = arange(min(x), max(x), 1)
y_line = objective(x_line, a, b, c)
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()