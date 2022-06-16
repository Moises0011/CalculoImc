peso = float(input("Digite seu peso: "))

altura = float(input("Informe sua altura: "))

imc = peso / (altura * altura)

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudavel")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade grau 1")
elif imc < 40:
    print("Obesidade grau 2 (severa)")
else:
    print("Obesidade grau 3 (morbida)")