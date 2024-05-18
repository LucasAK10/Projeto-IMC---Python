#entrada de dados
nome = input('Informe o seu nome: ')
peso = str(input('Informe o peso em (kg): ')).replace(',','.')
altura = str(input('Informe a sua altura em (m): ')).replace(',','.')

try:
    #conveter para float
    peso = float(peso)
    altura = float(altura)

# calculo do imc
    imc = peso/(altura**2)
#exibe o resultado o imc
    print(f'O valor do IMC de {nome} é {imc:,.2f}.')

except:
    print('Não foi possível calcular o IMC')
    
#verifica o peso
if imc <18.5:
    print(f'{nome} Paciente está abaixo do peso.')
elif imc <25:
    print(f'{nome} Paciente está com peso ideal.')
elif imc <30:
    print(f'{nome} Paciente está com sobrepeso.')
elif imc <40:
    print(f'{nome} Paciente está com obesidade grase.')
else:
    print('Obesidade gravíssima.')









  



