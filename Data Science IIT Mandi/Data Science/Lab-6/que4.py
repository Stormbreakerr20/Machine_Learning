import random
import matplotlib.pyplot as plt

def Galton_board(balls,levels):
    l=[]
    bins=levels+1
    
    

    for i in range(bins):
        l.append([0]*(i + 1))

    for i in range(balls):
        l[0][0]+=1
        previndex=0
        for j in range(levels):
            side = random.choice([-1, 1])
            if side==1:
                previndex=previndex+1
            
            l[j + 1][previndex] += 1
            
    mean=sum([i for i in l[-1]])/bins
    var = (sum([(i-mean)**2 for i in l[-1]])/bins)
    print(f"For L = {levels} ==> Mean = {mean}, Variance = {var}")
    print(l[-1])
    plt.plot([i for i in range(1,bins+1)],l[-1])
    plt.xlabel("Slot Number -->")
    plt.ylabel("Distribution of balls -->")
    plt.show()

Galton_board(10000, 2)
Galton_board(10000, 6)
Galton_board(10000, 20)
Galton_board(10000, 100)

def Galton_board2(balls,levels):
    l=[]
    bins=levels+1

    for i in range(bins):
        l.append([0]*(i + 1))


    for i in range(balls):
        l[0][0]+=1
        previndex=0
        for j in range(levels):
            side = random.choice([-1, 1])
            if side==1:
                previndex=previndex+1
            
            l[j + 1][previndex] += 1
            
    print(l[-1])

Galton_board2(10000, 10)
Galton_board2(10000, 9)

# for odd and even level is that more the level leser are the balls in each slot as distributed uniformly