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

a=open('27_B_28766.txt').readlines()
for i in range(len(a)):
    a[i]=a[i].replace(',','.').split()
    a[i][0]=float(a[i][0])
    a[i][1] = float(a[i][1])

K1=[]
K2=[]
K3=[]

for t in a:
    x,y,z=t
    if y<15:K1.append(t)
    if 15<y<23: K2.append(t)
    if y>23: K3.append(t)

C1=center(K1)
C2=center(K2)
C3=center(K3)
G=[]
for t in a:
    x,y,z=t
    if z[0]=='Z' and z[-1]=='I':
        G.append(t)

def giga(K):
    mns=10**20
    for t1 in K:
        for t2 in K:
            if t1!=t2:
                x1,y1,z1=t1
                x2,y2,z2=t2
                if z1[0]=='Z'and z1[-1]=='I' and z1.count('I')==1 and 'V' not in z1:
                    if z2[0] == 'Z' and z2[-1] == 'I' and z2.count('I') == 1 and 'V' not in z2:
                        mns=min(dist(t1[:-1],t2[:-1]),mns)
    return mns

B1=giga(K1)
B2=giga(K2)
B3=giga(K3)
print(B1*10000,B2*10000,B3*10000)