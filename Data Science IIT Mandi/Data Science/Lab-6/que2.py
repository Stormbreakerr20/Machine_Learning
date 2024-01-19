from scipy.integrate  import quad
import math
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    if(x>0 and x<2):
        return (4*x-2*x**2)/(math.e)**(x)
    return 0
# 1
y=quad(f,-np.inf,np.inf)

ans = y[0]-y[1]
c=1/ans
print(f"value of C: {c}")

# b
plt.plot([i for i in range(-20,21)],[c*f(i) for i in range(-20,21)])
plt.show()

# c
prob_lessthan_2 = quad(f,-np.inf,2)[0]-quad(f,-np.inf,2)[1]
prob_lessthan_1 = quad(f,-np.inf,1)[0]-quad(f,-np.inf,1)[1]
prob_1_to_2=(prob_lessthan_2-prob_lessthan_1)*c
print(prob_1_to_2)