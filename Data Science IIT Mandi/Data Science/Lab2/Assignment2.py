# 1
# a=event that the tested person has the disease
# b = event that the test result is positive

# find  p(a/b)

p_b_given_a=0.99
p_b_given_not_a=0.005

p_a=0.001

# p(a/b)=p(b/a)*p(a)/p(b)       p(b/a)=0.99   p(a)=0.001    p(not a) =1-p(a)=0.999

# p(b)  = p(b int a) +p (b int nota)  =  p(b/a)p(a) +p(b/nota)p(nota)

p_a_given_b = (p_b_given_a*p_a)/(p_b_given_a*p_a +p_b_given_not_a*(1-p_a))

print(p_a_given_b)

print()
 
# 2
import math
import random

def Nsided_dice(n):
    S=[]
    E1=[]
    E2=[]
    E3=[]
    E4=[]
    
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            S.append((i,j))
            
            
            if((i+j)==n):
                E1.append((i,j))
                
            if(i==math.floor(n/2)):
                E2.append((i,j))
                
            if((i+j)>n+math.floor(n/2)):
                E3.append((i,j))
                
            if(((i+j)==n)and ((i+j)>n+math.floor(n/2)) ):
                E4.append((i,j))
                
    P_E1= len(E1)/len(S)
    P_E2= len(E2)/len(S)
    P_E3= len(E3)/len(S)
    P_E4= len(E4)/len(S)
                
                
    print(S)
    print(E1)
    print(E2)
    print(E3)
    print(E4)
    print(P_E1)
    print(P_E2)
    print(P_E3)
    print(P_E4)
    
    # event 1 and 2 are not independent as occurance of [n/2] on first dice in event 1 will affect the probability of event-2 
    # if we take out cases when sum =n from event 1 then there can be a change in p of event 2
    # independent = p(a int b)=0
    
    # mutually exculsive are generally dep on each other but they cannot occur at same time like drawing two card from deck 
    # when p(a int b)=0 they become independent
    
    # event 1 and 3 are independent as p(a int b ) =0 
Nsided_dice(10)



# 3
print()
def prob_dice(n,k,d):
    S=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            S.append((i,j))
    
    outcomes=[]
    
    for j in range(k):
        x=random.randint(0,n*n-1)
        outcomes.append(S[x])

    c1=0
    c2=0
    c3=0
    c4=0   
    e1=[]
    e2=[]
    e3=[]
    e4=[]
    
    for i in outcomes:
        if(sum(i)==n):
            c1+=1
            e1.append(i)
        if(i[0]==math.floor(n/2)):
            c2+=1
            e2.append(i)
        if(sum(i)>n+math.floor(n/2)):
            c3+=1
            e3.append(i)
        if((sum(i)==n)and (sum(i)>n+math.floor(n/2)) ):
            c4+=1
            e4.append(i)
    
    d['p1'][k]=c1/k           
    d['p2'][k]=c2/k           
    d['p3'][k]=c3/k           
    d['p4'][k]=c4/k         
    if(len(e1)==0 or len(e2)==0):
        d["e1e2"].append("Yes")
    else:
        t=0
        for i in e1:
            if i in e2:
                d["e1e2"].append("No")
                t=1
                break
        if(t==0):
            d["e1e2"].append("Yes")
            
    if(len(e4)==0):
        d["e3e4"].append("Yes")
    else:
        for i in e4:
            if i in e3:
                d["e3e4"].append("No")
                break
            if(e4.index(i)==len(e4)-1):
                d["e3e4"].append("Yes")
        
    
    
    
d={'p1':{10:0,50:0,100:0,1000:0,5000:0},'p2':{10:0,50:0,100:0,1000:0,5000:0},'p3':{10:0,50:0,100:0,1000:0,5000:0},'p4':{10:0,50:0,100:0,1000:0,5000:0},"e1e2":[],"e3e4":[]}
prob_dice(6,10,d)
prob_dice(6,50,d)
prob_dice(6,100,d)
prob_dice(6,1000,d)
prob_dice(6,5000,d)


print('p1: ',d['p1'])
print('p2: ',d['p2'])
print('p3: ',d['p3'])
print('p4: ',d['p4'])
print('E1 E2 are independent? : ',d['e1e2'])
print('E3 E4 are independent? : ',d['e3e4'])
        
    
    
     