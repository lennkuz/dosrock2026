import sys
from functools import lru_cache
sys.setrecursionlimit(1000000)
@lru_cache()
def f(n):
    if n<10:
        return 3
    return (n+4)*f(n-5)
for i in range(10,257487):
    f(i)
print((f(257487)//683+67*f(257477))//f(257472))