# # 1/2
import numpy as np
import matplotlib.pyplot as plt

l_1000=np.random.randint(100,size=1000)
l_2000=np.random.randint(100,size=2000)
l_5000=np.random.randint(100,size=5000)

mega_list=[l_1000,l_2000,l_5000]
n=[1000,2000,5000]
for j in range(len(mega_list)):
    d={}
    for i in mega_list[j]:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    keys=list(d.keys())
    values=list(d.values())
    bins=np.arange(0,101,2)
    plt.bar(keys,values)
    plt.xticks(bins)
    plt.xlabel(f"random values for n = {n[j]} ")
    plt.ylabel("frequency of values")
    plt.show()




# 3
def prob(n):
    d={"same_birthday":0,"no_same_birthday":0}
    for i in range(1000):
        birthdays=np.random.randint(366,size=n)
        birthdays=list(birthdays)
        # atleast 2 people same bday= 1-p(no two same)===> P(no two same) = (365/365)*(364/365)*(363/365)....= ((1/365)^n)*365*364....*365-n
        temp=[]
        for i in birthdays:
            if i not in temp:
                temp.append(i)
        
        if (len(temp)!=len(birthdays)):
            d["same_birthday"]+=1
        else:
            d["no_same_birthday"]+=1

    return d["same_birthday"]/1000



print("probability of atleast two same birthdays for n = 23 is: ",prob(23))
print("probability of atleast two same birthdays for n = 40 is: ",prob(40))
print("probability of atleast two same birthdays for n = 80 is: ",prob(80))
print("probability of atleast two same birthdays for n = 300 is: ",prob(300))
# as the no. of people increase P(atleast two same ) --> 1

d={i:prob(i) for i in range(1,301)}
d_keys=list(d.keys())
d_values=list(d.values())
xtick=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
plt.plot(d_values,d_keys)
plt.xticks(xtick)
plt.yticks([i for i in range(0,301,25)])
plt.xlabel("Probability")
plt.ylabel("No. of people for experiment")
plt.show()



min_n=0
for i in d:
    if d[i]>=0.8:
        min_n=i
        break
print(f"minimum n for which p>=0.8 => {min_n}")
print()

# 4

# 1 venus day =243 earth days
#  daytime =122 days night=121 days  
#  p(daytime)=2/3, p(night)=1/3

# np.random.choice(a,size,replace,p)
# np.arange(a) is executed by 1 , size = final size req ,p=probability of each ele

def prob_venus(n):
    d={"same_bday":0,"not_same_bday":0}
    for i in range(1000):
        l=np.random.choice(243,n,p=[(2/3)/122 if i<=122 else (1/3)/121 for i in range(1,244)])
        temp=[]
        for i in l:
            if i not in temp:
                temp.append(i)
        
        if len(l)!=len(temp):
            d["same_bday"]+=1
        else:
            d["not_same_bday"]+=1
            
    return d["same_bday"]/1000


print("probability of atleast two same birthdays on venus for earth days, for n = 23 is: ",prob_venus(23))
print("probability of atleast two same birthdays on venus for earth days, for n = 40 is: ",prob_venus(40))
print("probability of atleast two same birthdays on venus for earth days, for n = 80 is: ",prob_venus(80))

d1={i:prob_venus(i) for i in range(1,244)}
d1_keys=list(d1.keys())
d1_values=list(d1.values())
xtick=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
plt.plot(d1_values,d1_keys)
plt.xticks(xtick)
plt.yticks([i for i in range(0,301,25)])
plt.xlabel("Probability On Venus")
plt.ylabel("No. of people for experiment")
plt.show()
