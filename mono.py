'''
Part A: 
Monoatomic

H=[x y 0 0.....0]
  [y x y 0.....0]
  [0 y x y.....0]
  [.............]
  [0.......y x y]
  [0.......0 y x]
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
d=int(input("Enter diagonal element (E0):"))

d1=int(input("Enter non-diagonal element (beta):"))

for i in range(n):
    for j in range(n):
        if i==j:
            a[i][j]=d
        elif i==j-1 or i==j+1:
            a[i][j]=d1


print("The plot")

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
plt.xlabel('For mono-atomic')
plt.ylabel('Density of states')
plt.title(f'Input: E0={d}, 'r'$\beta$='f'{d1}, N={n}')

plt.show()

