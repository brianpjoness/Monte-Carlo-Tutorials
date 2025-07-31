
import math
from scipy.stats import norm

S = 40# Underlying Price
K = 40 # Strike Price
T = 0.5  # Time to Experiation
r = 0.10 # Risk free rate
vol = 0.6 # volatitlity (sigma)  essentially standard deviation

# European call or put option
d1 = (math.log(S/K) + (r + 0.5 * vol **2) * T) / (vol * math.sqrt(T))  # how sensitive option is to underlying

d2 = d1 -(vol * math.sqrt(T))   # risk nuetral probability that the call/put will be excercised

# calculate call option price
# weighted average of current price - strick price times risk free rate * probability call excercises in the money
C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
# cdf - cumalitive distribution function assuming normal distribution


# calculate put option price
# opposite of call option
P = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


print(f"Call Option Value: {round(C,2)}")
print(f"Put Option Value: {round(P,2)}")   # you want the premium (the price you payed for the option) to be greater than the price of the option