from itertools import product
k = 0
for r in product("АЕЛПРЬ", repeat = 5):
    r = ''.join(r)
    k += 1
    if k % 2 == 0 and r[0] != "Ь" and r[0] != "Р" and r.count("Л") >= 2:
        print(k, r)
