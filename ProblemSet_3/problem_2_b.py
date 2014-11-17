import math

m_max = 1.18 # dimensionless units
G =  6.67e-11 #m^3 kg^-1 s^-2
m_be = 0.074
m_h = 1.67e-27
mu = 2.33
kb = 1.38e-23
m_sun = 1.9891e30

def calc_cs(temperature):
    top = kb*temperature
    bottom = mu*m_h
    return math.sqrt(top/bottom)

temperature = 10 # K
cs = calc_cs(temperature)
top = m_max**2 * cs**6
bottom = mu * m_h * G**3 * (m_be*m_sun)**2

print "N_min is ", top/bottom


