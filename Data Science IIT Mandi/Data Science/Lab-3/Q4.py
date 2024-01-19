m_u= 0.2
m_i=0.6
m_o =0.2
def p_b(m_u,m_i,m_o,year):
    p_b= (0.25)**year*m_u + m_i*(0.5)**year +m_o*(0.75)**year
    return p_b



def update(curr,market_beat_perc,year,p_b):
    new =(((market_beat_perc)**year)*(curr))/p_b
    return new

m_u_new=update(m_u,0.25,2,p_b(m_u,m_i,m_o,2))
m_i_new=update(m_i,0.5,2,p_b(m_u,m_i,m_o,2))
m_o_new=update(m_o,0.75,2,p_b(m_u,m_i,m_o,2))

print(f"if beat for 2 years underperformer belief: {round((update(m_u,0.25,2,p_b(m_u,m_i,m_o,2)))*100,2)}")
print(f"if beat for 2 years in-lineperformer belief: {round((update(m_i,0.5,2,p_b(m_u,m_i,m_o,2)))*100,2)}")
print(f"if beat for 2 years overperformer belief: {round((update(m_o,0.75,2,p_b(m_u,m_i,m_o,2)))*100,2)}")
print()
print(f"if again beat market for next year underperformer belief: {(update(m_u_new,0.25,1,p_b(m_u_new,m_i_new,m_o_new,1))*100)}")
print(f"if again beat market for next year in-lineperformer belief: {(update(m_i_new,0.5,1,p_b(m_u_new,m_i_new,m_o_new,1))*100)}")
print(f"if again beat market for next year overperformer belief: {(update(m_o_new,0.75,1,p_b(m_u_new,m_i_new,m_o_new,1))*100)}")

print()
print(f"if again beat market directly for 3 years underperformer belief: {(update(m_u,0.25,3,p_b(m_u,m_i,m_o,3)))*100}")
print(f"if again beat market directly for 3 years in-lineperformer belief: {(update(m_i,0.5,3,p_b(m_u,m_i,m_o,3))*100)}")
print(f"if again beat market directly for 3 years overperformer belief: {(update(m_o,0.75,3,p_b(m_u,m_i,m_o,3))*100)}")
print()
print(f"if again beat market directly for 10 years underperformer belief: {(round(update(m_u,0.25,10,p_b(m_u,m_i,m_o,10))))*100}")
print(f"if again beat market directly for 10 years in-lineperformer belief: {(round(update(m_i,0.5,10,p_b(m_u,m_i,m_o,10)))*100)}")
print(f"if again beat market directly for 10 years overperformer belief: {(round(update(m_o,0.75,10,p_b(m_u,m_i,m_o,10)))*100)}")