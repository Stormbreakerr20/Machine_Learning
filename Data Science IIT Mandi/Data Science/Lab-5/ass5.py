
import pandas as pd
import matplotlib.pyplot as plt


x=pd.read_csv("2021_IN_Region_Mobility_Report.csv")

sub_region_1=x["sub_region_1"].tolist()
sub_region_2=x["sub_region_2"].tolist()
metro_area=x["metro_area"].tolist()
iso_3166_2_code=x["iso_3166_2_code"].tolist()
retail_and_recreation_percent_change_from_baseline=x["retail_and_recreation_percent_change_from_baseline"].tolist()
grocery_and_pharmacy_percent_change_from_baseline=x["grocery_and_pharmacy_percent_change_from_baseline"].tolist()
parks_percent_change_from_baseline=x["parks_percent_change_from_baseline"].tolist()
transit_stations_percent_change_from_baseline=x["transit_stations_percent_change_from_baseline"].tolist()
workplaces_percent_change_from_baseline=x["workplaces_percent_change_from_baseline"].tolist()
residential_percent_change_from_baseline=x["residential_percent_change_from_baseline"].tolist()



d={"Jan":[31],"Feb":[28],"March":[31],"April":[30],"May":[31],"June":[30],"July":[31],"Aug":[31],"Sept":[30],"Oct":[31],"Nov":[30],"Dec":[31]}
index =128037

def f(d,l,index):
    r=[]
    for i in range(365):
        r.append(l[index+i])
    d["Jan"].append(r)
    
f(d,retail_and_recreation_percent_change_from_baseline,index)
f(d,grocery_and_pharmacy_percent_change_from_baseline,index)
f(d,parks_percent_change_from_baseline,index)
f(d,transit_stations_percent_change_from_baseline,index)
f(d,workplaces_percent_change_from_baseline,index)
f(d,residential_percent_change_from_baseline,index)


plt.plot([i for i in range(1,366)],d["Jan"][1],label="Plot for retail")
plt.plot([i for i in range(1,366)],d["Jan"][2],label="Plot for grocery")
plt.plot([i for i in range(1,366)],d["Jan"][3],label="Plot for parks")
plt.plot([i for i in range(1,366)],d["Jan"][4],label="Plot for transit")
plt.plot([i for i in range(1,366)],d["Jan"][5],label="Plot for workplace")
plt.plot([i for i in range(1,366)],d["Jan"][6],label="Plot for resident")
y=[]
suma=0
for i in d:
    y.append(d[i][0]+suma)
    suma+=d[i][0]

plt.xticks(y,[i for i in d])

plt.legend()
plt.show()

# 2
print()
def variance(l):
    mean=sum(l)/len(l)
    var=[(i - mean)**2 for i in l]
    return sum(var)/len(l)

print(f"Variance for entire year for mobility retail = {variance(retail_and_recreation_percent_change_from_baseline[0:365])}")
print(f"Variance for entire year for mobility grocery = {variance(grocery_and_pharmacy_percent_change_from_baseline[0:365])}")
print(f"Variance for entire year for mobility transit = {variance(transit_stations_percent_change_from_baseline[0:365])}")
print(f"Variance for entire year for mobility parks = {variance(parks_percent_change_from_baseline[0:365])}")
print(f"Variance for entire year for mobility workplace = {variance(workplaces_percent_change_from_baseline[0:365])}")
print(f"Variance for entire year for mobility residential = {variance(residential_percent_change_from_baseline[0:365])}")
print()
print(f"Variance for entire April-May for mobility retail = {variance(retail_and_recreation_percent_change_from_baseline[90:139])}")
print(f"Variance for entire April-May for mobility grocery = {variance(grocery_and_pharmacy_percent_change_from_baseline[90:139])}")
print(f"Variance for entire April-May for mobility transit = {variance(transit_stations_percent_change_from_baseline[90:139])}")
print(f"Variance for entire April-May for mobility parks = {variance(parks_percent_change_from_baseline[90:139])}")
print(f"Variance for entire April-May for mobility workplace = {variance(workplaces_percent_change_from_baseline[90:139])}")
print(f"Variance for entire April-May for mobility residential = {variance(residential_percent_change_from_baseline[90:139])}")
print()

t={}
def exp(i):
    return retail_and_recreation_percent_change_from_baseline[89+i]*0.2 + grocery_and_pharmacy_percent_change_from_baseline[89+i]*0.2 +transit_stations_percent_change_from_baseline[89+i]*0.05 + parks_percent_change_from_baseline[89+i]*0.02 +workplaces_percent_change_from_baseline[89+i]*0.03 +residential_percent_change_from_baseline[89+i]*0.5
def meanp(i):
    return (retail_and_recreation_percent_change_from_baseline[89+i] + grocery_and_pharmacy_percent_change_from_baseline[89+i] +transit_stations_percent_change_from_baseline[89+i] + parks_percent_change_from_baseline[89+i] +workplaces_percent_change_from_baseline[89+i] +residential_percent_change_from_baseline[89+i])/6

for i in range(1,51):
    t[f"day {i}"]=[round(exp(i),2)]
    t[f"day {i}"].append(round(meanp(i),2))

print(t)

