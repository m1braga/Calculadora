'''Menu de opções'''
operacao = [
    'Soma',
    'Subtração',
    'Multiplicação',
    'Divisão'
]
num = 0
'''Função para funcionamento da calculadora, com condições para resolver operações matemáticas'''
def men():
    for i in range(len(operacao)):
        print(i, operacao[i])
    num = int(input('Qual operação acima deseja fazer?'))    
    if num <= 3:
        num1 = float(input('Digite o primeiro número:'))
        num2 = float(input('Digite o segundo número:'))
        if num == 0:
            resultado = float(num1 + num2)
        if num == 1:
            resultado = float(num1 - num2)
        if num == 2:
            resultado = float(num1 * num2)
        if num == 3:
            resultado = float(num1 / num2)  
        print(f"O resultado da operação é:  {resultado}")
    else:
        print('Opção não encontrada!')
men()


