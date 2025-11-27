def euclides(num1, num2):
    numeros = [num1, num2]
    while True:
        numeros.sort
        residuo = (numeros[0] % numeros[1]) 
        if residuo == 0:
            return numeros[1]
        numeros[0] = numeros[1]
        numeros[1] = residuo

