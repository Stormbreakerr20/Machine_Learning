# 1 theorotical p(A/B)= 0.161

# p (test positive ) = p(B int A) +P(B int notA)=0.059
import matplotlib.pyplot as plt
import random
def prob(n):
    population_h_or_d=[1 for i in range(n)]
    test_p_or_n=[0 for i in range(n)]
    
    # 1=healthy 0=infected
    # 1=pos 0=neg
    for i in range(n//100):
        x=random.randint(0,n-1)
        while population_h_or_d[x]==0:
            x=random.randint(0,n-1)
        population_h_or_d[x]=0
        
        
    d_index=[]
    h_index=[]
    for i in range(n):
        if population_h_or_d[i]==0:
            d_index.append(i)
        else:
            h_index.append(i)
    # 1% with infection
    
    for i in range(round(len((d_index))*0.95)):
        x=random.randint(0,len(d_index)-1)
        while test_p_or_n[d_index[x]]==1:
            x=random.randint(0,len(d_index)-1)
        test_p_or_n[d_index[x]]=1
        
    for i in range(round(len((h_index))*0.05)):
        x=random.randint(0,len(h_index)-1)
        while test_p_or_n[h_index[x]]==1:
            x=random.randint(0,len(h_index)-1)
        test_p_or_n[h_index[x]]=1
            
            
    p=0

    for i in range(n):
        if test_p_or_n[i]==1 and population_h_or_d[i]==0:
            p+=1


    if(p==0):
        return 0
    return p/test_p_or_n.count(1)
            

print(f"probability person actually has disease given tested positive for n= 1000 ==> {prob(1000)}")
print(f"probability person actually has disease given tested positive for n= 10000 ==> {prob(10000)}")
print(f"probability person actually has disease given tested positive for n= 100000 ==> {prob(100000)}")

d={i:prob(i) for i in range(1,10001)}
d_keys=list(d.keys())
d_values=list(d.values())

ytick=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
plt.plot(d_keys,d_values)
plt.yticks(ytick)
# plt.xticks([i for i in range(0,100000)])
plt.ylabel("Probability")
plt.xlabel("No. of people for experiment")
plt.show()



