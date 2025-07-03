# Programa: Calculadora Simples
print("Calculadora Básica\n" + "=" * 20)

# Solicita os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Menu de operações
print("\nOperações disponíveis:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# Solicita a operação
while True:
    opcao = input("\nDigite o número da operação desejada (1-4): ")
    
    if opcao in ['1', '2', '3', '4']:
        break
    print("Opção inválida! Digite um número entre 1 e 4.")

# Realiza o cálculo
if opcao == '1':
    resultado = num1 + num2
    operacao = "+"
elif opcao == '2':
    resultado = num1 - num2
    operacao = "-"
elif opcao == '3':
    resultado = num1 * num2
    operacao = "*"
elif opcao == '4':
    if num2 != 0:
        resultado = num1 / num2
        operacao = "/"
    else:
        print("Erro: Divisão por zero!")
        exit()

# Exibe o resultado
print(f"\nResultado: {num1} {operacao} {num2} = {resultado:.2f}")