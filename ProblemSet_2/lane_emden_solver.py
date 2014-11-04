'''
Sove the isothermal Lane-Emden equation with boundry conditions x(0) = x'(0) = 0 by
numerically integrating. Reproduce the plots in Figures 9.1 and 9.2 of Stahler & Palla.
'''

import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Set up initial inital values and independent variable array
yinit = [0, 0]
xvalues  = np.linspace(0.1, 1000.0, 100000)

# A function that returns the first derivative of each element in
# array (see write-up for details)
def derivative(y, x):
    return np.array([y[1], ((-2*y[1]/x) + math.exp(-y[0]))])

y = odeint(derivative, yinit, xvalues)

plt.plot(xvalues, y[:,0],'r--', label=r'$\psi$')
plt.plot(xvalues, np.exp(-y[:,0]), label=r'$\rho/\rho_c$')
plt.legend()
plt.xlabel(r'Nondimensonal Radius $\xi$')
plt.show()

plt.plot(np.log10(1/np.exp(-y[:,0])), ((4*math.pi * (1/np.exp(-y[:,0])))**(-0.5))*(xvalues**2 * y[:,1]))
plt.xlabel(r'Density contrast log($\rho_c/\rho_0$)')
plt.ylabel(r'Cloud mass $m$')
plt.show()

