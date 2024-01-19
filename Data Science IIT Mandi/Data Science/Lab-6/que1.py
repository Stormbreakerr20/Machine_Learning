import math
import matplotlib.pyplot as plt
import numpy as np
# a
def pdf(x,mean , sd):
    n=(math.e)**(-math.pow(x-mean, 2)/2*math.pow(sd, 2))
    d=math.sqrt(2*math.pi)*sd
    return n/d

plt.plot([i for i in range(-100,110)],[pdf(i,0,1) for i in range(-100,110)])
plt.show()
# b
x= 0 + 1*(np.random.randn(1,100000))
#  x = mean + standard_dev*numpy

print(np.std(x))
print(np.mean(x))
a1=np.arange(x.min(),x.max()+1,0.02)
print(x.min())
print(x.max())
plt.hist(x,bins=a1)
plt.show()