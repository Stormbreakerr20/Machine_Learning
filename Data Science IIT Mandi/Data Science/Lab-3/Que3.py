h=0.001
r1=0.2
r2=0.8
r1_h=0.89
r2_h=0.99
r1_noth=0.025
r2_noth=0.005

def s(r1,r2):
    return r1*(0.001*0.89 + 0.999*0.025) + r2*(0.001*0.99 + 0.999*0.005)

def h_s(r1,r2):
    return 0.001*(r1*0.89 + r2*0.99)/s(r1,r2)
def r2_s(r1,r2):
    return r2*(0.001*0.99+ 0.999*0.005)/s(r1,r2)

def hr2_s(r1,r2):
    return 0.001*r2*0.99/(0.001*r2*0.99 + 0.999*r2*0.005)

def r2_hs(r1,r2):
    return hr2_s(r1, r2)*r2_s(r1, r2)/h_s(r1, r2)

print(r2_hs(r1, r2))   
for i in range(9):
    r2=r2_hs(r1, r2)
    r1= 1-r2
    print(r2_hs(r1, r2))   

print(r2_hs(r1, r2))   
    