import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

mach_range = np.linspace(1,20,100)
n_min = 0.057 # found in part b

def calc_sigma_s(mach):
    return math.log(1 + mach/4)

sigma_s = np.asarray([calc_sigma_s(value) for value in mach_range])

plt.plot(mach_range, n_min/(np.exp(np.sqrt(2*sigma_s**2)*sp.erfinv(1 - 2*n_min) - (sigma_s**2/2))), lw=4, color='#424242')
plt.xlabel('Mach Number', fontsize=16, labelpad=20)
plt.plot(7, 5e4, marker='o', color='r')
plt.ylabel('Average Density', fontsize=16, labelpad=20)
plt.show()
