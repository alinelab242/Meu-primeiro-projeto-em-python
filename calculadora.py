# Calculadora Aritmética
# Projeto seguindo as instruções: entrada, conversão, operações, repetição e saída.

print("=== CALCULADORA ARITMÉTICA ===")

# Laço geral para repetir o programa inteiro
while True:

    # 1. Receber dois números do usuário
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))   
  # 2. Menu de operações
    print("\nEscolha a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
opcao = input("Digite o número da operação: ") 
  # 3. Estrutura condicional para executar a operação escolhida
    if opcao == "1":
        resultado = num1 + num2
        print("Resultado da soma:", resultado)

    elif opcao == "2":
        resultado = num1 - num2
        print("Resultado da subtração:", resultado)

    elif opcao == "3":
        resultado = num1 * num2
        print("Resultado da multiplicação:", resultado)

    elif opcao == "4":
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado da divisão:", resultado)
        else:
            print("Erro: divisão por zero não é permitida.")

    else:
        print("Opção inválida!") 
 # 4. Laco de repetição para continuar ou encerrar
    continuar = input("\nDeseja fazer outra operação? (s/n): ")

    if continuar.lower() != "s":
        print("\nEncerrando a calculadora... até mais!")
        break
