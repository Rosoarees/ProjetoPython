# Programa: Contador de Pessoas por Sexo
print("Contagem de Pessoas por Sexo\n" + "=" * 30)

# Solicita o total de pessoas
while True:
    try:
        total_pessoas = int(input("Digite o total de pessoas no grupo: "))
        if total_pessoas > 0:
            break
        print("Erro: Digite um número maior que zero!")
    except ValueError:
        print("Erro: Digite um número inteiro válido!")

# Contador para sexo masculino
contador_masculino = 0

# Coleta o sexo de cada pessoa
for i in range(1, total_pessoas + 1):
    while True:
        sexo = input(f"Digite o sexo da {i}ª pessoa (m/M para masculino): ").upper()
        if sexo in ['M', 'F']:
            if sexo == 'M':
                contador_masculino += 1
            break
        print("Erro: Digite 'm' ou 'M' para masculino, 'f' ou 'F' para feminino")

# Exibe o resultado
print(f"\nTotal de pessoas do sexo masculino: {contador_masculino}")
print(f"Porcentagem masculina: {(contador_masculino/total_pessoas)*100:.1f}%")