import numpy.random as rd
import random
def prb(n):
    l=[]
    sum=0
    k=[1,-1]
    
    for j in range(1000):
        p1=0.5
        for i in range(n):
            r=rd.choice(k,p=[p1,1-p1])
            sum+=r
            if(r==1):
                p1+=random.random()/random.randint(20,50)
        l.append(sum)
        sum=0
    print(l)
    prob=0
    for  i in range(-n,n+1):
        prob+=l.count(i)/1000
    return prob