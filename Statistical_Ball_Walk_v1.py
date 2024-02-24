
"""

- Statistical Walk -
     -Neil Pohl-
  Created: 2/23/2024


"""
import random
import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit 

"""
Balls = The number of balls being dropped in the plinko
Layers = The number plinko layers
Baskets = The number of places where the ball can land
Ballsinbasket = The number of times a ball landed in a basket
"""
balls=1000000
layers=100
baskets=[]
ballsinbasket=[]

for i in range(layers+1):
    ballsinbasket.append(0)
    baskets.append(-(layers/2)+i)
for i in range(balls):
    position=0
    for i in range(layers):
        position=position+random.choice([0,1])
    ballsinbasket[position]=ballsinbasket[position]+1
def gauss(x, A, sigma): 
    return A * np.exp(-(1/2)*(x/sigma)**2)
ballsinbasket = [x / max(ballsinbasket) for x in ballsinbasket]
popt, pcov = curve_fit(gauss, baskets, ballsinbasket)
plt.plot(baskets,ballsinbasket,'o')
plt.plot(baskets,gauss(baskets,popt[0],popt[1]))
plt.show()

print("Square Root of Layers: ",np.sqrt(layers))
print("2x Standard Deviation of Gauss: ",2*popt[1])

