def version_1(g, n=100):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    lst = []
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    for c in sieve:
        if sieve[c] != 0:
            lst.append([c])
    return lst[g]



print(version_1(5))


def num (k, n = 100):
    lst = [1]
    for i in range (2, 100):
        for j in range (2, i):
            if i % j == 0:
                break
            else:
                lst.append(i)


    return list(set(lst))[k-1]

print(num(2))
