def is_prime(n):
    
    prime_numbers = [2]
    
    for i in range(3,n+1):
        isPrime = True
        for j in range(3, i):
            
            if i%2 == 0:
                isPrime = False
            if i%j == 0:
                isPrime = False
        if isPrime:
            prime_numbers.append(i)
    
    return prime_numbers

