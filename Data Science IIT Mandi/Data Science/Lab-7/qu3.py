import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
f= pd.read_csv('marks.csv')

marks=f['Marks'].tolist()

means=[]
var=[]
std=[]
for i in range(100):
    l=[]
    for j in range(50):
        x=random.randint(0,len(marks)-1)
        l.append(marks[x])
    means.append(sum(l)/len(l))
    var.append(sum([(i-(sum(l)/len(l)))**2 for i in l])/len(l))
    std.append((sum([(i-(sum(l)/len(l)))**2 for i in l])/len(l))**0.5)
    
print(f"Population Mean: {sum(means)/len(means)}")
print(f"Population Variance: {sum(var)/len(var)}")
print(f"Population Std: {sum(std)/len(std)}")

def f(n):
    m=[]
    for i in range(100):
        l=[]
        for j in range(n):
            x=random.randint(0,len(marks)-1)
            l.append(marks[x])
        m.append(sum(l)/len(l))
        
    plt.hist(m,bins=25)
    plt.show()


f(5)
f(10)
f(15)
f(25)