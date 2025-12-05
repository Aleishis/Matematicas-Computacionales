from static.entities.prime import is_prime

def factores(n):
    factores = {}
    primos = is_prime(n)

    for p in primos:
        while n % p == 0:
            factores.setdefault(p, 0)
            factores[p] += 1
            n //= p
    return factores

def mcm(numero1, numero2):
    f1 = factores(numero1)
    f2 = factores(numero2)

    all_factors = []

    for key in f1:
        all_factors.append(key)
    for key in f2:
        if key not in all_factors:
           all_factors.append(key)

    total = 1

    for p in all_factors:
        exp1 = f1.get(p, 0)
        exp2 = f2.get(p, 0)

        total *= (p ** max(exp1, exp2))

    return total
