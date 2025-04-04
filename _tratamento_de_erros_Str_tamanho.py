class TamanhoPalavra(Exception):
    pass
try:

    palavra1 = (input("Digite uma palavra:  "))
    palavra2 = (input("Digite digite uma palavra com a mesma quantidade de letras que a digitada anteriormente: "))


    if  len(palavra1) != len(palavra2):
        raise TamanhoPalavra("Numero de leras não coincidem por gentileza tente novamente")

except TamanhoPalavra as a:
    print(a)