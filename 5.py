for n in range(1, 1000):
    r = bin(n)[2:]
    sm = sum(int(x) for x in r)
    r = r + str(sm % 2)
    sm = sum(int(x) for x in r)
    r = r + str(sm % 2)
    r = int(r, 2)
    if r > 253:
        print(n)
        break
