from itertools import permutations
s1 = '457 346 24 123 167 257 156'
s2 = 'БВ АВД БГК ДГЕ КГВ АБЕ ДКЕ'
s2 = {frozenset(x) for x in s2.split()}
print("1 2 3 4 5 6 7")
for p in permutations("АБВГДЕК"):
    s3 = s1
    for x, y in zip("1234567", p):
        s3 = s3.replace(x, y)
    s3 = {frozenset(x) for x in s3.split()}
    if s3 == s2:
        print(*p)
