import pandas as pd

# 1
df=pd.read_csv('data.csv')

cloudy=df['Cloudy'].tolist()
rain=df['Rain'].tolist()
snow=df['Snow'].tolist()

print(f"day is cloudy = {(cloudy.count(1))/100}")
print(f"day is rainy = {(rain.count(1))/100}")
print(f"day is snowing = {(snow.count(1))/100}")


P_r_given_c=0

for i in range(100):
    if(cloudy[i]==1 and rain[i]==1):
        P_r_given_c+=1
    
print(f"Probability it will rain given cloudy = {P_r_given_c/(cloudy.count(1))}")

P_c_given_r=0

for i in range(100):
    if(cloudy[i]==1 and rain[i]==1):
        P_c_given_r+=1
    
print(f"Probability it is cloudy given raining = {P_c_given_r/rain.count(1)}")


# by law p_r_given_c = p_c_given_r(p_r/p_c)
print()
print(f"p_c_given_r*(p_r/p_c) = {(P_c_given_r/rain.count(1))*((rain.count(1))/100)/(cloudy.count(1)/100)}  which is equal to P_r_given_c")


P_r_given_notc=0

for i in range(100):
    if(cloudy[i]==0 and rain[i]==1):
        P_r_given_notc+=1
    
print(f"Probability it is rain given not cloudy = {P_r_given_notc/(cloudy.count(0))}")

P_r_or_s_given_c=0

for i in range(100):
    if(cloudy[i]==1 and (rain[i]==1 or snow[i]==1)):
        P_r_or_s_given_c+=1
        
print(f"Probability it is rain or snow given cloudy = {P_r_or_s_given_c/(cloudy.count(1))}")

P_r_and_s_given_c=0

for i in range(100):
    if(cloudy[i]==1 and (rain[i]==1 and snow[i]==1)):
        P_r_and_s_given_c+=1
        
print(f"Probability it is rain and snow given cloudy = {P_r_and_s_given_c/(cloudy.count(1))}")