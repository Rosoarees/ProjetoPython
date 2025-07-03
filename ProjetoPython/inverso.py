# Programa: Inversão de Vetor
print("Inversor de Valores\n" + "=" * 30)

# Lendo os 10 números
vetor = []
for i in range(1, 11):
    while True:
        try:
            numero = float(input(f"Digite o {i}º número real: "))
            vetor.append(numero)
            break
        except ValueError:
            print("Erro: Digite um número válido!")

# Exibindo na ordem inversa
print("\nValores na ordem inversa:")
for numero in reversed(vetor):
    print(numero)

# Versão alternativa em uma linha:
# print("\nValores invertidos:", list(reversed(vetor)))