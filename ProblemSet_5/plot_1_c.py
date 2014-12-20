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
Mdot = 10e-5*(solar_g/yr_sec)


Rinit = 2.5
mvalues = np.linspace(0.01, 1, 1000)
#Rinit = 2.5*6.955e10
#mvalues = np.linspace(0.01*solar_g, 1*solar_g, 1000)

def bb_luminosity(radius):
    return 4*np.pi*(radius**2)*sigma*(3500**4)

def derivatives(mass, radius):
    term1 = ((radius*6.955e10)**2)/(3*G*(mass*solar_g)**2)*bb_luminosity(radius*6.955e10)
    term2 = ((0.25*Mdot)/3)*((radius*6.955e10)/(mass*solar_g))
    term3 = ((2*Mdot)/7)*((radius*6.955e10)/(mass*solar_g))
    term4 = ((84.2*ev_ergs)*Mdot/(m_p*3*G))*((radius*6.955e10)**2)/((mass*solar_g)**2)

    return (term1 + term2 + term3 + term4)

def other_derivs(mass, radius):
    return bb_luminosity(radius*6.955e10) - (0.25*G)*((mass*solar_g)/(radius*6.955e10))

radius = odeint(derivatives, Rinit, mvalues)
luminosity = odeint(other_derivs, Rinit, mvalues)

plt.plot(mvalues, radius)
plt.xlabel('Mass (Solar Mass)', fontsize=16)
plt.ylabel('Radius', fontsize=16)
plt.show()

plt.plot(mvalues, luminosity)
plt.xlabel('Mass (Solar Mass)', fontsize=16)
plt.ylabel('Luminosity', fontsize=16)
plt.show()
