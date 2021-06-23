# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:43:16 2021

@author Ryeder, C/O 2022 UCLA Groupmate
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def SIR_1(y,t):
  S,I,R=y; 
  dydt=[A-beta*S*I-mu*S,beta*S*I-gamma*I-mu*I, gamma*I-mu*R]
  return dydt

def SVEIR(y,t):
  S,V,E,I,R=y; 
  dS=(r*N*(1-(N/K)))-(beta*S*I/N)-(S*(zeta1+mu))+(omega*V);
  dV=(zeta1*S)-((1-epsilon)*beta*V*I/N)-((zeta2+mu+omega)*V);
  dE=(beta*S*I/N)+((1-epsilon)*beta*V*I/N)-((sigma+mu)*E);
  dI=(sigma*E)-((mu+alpha+tau)*I);
  dR=(tau*I)+(zeta2*V)-(mu*R)
  dydt=[dS, dV, dE, dI, dR];
  return dydt


A=.04  #birthrate
beta=0.1*(10**-2)  #transmission rate
mu=4.215*(10**-5)  #death rate
gamma=0.048 #recovery rate
s0=750;  #intial susceptible pop
i0=175;  #inital infected pop
r0=75; #initial recovered pop
N0=s0+i0+r0;  #intial total pop

t=np.linspace(0,100,100)   #time interval, third arg is how many steps
print(beta)

y0=[s0,i0,r0];
sol=odeint(SIR_1,y0,t)
plt.plot(t,sol[:,0],'r',label='S(t)')
plt.plot(t,sol[:,1],'b',label='I(t)')
plt.plot(t,sol[:,2],'g',label='R(t)')
plt.legend(loc='best');
plt.xlabel('t');
plt.grid();
plt.show();

N=1000  #population
r=.01  #rate of birth
K=10000 #pop limit
beta=0.1*(10**-2)  #transmission rate from susceptible to exposed
mu=4.215*(10**-5)  #death rate from susceptible pop
tau=0.048 #recovery rate from infected
zeta1=.2  #vax 1 rate
zeta2=.2  #vax 2 rate, after getting vax 2 automatically moved to recovered
omega=.1*(10**-6) #rate from vax1 to susceptible
epsilon=0.1 #rate from vax1 to infected
sigma=.5  #rate from exposed to infected
alpha=4.215*(10**-4)  #death rate from infected pop

s0=750;  #intial susceptible pop
i0=175;  #inital infected pop
r0=100; #initial recovered pop
v0=75;
e0=350;

t=np.linspace(0,20,1000)

y0=[s0,v0,e0,i0,r0];
sol=odeint(SVEIR,y0,t)
plt.plot(t,sol[:,0],'r',label='S(t)')
plt.plot(t,sol[:,1],'b',label='V(t)')
plt.plot(t,sol[:,2],'g',label='E(t)')
plt.plot(t,sol[:,3],label='I(t)')
plt.plot(t,sol[:,4],label='R(t)')
plt.legend(loc='best');
plt.xlabel('t');
plt.grid();
plt.show();

"""
A=.04  #birthrate, same for all pops
mu=4.215*(10**-5)  #death rate, same for all pops

beta1=0.1*(10**-3)  #transmission rate from S_1 to I_1
gamma1=0.048 #recovery rate in pop1, I_1 to R_1
tau_12=0.03 #travel rate between R_1, S_1 to R_2, S_2
iota_12=0.005  #travel rate between I_1 to I_2
tau_13=0.02 #travel rate between R_1, S_1 to R_3, S_3
iota_13=0.002  #travel rate between I_1 to I_3
s1_0=750;  #intial susceptible pop1
i1_0=175;  #inital infected pop1
r1_0=75; #initial recovered pop1

beta2=0.15*(10**-3)  #transmission rate from S_2 to I_2
gamma2=0.04 #recovery rate in pop2, I_2 to R_2
tau_23=0.03 #travel rate between R_2, S_2 to R_3, S_3
iota_23=0.005  #travel rate between I_2 to I_3
tau_21=0.02 #travel rate between R_2, S_2 to R_1, S_1
iota_21=0.001  #travel rate between I_2 to I_1
s2_0=900;  #intial susceptible pop2
i2_0=175;  #inital infected pop2
r2_0=55; #initial recovered pop2

beta3=0.15*(10**-3)  #transmission rate from S_3 to I_3
gamma3=0.04 #recovery rate in pop3, I_3 to R_3
tau_32=0.03 #travel rate between R_3, S_3 to R_2, S_2
iota_32=0.005  #travel rate between I_3 to I_2
tau_31=0.02 #travel rate between R_3, S_3 to R_1, S_1
iota_31=0.001  #travel rate between I_3 to I_1
s3_0=900;  #intial susceptible pop3
i3_0=175;  #inital infected pop3
r3_0=55; #initial recovered pop3

def SIR_3(y,t):
  S_1,I_1,R_1,S_2,I_2,R_2,S_3,I_3,R_3=y; 
  dS_1=A-beta1*I-mu
  dydt=[A-beta*I-mu*I*S,beta*S*I-gamma*I-mu*I, gamma*I-mu*R]
  return dydt
"""
