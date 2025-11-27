from prime import is_prime

def factores(n):
    factores= {}
    primos = is_prime(n)
    
    for i in primos:
        
        while True:
            if n%i == 0:
                factores.setdefault(i,0)
                factores[i] += 1
                n /= i
            else:
                break
    return factores
    

def mcd(num1, num2):
    factores_temporales = []
    
    factores_num1 = factores(num1)
    factores_num2 = factores(num2)
    
    factores_comunes = []
    
    for key in factores_num1:
        factores_temporales.append(key)
    for key in factores_num2:
        if key in factores_temporales:
            factores_comunes.append(key)
    
    total = 1
    for f in factores_comunes:
        factor1 = factores_num1[f]
        factor2 = factores_num2[f]
        if (factor1 < factor2):
            total *= (f**factor1)
        elif (factor2 < factor1):
            total *= (f**factor2)
        else:
            total *= (f**factor1)

    return total 

