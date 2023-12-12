# Calculadora em Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    try:
        print("\n******************* Python Calculator *******************")
        print("\nSelecione o número da operação desejada: \n")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        escolha = int(input("\nDigite sua opção (1/2/3/4/5): "))
        if escolha == 5:
            print("Programa finalizado!")
            break
        elif escolha not in (1,2,3,4):
            print("Escolha uma opção válida")
            continue
    except ValueError:
        print("Digite uma opção válida, por favor")
        continue
    else:
        print("Obrigado(a). Para continuar, digite os números.")
        while True:
            try:
                num1 = float(input("\nDigite o primeiro número: "))
                num2 = float(input("\nDigite o segundo número: "))
            except ValueError:
                print("Você não consegue realizar operações com esse tipo de variável, tente novamente")
                continue
            else:
                if escolha == 1:
                    print("\n", num1, "+", num2, "=", add(num1, num2), "\n")
                elif escolha == 2:
                    print("\n", num1, "-", num2, "=", subtract(num1, num2), "\n")
                elif escolha == 3:
                    print("\n", num1, "*", num2, "=", multiply(num1, num2), "\n")
                elif escolha == 4:
                    if num2 == 0:
                        print("Não é possível dividir por zero. Tente novamente.")
                    else:
                        print("\n", num1, "/", num2, "=", divide(num1, num2), "\n")
                else:
                    print("Opção inválida. Tente novamente.")
                break
