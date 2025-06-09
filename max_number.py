pip=[ ]
for i in range(7):
   pop=input(f"number {i+1} :")
   pip.append(pop)
   
max=pip[0]

for non in  pip:
   if non >max:
      max=non
      
print (f"the max number is: {max} ")