# factorial(nuimero) = numero * factorial(numero -1)
# la función se llama a si misma

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1) # factorial(3) = 3 * factorial(2)
    
# print(factorial(8))


def suma(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma(numero - 1)


print(suma(100))