import matplotlib.pyplot as plt
import numpy as np
from fitter import Fitter, get_common_distributions, get_distributions 

data= open("data.txt","r")
l=data.readlines()
l_data=[float(i) for i in l]
mean=sum(l_data)/len(l_data)

print(f"Mean: {mean}  ,  Variance = {(sum([(i - mean)**2  for i in l_data])/len(l_data))**(0.5)}")
a1=np.arange(min(l_data),max(l_data)+1,0.02)

plt.hist(l_data,bins=a1)

f = Fitter(l_data, distributions= ['gamma', "lognorm", "beta","expon","norm"])
f.fit()
print(f.summary())
plt.show()


a=[]
b=[]
for i in l_data:
    if(i<mean):
        a.append(i)
    else:
        b.append(i)
a1=np.arange(min(l_data),max(l_data)+1,0.02)
plt.hist(a)

f = Fitter(a, distributions= ['gamma', "lognorm", "beta","expon","norm"])
f.fit()
print(f.summary())
plt.show()

a1=np.arange(min(l_data),max(l_data)+1,0.02)
plt.hist(b)

f = Fitter(b, distributions= ['gamma', "lognorm", "beta","expon","norm"])
f.fit()
print(f.summary())
plt.show()

meana=sum(a)/len(a)

print(f"Mean part 1: {meana}  ,  Variance part 1 = {(sum([(i - meana)**2  for i in a])/len(a))**(0.5)}")
meanb=sum(b)/len(b)
print(f"Mean part 2: {meanb}  ,  Variance part 2 = {(sum([(i - meanb)**2  for i in b])/len(b))**(0.5)}")

