try:
    peso = float(input('Ingrese su peso en kg: '))
    altura = float(input('Ingrese su altura en Cm: '))

    if peso <= 0 or altura <= 0:
        print('Por favor ingrese parámetros válidos (positivos).')
    else:
 
        imc = peso / (altura * altura)
        
        print(f'Su IMC es: {imc:.2f}')
        
        if imc < 18.5:
            print('bajo peso ')
        elif 18.5 <= imc <= 24.9:
            print('peso normal ')
        elif  25 <= imc <= 26.9:
            print('sobrepeso grado 1')
        elif 27 <= imc <= 29.9:
            print('sobrepeso grado 2')
        elif 30 <= imc <= 34.9:
            print('obesidad tipo 1')
        elif 35 <= imc <= 39.9:
            print('obesidad tipo 2')
        else:
            print('morbida')
except ValueError:
    print('POr favor ingrese valores numericos validos! ') 