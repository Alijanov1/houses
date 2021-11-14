# find who lives higher in multi storey appartment
# don't use loops, use only finctions 
import math
def whoLivesHigher(floors,sections,apf, name1, a1,name2,a2):
  res = a1 % (apf * floors)
  res2 = a2 % (apf * floors)
  result = res // apf
  result2 = res2 // apf
  if math.ceil(result) > math.ceil(result2):
    return(name1)
  else: return(name2)

print(whoLivesHigher(10,3,3,'Elbek',69,'MS',59))
print(whoLivesHigher(10,3,3,'Asliddin',30,'Aziz',29))
print(whoLivesHigher(10,3,3,'Nurali',56,'Nursultan',55))
# it's working