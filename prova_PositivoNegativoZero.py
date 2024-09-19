def positivo_negativo_zero(numero):
    if numero > 0:
        print(f'O numero é positivo')
    elif numero < 0:
        print(f'O numero é negativo')
    else:
        print(f'O numero é zero')
    
numero = float(input('Digite um numero positivo, negativo ou zero:'))
    
positivo_negativo_zero(numero)
