import numpy as np
import matplotlib.pyplot as plt

#expectation = summation(x(p(X)))
expectation_A = 0.4*(-10) +0.2*(10) +0.4*(20)
expectation_B = 0.4*(5) +0.2*(20) +0.4*(10)
variance_A = 0.4*((-10-expectation_A)**2) +0.2*((10-expectation_A)**2) +0.4*((20-expectation_A)**2)
variance_B = 0.4*((5-expectation_B)**2) +0.2*((20-expectation_B)**2) +0.4*((10-expectation_B)**2)
covaiance_AB = 0.4*((-10-expectation_A)*(5-expectation_B)) +0.2*((10-expectation_A)*(20-expectation_B)) +0.4*((20-expectation_A)*(10-expectation_B))
print("the expected return of b is : ",expectation_B)
print("the expected return of a is : ",expectation_A)
print("the variance of a is : ",variance_A)
print("the variance of b is : ",variance_B)
standard_deviation_A = (variance_A)**0.5
standard_deviation_B = (variance_B)**0.5
print("the standard deviation of a is: ",standard_deviation_A)
print("the standard deviation of b is: ",standard_deviation_B)


def expected_return( n,pa,pb,pc,ra,rb,rc):
    a = np.random.choice([ra,rb,rc],size=n,p = [pa,pb,pc])
    total_return = 0
    for item in a:
        if(item == ra):
            total_return = total_return + ra
        elif(item == rb):
            total_return = total_return +rb
        else:
            total_return = total_return + rc
    return total_return/n            

def expected_variance(n,pa,pb,pc,ra,rb,rc):
    a = expected_return(n,pa,pb,pc,ra,rb,rc)
    b = np.random.choice([ra,rb,rc],size=n,p = [pa,pb,pc])
    for i in range (len(b)):
        b[i] = (b[i] -a)**2
    return sum(b)/n    
        
        
            
print(expected_return(10000,0.4,0.2,0.4,-10,10,20),"expected return by simulation of a")            
print(expected_variance(10000,0.4,0.2,0.4,-10,10,20),"expected variance of a by simulation")



# by theoritical calculations
# expected return on a = 6
# expected return on b = 10
# variance on a = 184
# variance on b  = 30
# covariance of a ,b is 40

# when w1 = 0.4,w2 = 0.6
# expected return = 8.4
# variance or risk = 59.44

# when w1 = 0.5,w2 = 0.5
# expected return = 8
# variance or risk = 73.5

# when w1 = 0.6,w2 = 0.4
# expected return = 7.6
# variance or risk = 90.24



# print(expected_return_by_simulation(10000,0.4,0.6,6,10))
# print(expected_variance_by_simulation(10000,0.4,0.6,6,10))

def expected_return_on_various_weights_of_a_and_b(wa):
    return ((wa*expectation_A) +((1-wa)*expectation_B))

def expected_variance_on_various_weights_of_a_and_b(wa):
    return ((wa**2)*variance_A  + ((1-wa)**2)*variance_B  +2*wa*(1-wa)*covaiance_AB)

list_weights = [0.1,0.2,0.3,0.4,0.5,0.7,0.8,0.9]
return_value = []
risk_value = []
for item in list_weights:
    return_value.append(expected_return_on_various_weights_of_a_and_b(item))
    risk_value.append(expected_variance_on_various_weights_of_a_and_b(item))
    
plt.plot(risk_value,return_value)
plt.xlabel("risk_value------------------>")
plt.ylabel("return value ---------------------->")
plt.grid(True)
plt.show()

# (0.1,0.9) combination would be best as it has minimum risk and max return value 

# risk and return for 0.1,0.9