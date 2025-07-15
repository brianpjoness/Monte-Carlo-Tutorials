
import math
import numpy as np
import pandas as pd
import datetime
import scipy.stats as stats
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr


# this model is simple as heck

sims = 100000

A = np.random.uniform(1,5, sims)
B = np.random.uniform(2, 6, sims)

duration = A+B

plt.figure(figsize=(3, 1.5))
plt.hist(duration, density=True)
plt.axvline(9, color="r")
plt.show()

print((duration>9).sum()/sims)