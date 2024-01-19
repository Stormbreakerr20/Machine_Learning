import numpy as np
import random
import matplotlib.pyplot as plt
mean=60000
std=10000
data= np.random.normal(mean,std,10000)
a=0
for i in data: 
    if i<70000 and i>50000:
        a+=1
print(f"probability that a randomly selected person from this population has an income between $50,000 and $70,000 per year: {a/10000}")


b=0

for i in range(100):
    l=[]
    for j in range(100):
        x=random.randint(0,10000-1)
        l.append(data[x])
    
    avg=sum(l)/len(l)
    if  avg>55000 and avg<65000:
        b+=1

print(f"probability that the average income of a random sample of 100 people from this population is between $55,000 and $65,000 per year: {b/100}")

plt.hist(data,bins =100)
# Add a vertical line at the mean
plt.axvline(mean, color='r', linestyle='dashed')
# Add a vertical line at the std
plt.axvline(mean +std, color='b', linestyle='dashed')
plt.axvline(mean -std, color='b', linestyle='dashed')
# Add a vertical line at the ranges
plt.axvline(np.max(data), color='g', linestyle='dashed')
plt.axvline(np.min(data), color='g', linestyle='dashed')

plt.show()


# A box plot is a graphical representation of the distribution of a dataset that shows the median, and outliers of the data. The box in the box plot represents the middle 50% of the data, and the "whiskers" extending from the box represent the minimum and maximum values that are not considered outliers.   
#  an outlier is a data point that is significantly different from the other data points in a dataset. Outliers can occur for various reasons, such as measurement error, data entry errors, or genuine but rare occurrences in the population being studied.

plt.boxplot(data)
plt.axhline(np.max(data), color='g', linestyle='dashed')
plt.axhline(np.min(data), color='g', linestyle='dashed')
plt.show()

# 
# The Central Limit Theorem (CLT) is a fundamental concept in statistics that states that the sampling distribution of the means of a large number of independent and identically distributed random variables will approximate a normal distribution, regardless of the shape of the original population distribution.

# In simpler terms, the CLT says that if you take many random samples of the same size from a population, and calculate the mean of each sample, the distribution of those sample means will tend to be normal, even if the original population distribution is not normal. This applies as long as the sample size is "large enough" (typically greater than 30).

def f(n):
    meanl=[]

    for i in range(1000):
        l=[]
        for j in range(n):
            x=random.randint(0,10000-1)
            l.append(data[x])
        mean= sum(l)/len(l)
        meanl.append(mean)
        
    meansample=sum(meanl)/len(meanl)
    stdsample=(sum([(i-meansample)**2 for i in meanl])/len(meanl))**0.5

    plt.hist(meanl,bins=100)
    # Add a vertical line at the mean
    plt.axvline(meansample, color='r', linestyle='dashed')
    # Add a vertical line at the std
    plt.axvline(meansample +stdsample, color='g', linestyle='dashed')
    plt.axvline(meansample -stdsample, color='g', linestyle='dashed')

    plt.show()
    
f(10)
f(50)
f(100)

