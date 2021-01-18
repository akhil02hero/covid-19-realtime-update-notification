# A Python program to print all 
# permutations using library function 
from itertools import permutations 
a={1,2,3}
# Get all permutations of [1, 2, 3] 
perm = permutations(a) 

# Print the obtained permutations 
for i in list(perm): 
	print (i)
