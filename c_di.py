'''
Part C:
Diatomic ring

m=[x z 0 0.....z]
  [z y z 0.....0]
  [0 z x z.....0]
  [.............]
  [0.......z x z]
  [z.......0 z y]

'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
import math

def eigen(A):

    eigvals, eigvecs = la.eig(A)
    eigvals = eigvals.real
    return eigvals
    

n=int(input("Enter dimension of matrix:"))
a=[[0 for i in range(n)] for j in range(n)]
d=int(input("Enter diagonal element (E1):"))

d1=int(input("Enter 2nd diagonal element (E2):"))
d2=int(input("Enter non-diagonal element (beta):"))

for i in range(n):
    for j in range(n): 
        if i==j:
            if i%2==0:
                a[i][j]=d
            else: a[i][j]=d1
        elif i==j-1 or i==j+1:
            a[i][j]=d2
        
a[0][n-1]=d2
a[n-1][0]=d2

print("The plot:")

'''for i in range(n):
    for j in range(n):
        print(a[i][j],end="  ")
    print()'''

eigenst=eigen(a)
'''print("The eigen values are:")
for i in range(len(eigenst)):
    print(eigenst[i])
print("-----------")'''
emax=max(eigenst)
emin=min(eigenst)

wid=math.sqrt(n)
bi=int(wid)
plt.style.use('ggplot')
plt.hist(eigenst, bins=bi)
plt.xlabel('For Di-atomic ring')
plt.ylabel('Density of states')
plt.title(f'Input: E1={d}, E2={d1}, 'r'$\beta$='f'{d2}, N={n}')
plt.show()
