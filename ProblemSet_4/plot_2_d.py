import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0.1, 10)

t_values = [1, 1.5, 2, 4]

def get_s(t, x_values):
    term1 = np.exp(-x_values/t)
    term2 = x_values *(t**(3./2.))
    return term1/term2

for temp in t_values:
    plt.plot(x_values, get_s(temp, x_values), label=str(temp))

plt.legend()
plt.ylabel('Non-Dimensional surface density')
plt.xlabel('Non-Dimensional radius')
plt.xscale('log')
plt.yscale('log')
plt.show()
