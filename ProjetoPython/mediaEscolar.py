# Programa: Cálculo de Média de 4 Notas
print("Calculadora de Média Escolar\n" + "=" * 30)

# Lista para armazenar as notas
notas = []

# Loop para ler as 4 notas
for i in range(1, 5):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota (0-10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Erro: A nota deve estar entre 0 e 10!")
        except ValueError:
            print("Erro: Digite um número válido!")

# Calcula a média
media = sum(notas) / len(notas)

# Exibe os resultados
print("\nNotas digitadas:", " | ".join(f"{nota:.1f}" for nota in notas))
print(f"Média calculada: {media:.2f}")

# Verificação de aprovação (opcional)
if media >= 6:
    print("Situação: Aprovado(a) ✅")
else:
    print("Situação: Reprovado(a) ❌")