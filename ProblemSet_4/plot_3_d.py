import math
import numpy as np
import matplotlib.pyplot as plt

star_mass = 1.98e33
disk_mass = 0.03*star_mass
au = 1.496e13

kappa = 3 #cm^2 g^-1
alpha = 0.01
stefan_boltzmann = 5.67e-5
boltzmann = 1.38e-16
mu = 0.6 # all ionized gas
m_h = 1.67e-24
G = 6.67e-8

radius = np.linspace(1, 20)*au


def calc_c_s(tm, k):
    term1 = k*tm
    term2 = mu*m_h
    return np.sqrt(term1/term2)

def Omega_is(m, r):
    return np.sqrt((G*m)/r**3)

def H_is(c_s, Omega):
    return c_s / Omega

def Sigma_is(m, r):
    return m/r**2

def tm_is(m, r):
    term1 = kappa/(mu*m_h)
    term2 = (Sigma_is(m, r)*Omega_is(m, r)*kappa)/stefan_boltzmann
    return (3./4.)*(term1*term2)**(1./3.)

def ts_is(m, r, tm):
    return tm*((3./8.)*kappa*Sigma_is(m, r))**(1./4.)

def Q_is(m, r):
    term1 = Omega_is(m, r)*calc_c_s(tm, boltzmann)
    term2 = math.pi*G*Sigma_is(m, r)
    return term1/term2

tm = tm_is(disk_mass, radius)
ts = ts_is(disk_mass, radius, tm)
Q = Q_is(star_mass, radius)

plt.plot(radius, Sigma_is(disk_mass, radius)/H_is(calc_c_s(tm, kappa), Omega_is(star_mass, radius)), label='Density')
plt.plot(radius, tm, label='Midplane Temperature')
plt.plot(radius, ts, label='Surface Temperature')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
plt.plot(radius, Q, label='Toomre Q')
plt.axhline(1, 0, 1, lw=3, color='k')
#plt.xscale('log')
#plt.yscale('log')
plt.legend()
plt.show()
