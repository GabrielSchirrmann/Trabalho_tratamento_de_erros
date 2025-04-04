class NumeroPar(Exception):
    pass
try:

    numero = int(input("Digite um numero par"))

    if numero % 2 != 0:
        raise NumeroPar("por favor digite um numero valido e tente novamente")

except NumeroPar as a:
    print(a)