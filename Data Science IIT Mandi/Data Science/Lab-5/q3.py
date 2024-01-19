
import math
import matplotlib.pyplot as plt
import numpy as np

E_r1=0.4*(-10)+0.2*(10)+0.4*(20) 
E_r2=0.4*(5)+0.2*(20)+0.4*(10)

v_r1=0.4*((E_r1/100-(-0.1))**2)+0.2*((E_r1/100-0.1)**2)+0.4*((E_r1/100-0.2)**2)
v_r2=0.4*((E_r2/100-(0.05))**2)+0.2*((E_r2/100-0.2)**2)+0.4*((E_r2/100-0.1)**2)

sd1=math.sqrt(v_r1)
sd2=math.sqrt(v_r2)

print("from stock1,\nexpected return:",E_r1,"\nvariance:",v_r1,"\nStandard Deviation:",sd1*100)
print("\nfrom stock2,\nexpected return:",E_r2,"\nvariance:",v_r2,"\nStandard Deviation:",sd2*100)


print("For Stock 1:")
N=[100,200,500,1000]
for i in N:
    data=np.random.choice([-0.1,0.1,0.2],size=i,p=[0.4,0.2,0.4])
    mean=np.mean(data)
    variance=np.var(data)
    sd=np.std(data)
    print(f"for N={i},mean={mean*100},variance={variance},standard deviation={sd*100}")
    
print("For Stock 2:")
for i in N:
    data=np.random.choice([0.05,0.2,0.1],size=i,p=[0.4,0.2,0.4])
    mean=np.mean(data)
    variance=np.var(data)
    sd=np.std(data)
    print(f"for N={i},mean={mean*100},variance={variance},standard deviation={sd*100}")

def E_p(w1,w2):
    return w1*E_r1+w2*E_r2

def cov(E_r1,E_r2):
    return 0.4*(-0.1-E_r1/100)*(0.05-E_r2/100)+0.2*(0.1-E_r1/100)*(0.2-E_r2/100)+0.4*(0.2-E_r1/100)*(0.1-E_r2/100)

cov=cov(E_r1,E_r2)

def sd_p(w1,w2,sd1,sd2,cov):
    # variance (aX+bY)=a**2 * var(x) + b**2 *var(y) +2ab*cov(x,y)
    return ((w1**2)*((sd1/100)**2)+(w2**2)*((sd2/100)**2)+2*w1*w2*cov)*10000


w1=np.arange(0.1,0.9,0.1)
w2=[1-i for i in w1]
xlist=[]
ylist=[]

for i in w1:
    xlist.append(E_p(i,1-i))
    ylist.append(sd_p(i,1-i,sd1,sd2,cov))

best=[]
for i in w1:
    if E_p(i,1-i)==max(xlist):
        best.append(i)
        best.append(1-i)



n=1000
data1=np.random.choice([-0.1,0.1,0.2],size=n,p=[0.4,0.2,0.4])
data2=np.random.choice([0.05,0.2,0.1],size=n,p=[0.4,0.2,0.4])
M1=np.mean(data1)
M2=np.mean(data2)
strddev1=np.std(data1)
strddev2=np.std(data2)

cov2=0.4*(-0.1-M1)*(0.05-M2)+0.2*(0.10-M1)*(0.20-M2)+0.4*(0.20-M1)*(0.10-M2)
std_rdm=sd_p(best[0],best[1],strddev1,strddev2,cov2)
Exp_rtr=(best[0]*M1+best[1]*M2)*1006

print(f"by theoritically,we got : risk={sd_p(best[0],best[1],sd1,sd2,cov)} and return={E_p(best[0],best[1])}")
print(f"BY sampling the best combination,,we got: risk={std_rdm} and return={Exp_rtr}")



plt.plot(xlist,ylist)
plt.show()




