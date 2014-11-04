import sys
import math

l_values = [1., 10., 100.] # pc
p_over_m = 17.7 # km s^-1 / unit stellar mass
sigma_1 = 1 # km s^-1
mass_1 = 100 # m_sun
G = 6.67e-11 #m^3 kg^-1 s^-2
#G = 6.67e-8 #cm^3 g^-1 s^-2


pc_to_m = 3.08e16 # m
pc_to_km = 3.08e13 # km
sec_in_year = 3.155e7 # secs
msun_to_kg = 1.989e30 # kg

def calc_tff(l):
    mass = (mass_1*(l)**2)*msun_to_kg
    rho = mass/(l*pc_to_m)**3
    return math.sqrt((3*math.pi)/(32*G*rho))

def get_m_dot_cluster(l):
    sigma = sigma_1*(l)**0.5
    mass = mass_1*(l)**2
    return ((mass*sigma**2) / (l*pc_to_km))*(1/p_over_m)

def cloud_to_star(m_dot_cluster, l):
    tff = calc_tff(l) # secs
    mass = mass_1*(l)**2 #m_sun
    return (m_dot_cluster*tff) / mass

for value in l_values:
    print "For: ", value
    m_dot_cluster =  get_m_dot_cluster(value)

    print "M_dot_cluster is: ", m_dot_cluster
    print cloud_to_star(m_dot_cluster, value)
