from itertools import product, permutations

def f(w, x, y, z):
    return (w == z) or (not(y <= w)) or (not(x))

p = product((0, 1), repeat=5)
for x in p:
    a1, a2, a3, a4, a5 = x
    s1 = (0, 0, 1, a1)
    s2 = (a2, 1, 1, a3)
    s3 = (0, a4, a5, 0)
    if len(set([s1, s2, s3])) == 3:
        for r in permutations('wxyz'):
            if f(**dict(zip(r, s1))) == 0:
                if f(**dict(zip(r, s2))) == 0:
                    if f(**dict(zip(r, s3))) == 0:
                        print(*r)