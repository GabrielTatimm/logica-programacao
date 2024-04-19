lampada = input('A lampada estava plugada? S ou N:')
if lampada == "S":
    print(' Verfificar o Bulbo')
    bulbo = input("O bulbo queimou? S ou N:")
    if bulbo == "S":
        print('Trocar o Bulbo')
    else:    
        print('Comprar lampada nova')
else:
    print('Plugar a lampada')
   