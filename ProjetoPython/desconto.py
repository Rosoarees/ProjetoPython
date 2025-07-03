# Programa: Calculadora de Descontos por Faixa de Preço

# Dicionário que mapeia as faixas de preço para descontos
faixas_desconto = {
    (0, 100): 0.05,      # 5% de desconto para valores abaixo de R$ 100
    (100, 500): 0.10,    # 10% de desconto para valores entre R$ 100 e R$ 500
    (500, float('inf')): 0.15  # 15% de desconto para valores acima de R$ 500
}

# Solicita o valor do produto
valor = float(input("Digite o valor do produto (R$): "))

# Encontra o desconto aplicável usando next() e uma expressão geradora
desconto = next((perc for (min_, max_), perc in faixas_desconto.items() if min_ <= valor < max_), 0)

# Calcula os valores
valor_desconto = valor * desconto
preco_final = valor - valor_desconto

# Exibe os resultados
print("\nResumo do Desconto:")
print(f"Preço original: R$ {valor:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")