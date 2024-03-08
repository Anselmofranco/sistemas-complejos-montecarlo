#Resolución de problema de accidentología planteado en el artículo:
#https://creandoconciencia.org.ar/enciclopedia/accidentologia/modelos-fisicos-matematicos/El-Metodo-MONTE-CARLO.pdf
#a través de la generaciónd e números pseudoaleatorios y método de montecarlo.
#mu son coeficientes de rozamiento.
#v_p velocidad del auto peugeot estimada por histograma.

import numpy.random as rnd

import matplotlib.pyplot as plt

g=9.81
mu_ies=rnd.random(100000)*0.2 + 0.7
mu_p=rnd.random(100000)*0.2 + 0.7
m_ies=rnd.random(100000)*100 + 1300
m_p=rnd.random(100000)*100 + 500

x=rnd.random(100000)*3-1.5
r_1=mu_p*(14.3-x)
r_2=mu_p*(11.31-x) 
r_3=((11.31-x)**2) + 4.93**2
v_p=3.6*(2*g*(mu_ies*(13.6+x)+((r_1)**0.5+(m_ies/m_p)*((r_2**0.5)/(r_3**0.25)))**2))**0.5


plt.figure(1)
plt.hist(v_p,100)
