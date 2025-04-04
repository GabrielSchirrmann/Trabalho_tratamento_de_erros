class NumeroDividendo(Exception):
    pass
try:

    numero = int(input("Digite um numero para ser divodido por 10: "))

    if numero / 10 == 0:
        raise NumeroDividendo("por favor digite um numero valido e tente novamente")

except NumeroDividendo as a:
    print(a)

