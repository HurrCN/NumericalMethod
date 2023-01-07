# Developed by Muhammad Hurricane
# Finalized in May 29, 2021

# ======================================
# PACKAGES
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
import numpy as np
# ======================================
# MAIN EQUATION AS OBJECTIVE
def obj(x,a,b,c):
    return a*x**2+b*x+c
# ======================================
# DISCRETE DATA
#array the integrated variables data from Paraview 
xData = np.array([141, 171, 231, 304, 375, 425]) # the x is multiplied by E+6 
yData = np.array([135579, 162261, 217278, 287191, 358322, 410269])
plt.scatter(xData,yData,color='b') #then plot it
# ======================================
# PROPERTIES OF EQUATION
properties, _ = cf(obj, xData, yData) #make the props from curve-fit
a, b, c = properties #put the props into a,b,c straight into "obj"
print("a = %0.8f x 10^12 | b = %0.8f x 10^6| c = %0.8f" %(a,b,c))
#As the consequence, the "a" must be the "E-12" version so we've to neutralized it back
# ======================================
# CURVE CONSTRUCTION
xCurve = np.arange(min(xData), max(xData)) #set the xCurve boundaries
yCurve = obj(xCurve, a, b, c) #use the yCurve as function of xCurve 
plt.plot(xCurve,yCurve,'-',color='r') #then plot it
# ======================================
# LABELS
plt.xlabel('Cross-Sectional Area (E-6 m^2)')
plt.ylabel('Cost (IDR)')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#666666', linestyle='-', alpha=0.1)
plt.show()