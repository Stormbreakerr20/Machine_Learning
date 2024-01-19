import pandas as pd;
# To List
df=pd.read_csv('Data.csv')
l1=df['Numbers'].tolist()

# 1.1
print()
first_100=[l1[i] for i in range(100)]
print(f"Sum of first 100: {sum(first_100)}")
#1.2
print()
last_100=[l1[i] for i in range(len(l1)-1,len(l1)-101,-1)]
print(f"Sum of last 100: {sum(last_100)}")
#1.3
print()
first_2000=[l1[i] for i in range(2000)]
print(f"Sum of first 2000: {sum(first_2000)}")
# 1.4
print()
last_2000=[l1[i] for i in range(len(l1)-1,len(l1)-2001,-1)]
print(f"Sum of last 2000: {sum(last_2000)}")

# 1.5
print()
count=1
temp=[]
for i in range(len(l1)):
    if((i+1)%100==0):
        temp.append(l1[i])
        print(f"for elements {count} to {i+1} ::   Sum = {sum(temp)} , Mean : {sum(temp)/100}")
        count=count+100
        temp=[]
    else:
        temp.append(l1[i])
        
# 2.1
print()
print(f"89 is repeated {l1.count(89)} times")
# 2.2
print()
temp1=[]
for i in range(len(l1)):
    if (l1[i]==89):
        temp1.append(i+1)
print(f"89 is in lines: {temp1} ")
# 2.3
print()
dict1={}
for i in l1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)
# 2.4
print()
print(dict1.values())
print(f"{list(dict1.keys())[list(dict1.values()).index(max(list(dict1.values())))]} is repeated most times i.e {max(dict1.values())} times")
#3.1
print()
print(f"Largest: {max(first_100)} smallest: {min(first_100)} among first 100")
#3.2
print()
print(f"Largest: {max([l1[i] for i in range(101,202)])} smallest: {min([l1[i] for i in range(101,202)])} among 101th to 201th")
# 3.3,3.4
print()
count=1
temp3=[]
for i in range(len(l1)):
    if((i+1)%100==0):
        temp3.append(l1[i])
        print(f"Largest: {max(temp3)} smallest: {min(temp3)} among {count} to {i+1}")
        print(f"Mean of largest and smallest: {(max(temp3)+min(temp3))/2}")
        count=count+100
        temp3=[]
    else:
        temp3.append(l1[i])
        
# 4
print()
le=[]
lo=[]
for i in l1:
    if i%2==0:
        le.append(i)
    else:
        lo.append(i)
print(f"Odd: {len(lo)} Even: {len(le)}")
print(f"Odd: {lo} \n\nEven: {le}")
print(f"Avg of Odd: {sum(lo)/len(lo)}")
print(f"Avg of Even: {sum(le)/len(le)}")

# avg odd> avg even