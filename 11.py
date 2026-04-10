from math import *
L = 289
N = 10 + 1015
i = ceil(log2(N))
I1 = ceil(L*i/8)
k = 524288
I = I1 * k
I = I / 1024 / 1024
print(I)