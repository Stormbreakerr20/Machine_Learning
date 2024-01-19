import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

f=pd.read_csv('IC252marks.csv')

m=f['Mid sem 1'].tolist()
serial=[i for i in range(1,len(m)+1)]
print(m)
print(len(m))
print(serial)

mean=sum(m)/len(m)
sd=(sum([(i-mean)**2 for i in m])/len(m))**(0.5)
print(f"Mean: {mean}")
print(f"Standard Dev: {sd}")

s1=mean+(sd)
s1_=mean-(sd)
s2=mean+2*(sd)
s2_=mean-2*(sd)
s3=mean+3*(sd)
s3_=mean-3*(sd)
c1=0
c2=0
c3=0
for i in m:
    if(i>s1_ and i<s1):
        c1+=1
    if(i>s2_ and i<s2):
        c2+=1
    if(i>s3_ and i<s3):
        c3+=1
print(f"Percentage that follows sigma1: {(c1/len(m))*100} %, sigma2: {(c2/len(m))*100} %, sigma3: {(c3/len(m))*100} %")

# 3 sigma state for 1 sd 68.2%  for 2 sd 95.5% and for 3 sd 99.7% newmst lie in respective region but here it does not follow rule entirely

# b
grades={"O":[],"A":[],"B":[],"C":[],"D":[],"E":[],"F":[]}
for i in range(len(m)):
    if(m[i]>mean+1.5*sd):
        grades["O"].append(serial[i])
    elif(m[i]<mean+1.5*sd and m[i]>mean +sd):
        grades["A"].append(serial[i])
    elif(m[i]<mean+sd and m[i]>mean+0.5*sd):
        grades["B"].append(serial[i])
    elif(m[i]<mean+0.5*sd and m[i]>mean):
        grades["C"].append(serial[i])
    elif(m[i]<mean and m[i]>mean-0.5*sd):
        grades["D"].append(serial[i])
    elif(m[i]<mean-0.5*sd  and m[i]>mean-sd):
        grades["E"].append(serial[i])
    elif(m[i]<mean-sd and m[i]>mean-1.5*sd):
        grades["F"].append(serial[i])
        
# c

new = np.random.normal(mean, sd, 250)
# mean and standard deviation
newm, std = norm.fit(new) 
  
# Plot the histogram.
plt.hist(new, bins=25, density=True, alpha=0.6, color='b')
plt.hist(m, bins=25, density=True, alpha=0.6, color='g')
  
# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, newm, std)
  
plt.plot(x, p, 'k')
  
plt.show()

# standardize: mean=0 and std=1 each value = (x-mean)/std
val=[]
for i in m:
    val.append((i-mean)/sd)
    
mean1=sum(val)/len(val)
sd1=(sum([(i-mean1)**2 for i in val])/len(val))**(0.5)
print(f"Mean for Z-trans: {mean1}")
print(f"Standard Dev for Z-trans: {sd1}")