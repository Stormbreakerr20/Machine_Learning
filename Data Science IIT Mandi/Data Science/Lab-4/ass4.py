######################################################################### 1
import matplotlib.pyplot as plt
import math

outcomes=[]
for i in range(1,7):
    for j in range(1,7):
        outcomes.append((i,j))
d={1:0}
for i in outcomes:
    if(sum(i) in d):
        d[sum(i)]+=1
    else:
        d[sum(i)]=1
        
probofX={i:d[i]/36 for i in d}
    
print(f"probabilities : {probofX}")
probofX[13]=0
print(f"Sum of probabilities: {round(sum(list(probofX.values())))}")

plt.plot(list(probofX.keys()),list(probofX.values()))
plt.xlabel("P(X=i)")
plt.ylabel("prob values")
plt.show()

# b
print()
def f(x,probofX):
    if(x>=12):
        return 1
    elif(x<=1):
        return 0
    ans =0
    for i in range(2,math.floor(x+1)):
        ans+=probofX[i]
    return ans

print(f(math.pi,probofX))
print(f(math.sqrt(30),probofX))

d1={i:f(i,probofX) for i in range(-1,21)}

plt.plot(list(d1.keys()),list(d1.values()))
plt.xlabel(" x values")
plt.ylabel("F(x)")
plt.show()

######################################################################### 2
import matplotlib.pyplot as plt
import numpy.random as rd
import numpy as np
import random


def prb(n):
    l=[]
    sum=0
    k=[1,-1]
    
    for j in range(1000):
        for i in range(abs(n)):
            r=rd.choice(k)
            sum+=r
        l.append(sum)
        sum=0
    prob=0
    for i in range(-abs(n),abs(n)+1):
        prob+=l.count(i)/1000
    print(f"Sum of P(-n)+P(-n+1)......+P(n) = {prob}")
    return l.count(n)/1000
# part b
prb(5)
prb(10)

# part c
d={i:prb(i) for i in range(-10,11)}
plt.plot(list(d.keys()),list(d.values()))
plt.show()

# part d
# for fixed values of steps let steps = 100
def prb1(n):
    l=[]
    sum=0
    k=[1,-1]
    
    for j in range(1000):
        p1=0.5
        for i in range(abs(100)):
            r=rd.choice(k)
            sum+=r
        l.append(sum)
        sum=0
    prob=0
    for i in range(-100,n):
        prob+=l.count(i)/1000
    return prob
dicr={i:prb1(i) for i in range(-10,11)}
plt.plot(list(d.keys()),list(d.values()))
plt.show()

# part e

def prb2(n):
    l=[]
    sum=0
    k=[1,-1]
    for j in range(1000):
        for i in range(abs(n)):
            r=rd.choice(k,p=[0.7,0.3])
            sum+=r
        l.append(sum)
        sum=0
    prob=0
    for i in range(-n,n+1):
        prob+=l.count(i)/1000
    print(f"Sum of P(-n)+P(-n+1)......+P(n) = {prob}")
    return l.count(n)/1000
prb2(10)
######################################################################## 3
def F(x,l):
    return  (math.pow(l, x)*math.pow(math.e, -l))/math.factorial(x)
def F2(x,l):
    ans=0
    for i in range(0,x+1):
        ans+=F(i,l)
    return ans

d3={i:F(i,1) for i in range(0,21)}
d4={i:F(i,4) for i in range(0,21)}
d5={i:F(i,10) for i in range(0,21)}
plt.plot(list(d3.keys()),list(d3.values()) ,label="for lambda = 1")
plt.plot(list(d4.keys()),list(d4.values()),label="for lambda = 4")
plt.plot(list(d5.keys()),list(d5.values()) ,label="for lambda = 10")
plt.legend()
plt.show()

d6={i:F2(i,1) for i in range(0,21)}
d7={i:F2(i,4) for i in range(0,21)}
d8={i:F2(i,10) for i in range(0,21)}
plt.plot(list(d6.keys()),list(d6.values()) ,label="for lambda = 1")
plt.plot(list(d7.keys()),list(d7.values()),label="for lambda = 4")
plt.plot(list(d8.keys()),list(d8.values()) ,label="for lambda = 10")
plt.legend()
plt.show()

# name = poissens distribution
# mean = expectation =sigma xp  where p is our function with x from 0 to infinite

mean=0  #for lambda =4
for i in range(0,100):
    mean+=i*F(i,4)
print(f"Mean: {mean}")
# as x increases while doing experiment mean tends to lamda hence mean=lambda
meanx2=0  #for lambda =4
for i in range(0,100):
    meanx2+=math.pow(i, 2)*F(i,4)
print(f"Variance: {meanx2 - math.pow(mean, 2)}")

# variance also approches lamda hence var = lamda
    
######################################################################### 4
def F3(p,n,k):
    return (math.factorial(n)*math.pow(p,k)*math.pow(1-p,n-k))/(math.factorial(k)*math.factorial(n-k))

def F4(p,n,k):
    ans=0
    for i in range(0,k+1):
        ans+=F3(p,n,i)
    return ans

di1={i:F3(0.5,20,i) for i in range(21)}
di2={i:F3(0.7,20,i) for i in range(21)}
di3={i:F3(0.5,40,i) for i in range(21)}

plt.plot(list(di1.keys()),list(di1.values()) ,label="for n=0.5 p=20")
plt.plot(list(di2.keys()),list(di2.values()) ,label="for n=0.7 p=20")
plt.plot(list(di3.keys()),list(di3.values()) ,label="for n=0.5 p=40")
plt.legend()
plt.show()

di4={i:F4(0.5,20,i) for i in range(21)}
di5={i:F4(0.7,20,i) for i in range(21)}
di6={i:F4(0.5,40,i) for i in range(21)}

plt.plot(list(di4.keys()),list(di4.values()) ,label="for n=0.5 p=20")
plt.plot(list(di5.keys()),list(di5.values()) ,label="for n=0.7 p=20")
plt.plot(list(di6.keys()),list(di6.values()) ,label="for n=0.5 p=40")
plt.legend()
plt.show()


