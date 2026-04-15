from math import dist
def center(K):
    c=0
    mns=10**20
    for t1 in K:
        sm=0
        for t2 in K:
            sm+=dist(t1[:-1],t2[:-1])
        if sm<mns:
            mns=min(sm,mns)
            c=t1
    return c

a=open('27_A_28766 (1).txt').readlines()
for i in range(len(a)):
    a[i]=a[i].replace(',','.').split()
    a[i][0]=float(a[i][0])
    a[i][1] = float(a[i][1])

K1=[]
K2=[]

for t in a:
    x,y,z=t
    if y>8:K1.append(t)
    else: K2.append(t)

C1=center(K1)
G=[]
for t in a:
    x,y,z=t
    if z[0]=='Y' and z[-3:]=='III':
        G.append(t)

mxs=0
mns=10**20
for t in G:
    mns=min(dist(C1[:-1],t[:-1]),mns)
for t in G:
    mxs=max(dist(C1[:-1],t[:-1]),mxs)
print(mns*10000)
print(mxs*10000)