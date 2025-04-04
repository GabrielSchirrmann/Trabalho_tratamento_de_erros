class LetraMaiuscuala (Exception):
    pass
try:

    x = input("Digite uma frase ou palavra com apenas letras mauisculas: ")
    if x.islower():
        raise LetraMaiuscuala("por favor digite a palavra ou texto apenas com letras maiusculas")
    
except LetraMaiuscuala as a:
    print(a)



    

