def Sair():
    print("Encerrando o calculadora...")
    raise SystemExit

print('''
      CALCULARORA
        OPÇÕES
        
[ 1 ] Somar
[ 2 ] Subtrair
[ 3 ] Dividir
[ 4 ] Multiplicar
[ 5 ] Sair 

''')

opção = int(input('Qual sua opção? '))

if opção == 1:
    n1 = int(input('Digite o primeiro numero para SOMAR: '))
    n2 = int(input('Digite o segundo numero para SOMAR: '))
    total = n1 + n2
    print(f'A soma de {n1} com {n2} = {total}')
    
elif opção == 2:
     n1 = int(input('Digite o primeiro numero para SUBTRAIR: '))
     n2 = int(input('Digite o segundo numero para SUBTRAIR: '))
     total = n1 - n2
     print(f'A Subtração de {n1} com {n2} = {total}')
     
elif opção == 3:
     n1 = int(input('Digite o primeiro numero para DIVIDIR: '))
     n2 = int(input('Digite o segundo numero para DIVIDIR: '))
     total = n1 / n2
     print(f'A divisão de {n1} com {n2} = {total:.2}')
     
elif opção == 4:
     n1 = int(input('Digite o primeiro numero para MULTPLICAR: '))
     n2 = int(input('Digite o segundo numero para MULTPLICAR: '))
     total = n1 * n2
     print(f'A multplicação de {n1} com {n2} = {total}')
elif opção == 5:
    Sair()