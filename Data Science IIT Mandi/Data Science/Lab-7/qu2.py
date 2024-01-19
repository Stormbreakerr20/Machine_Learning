# The Gamma distribution is a continuous probability distribution that is often used to model the waiting time for a certain number of events to occur. It has two parameters: shape (a) and scale (scale).
# The np.random.gamma function takes two arguments: shape and scale, and an optional third argument size to specify the size of the output array. The shape parameter controls the shape of the distribution, while the scale parameter controls the scale of the distribution.

import numpy as np
import random
import matplotlib.pyplot as plt

# The standard error is often used to calculate confidence intervals and perform hypothesis tests on population parameters based on sample statistics. A smaller standard error indicates that the sample statistic is a more precise estimate of the population parameter, and a larger standard error indicates more variability or uncertainty in the estimate.
# The formula for calculating the standard error of the mean is:
# SEM = s / sqrt(n)
# where s is the sample standard deviation and n is the sample size.

d={}

for i in range(10,10001):
    data=np.random.gamma(2,0.5,i)
    d[i]=[np.mean(data)]
    d[i].append((np.std(data))**2)

mean=[d[i][0] for i in d]
std=[d[i][1] for i in d]

stderror=[((d[i][1])**0.5)/((i)**0.5) for i in d]

fig, axs = plt.subplots(1, 3, figsize=(10, 5))


axs[0].plot(list(d.keys()),mean)
axs[0].set_title('Plot of Mean')

axs[1].plot(list(d.keys()),std)
axs[1].set_title('Plot of Variance')

axs[2].plot(list(d.keys()),stderror)
axs[2].set_title('Plot of Standard Error')

plt.show()


