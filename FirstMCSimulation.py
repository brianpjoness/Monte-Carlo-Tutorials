
# risk neutral process

import math
import numpy as np
import pandas as pd
import datetime
import scipy.stats as stats
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# monte carlo simulates many different situations
# allows oyu to price complex derivatives

# risk neutral pricing for derivatives

# VaR is the value at risk
# CVaR is conditional value at risk, its the average loss assuming loss exceeds VaR threshold

# we can use variance reduction methods and quasi random numbers


# initial derivative parameters

vol = 0.0991 # vollatility (%)
r = 0.01 # ri
S = 101.15 # stock price
K = 98.01 # strike pricesk free reate %
N = 10 # number of time steps
M = 10000 # number of simulations - incrases the accuracy however computationally expensive

market_value = 3.86    # market price of option
T = ((datetime.date(2022, 3, 17)-datetime.date(2022, 1, 18)).days+1)/365    # time in years
print(T)

# Slow Solution

dt = T/N
nudt = (r-0.5*vol**2)*dt  # drift term
volsdt = vol* np.sqrt(dt)  # volatility times sqrt time
lnS = np.log(S)  # natural log of S

# Standard Error Placeholders
sum_CT = 0
sum_CT2 = 0

# Monte Caro Mehtod
# for i in range(M):   # goes through M simulati0ons
#     lnSt = lnS
#     for j in range(N):   # goes through the N time steps
#         lnSt = lnSt + nudt + volsdt*np.random.normal()   # St is the price of the asset at time t, its equal to what it was initialy at plus drift times volatility times random
#
#
#     ST = np.exp(lnSt)  # get the stock price since it was natural log beforea
#     CT = max(0, ST - K)   # option value
#     sum_CT = sum_CT + CT
#     sum_CT2 = sum_CT2 + CT*CT
#
#
# # Compute Expectation and Standard Error
# C0 = np.exp(-r*T)*sum_CT/M     # this is the discounted expected payoff to current value, multiplying by e^-rt accounts for the time value of money (think pert
# sigma = np.sqrt((sum_CT2 - sum_CT*sum_CT/M)*np.exp(-2*r*T)/(M-1))
# SE = sigma/np.sqrt(M)
#
# print("Call value is ${0} with SE +/- {1}".format(np.round(C0,2),np.round(SE,2)))



# Fast Solution - Vectorized     - runs faster

# precompute constants
dt = T/N
nudt = (r- 0.5*vol**2)*dt # drift is the average trend or direction, deterministic and long term growth expectaop
voldst = vol*np.sqrt(dt)

# Monte Carlo Method
Z = np.random.normal(size=(N, M))
delta_lnSt = nudt + voldst*Z   # small increments of stock price that are moving in time (by Z)
lnSt = lnS + np.cumsum(delta_lnSt, axis=0) # takes the sum of the changes of the small increments added to orignal price
lnSt = np.concatenate((np.full(shape=(1, M), fill_value=lnS), lnSt))

# compute expectation and SE
ST = np.exp(lnSt)
CT = np.maximum(0, ST - K)   # finds the max of stock price - stock price at the strike time , note it uses maximum since it is working with arrays
C0 = np.exp(-r*T)*np.sum(CT[-1])/M   # this is the discounted option price to account for inflation, it sums up the arrays and divides by the number of simulations as well

sigma = np.sqrt ( np.sum ((CT[-1] - C0)**2) / (M-1))  # CT[-1] is the option pay off, last row so its at time T
SE = sigma/np.sqrt(M)  # standard error is std / sqrt trials

print("Call value is ${0} with SE +/- {1}".format(np.round(C0,2),np.round(SE,2)))
