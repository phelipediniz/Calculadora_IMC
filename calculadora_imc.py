print('Qual o seu peso? (kg)')
peso = input()

if not peso.isdigit():
   print('Favor digitar o peso em kilos!')

try:
    print('Qual a sua altura? (m)')
    altura = float(input())

except ValueError:
    print("Favor digitar a altura em metros!")

peso = float(peso)
altura = float(altura)

imc = peso / (altura*altura)

print(f'Seu IMC é de {imc:.2f}')

if (imc < 18.5):
    print('Você está abaixo do peso, procure um nutricionista. Se alimente melhor!')
elif (imc >= 18.5) and (imc < 24.9):
    print('Parabéns, você está no seu peso ideal!')
elif (imc >=25) and (imc < 29.9):
    print('Cuidado!, você está com sobrepeso. Pratique exercícios físicos!')
elif (imc >= 30) and (imc < 34.9):
    print ('Seu imc corresponde a obesidade grau I, precisamos mudar a alimentação imediatamente. Você possui riscos de desenvolver doenças cardiovasculares!')
elif (imc >= 35) and (imc < 39.9):
    print('Seu imc corresponde a obesidade grau II. Procure imediatamente um nutricionista e um atendimento médico. Você possui altas chances de desenvolvimento de doenças como: diabetes, alto colesterol, pressão alta entre outras!')
else:
    print('Você possui o imc correspondente a obesidade mórbida. Procure imediatamente um médico para auxílio de equipe multidisciplinar.')