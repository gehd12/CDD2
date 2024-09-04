litro=float(input('informe a quantidade de litros'))
tipo=(input('informe o tipo de combustivel\n'
            'E ou e para entanol\n'
            'G ou g para gasolina'))

if tipo == 'G' or tipo== 'g':
    valor=litro*5.8
    print(f'total a pagar {valor}')

else:
    if tipo == 'E' or tipo == 'e':
        valor2 = litro * 4.9
        print(f'total a pagar {valor2}')


    else:
        print('invalido')