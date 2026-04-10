def f(n):
    a = []
    while n > 0:
        a.append(n % 27)
        n //= 27
    return a[::-1]

s = 2 * 2187**567 + 729 ** 566 - 2 * 243 ** 565 + 81 ** 564 - 2 * 27 ** 563 -6561
g = f(s)
ct = 0
for x in g:
    if x % 2 == 0 and x > 9:
        ct += 1
print(ct)