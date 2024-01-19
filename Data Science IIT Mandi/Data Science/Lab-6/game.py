import random
import matplotlib.pyplot as plt
import time

def Galton_board(balls,levels):
    l=[]
    bins=levels+1
    d={0:5,1:4,2:3,3:2,4:3,5:4,6:5}
    d5={9:"$1",12:"$2",16:"$5"}
    d10={10:"$1",24:"$2",29:"$5"}
    suml=0
    x="Yes"
    for i in range(bins):
        l.append([0]*(i + 1))
    for i in range(balls):
        if x=="leave":
            if balls==5:
                print(f"Your Total Sum was {suml}")
                if suml in d5:
                    print(f"Congrats! You Won {d5[suml]}")
                elif suml>16:
                    print("Woahhh! You Won $10")
                else:
                    print("Better Luck Next Time! You didn't won a Reward")
            if balls==10:
                print(f"Your Total Sum was {suml}")
                if suml in list(d10.keys()):
                    print(f"Congrats! You Won {d10[suml]}")
                elif suml>30:
                    print("Woahhh! You Won $10")
                else:
                    print("Better Luck Next Time! You didn't won a Reward")
            break
            
        l[0][0]+=1
        previndex=0
        for j in range(levels):
            side = random.choice([-1, 1])
            if side==1:
                previndex=previndex+1
            
            l[j + 1][previndex] += 1
            
        suml+=d[previndex]
        print()
        print(f"Rolling ball-{i+1}....")
        time.sleep(3)
        print()
        print(f"Nice! Ball went into slot {previndex+1}, Your current sum = {suml} ")
        print()
        if i<balls-1:
            x=input("Ready To Roll Next Ball or Want to leave? (Roll/Leave): ").lower()
            
    if(x!="leave"):
        time.sleep(3)
        print("Damn Those Rolls Were amazing...")
        time.sleep(2)
        print()
        print(f"Your Total Sum was {suml}")
        print()
        if balls==5:
            if suml in d5:
                print(f"Congrats! You Won {d5[suml]}")
            elif suml>16:
                print("Woahhh! You Won $10")
            else:
                print("Better Luck Next Time! You didn't won a Reward")
        if balls==10:
            if suml in d10:
                print(f"Congrats! You Won {d10[suml]}")
            elif suml>30:
                print("Woahhh! You Won $10")
            else:
                print("Better Luck Next Time! You didn't won a Reward")
        print()

print("Welcome To Galton World")
print("""Game Price $7 for each play 
      
      Rules:
      There are 6 Slots at the bottom of the board with each carrying certain points
      You will be given balls to roll down into the Galton Board, as the ball will fall into the slots points will sumed up
      For certain value of sum you will get a reward
      
      Points of Slots: 
      Slot:    1 2 3 4 5 6 7
      Points:  5 4 3 2 3 4 5
      
      Prize: 
      balls   Sum     Reward
      
               9        $1
        5      12       $2
               16       $5
          more than 16  $10
          
               10       $1
       10      24       $2
               29       $5
          more than 30  $10
          """)
print()
n=int(input("Enter No. of balls you Want: (5,10):  "))
Galton_board(n, 6)