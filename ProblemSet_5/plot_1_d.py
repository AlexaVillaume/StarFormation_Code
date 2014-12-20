import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

m_p = 1.67e-24 # g
sigma = 5.67e-5 #cgs
ev_ergs = 1.6e-12
solar_g = 1.989e33
G = 6.67e-8 # cgs
yr_sec = 3.156e7 #second
Mdot = 10e-4*(solar_g/yr_sec)


Rinit = 2.5
mvalues = np.linspace(0.01, 50, 2000)

def bb_luminosity(radius):
    return 4*np.pi*(radius**2)*sigma*(3500**4)

def derivatives(mass, radius):
    bb = max(bb_luminosity(radius*6.955e10), 3.846e33*(mass**3))
    term1 = (2./3)*((radius*6.944e10)**2)/((mass*solar_g)**2)
    term2 = -(0.25*Mdot*G)*(mass*solar_g)/(radius*6.955e10)
    term3 = -bb
    term4 = -3*Mdot*(mass*solar_g)/(radius*6.955e10)
    term5 = (84.2*ev_ergs*Mdot)

    return term1*(term2 + term3 + term4 + term5)


def other_derivs(mass, radius):
    bb = max(bb_luminosity(radius*6.955e10), 3.846e33*(mass**3))
    print bb - (0.25*G*Mdot)*((mass*solar_g)/(radius*6.955e10))
    return bb - (0.25*G*Mdot)*((mass*solar_g)/(radius*6.955e10))

def tout_radius(M):
    omega = 0.62246212
    l = -0.42450044
    kappa = -7.11727086
    gamma = 0.32699690
    mu = 0.02410413
    nu = 0
    eta = 0.94472050
    o = -7.45345690
    pi = -0.00186899

    term1 = omega*(M**2.5) + l*(M**6.5) + kappa*(M**11) + gamma*(M**19) + mu*(M**19.5)
    term2 = nu + eta*(M**2) + o*(M**8.5) + M**18.5 + pi*(M**19.5)

    return 500*(term1/term2)

def tout_lum(M):
    alpha = 0.397
    beta = 8.527
    gamma = 0.00026
    delta = 5.433
    sigma = 5.56
    eta = 0.788
    n = 0.0058

    term1 = alpha*M**5.5 + beta*M**11
    term2 = gamma + M**3 + delta*M**5 + sigma*M**7 + eta*M**8 + n*M**9.5

    return term1/term2

radius = odeint(derivatives, Rinit, mvalues)
luminosity = odeint(other_derivs, Rinit, mvalues)

#plt.plot(mvalues, radius, label="This Model")
#plt.plot(mvalues, tout_radius(mvalues), label = "Tout1996")
#plt.xlabel('Mass (Solar Mass)', fontsize=16)
#plt.ylabel('Radius', fontsize=16)
#plt.legend()
#plt.show()

plt.plot(mvalues, luminosity)
plt.plot(mvalues, tout_lum(mvalues))
plt.xlabel('Mass (Solar Mass)', fontsize=16)
plt.ylabel('Luminosity', fontsize=16)
plt.ylim(0, 400000)
plt.show()
