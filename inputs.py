# Cada dato ingresado mediante input ES un TEXTO

numero = input('Por favor, ingrese un número entero...')
print(type(numero))
print(numero)

print(f'Su NÚMERO multiplicado por 4 es : {numero * 4}')
print(f'Su NÚMERO (convertido a decimal) multiplicado por 2 es : {float(numero) * 2}')
print(f'Su NÚMERO (convertido a entero) multiplicado por 2 es : {int(numero) * 2}')