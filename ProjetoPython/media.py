# --- Calculadora de Média Aritmética de N Notas ---

# Bloco 1: Boas-vindas e configuração inicial
print("--- Bem-vindo à Calculadora de Média! ---")

# Vamos usar um loop 'try-except' para garantir que o usuário digite um número válido.
# Isto torna o nosso programa mais robusto e evita que ele quebre com entradas inválidas.
while True:
    try:
        # Perguntamos quantas notas serão inseridas e convertemos para inteiro.
        num_de_notas = int(input("Quantas notas você deseja inserir? "))
        
        # Se o usuário digitar um número negativo ou zero, pedimos novamente.
        if num_de_notas > 0:
            break # Sai do loop se o número for válido (maior que zero).
        else:
            print("Por favor, insira um número maior que zero.")
    except ValueError:
        # Esta mensagem aparece se o usuário digitar algo que não é um número (ex: "três").
        print("Entrada inválida. Por favor, digite um número inteiro.")


# Bloco 2: Inicialização das variáveis acumuladoras
# Precisamos de um lugar para guardar a soma das notas. Começa em zero.
soma_das_notas = 0.0 # Usamos 0.0 para indicar que trabalharemos com floats (decimais).

print("-" * 20) # Imprime uma linha para separar visualmente


# Bloco 3: O Loop para coletar as notas
# Este é um loop 'for', ideal para quando sabemos exatamente quantas vezes queremos repetir algo.
# A função range(1, num_de_notas + 1) vai gerar os números de 1 até N.
for i in range(1, num_de_notas + 1):
    
    # Usamos um loop interno para validar cada nota individualmente.
    while True:
        try:
            nota = float(input(f"Digite a nota {i}: "))
            # Poderíamos adicionar validações aqui, como if 0 <= nota <= 10:
            soma_das_notas += nota
            break # Sai do loop de validação da nota atual se for um número válido.
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a nota.")


# Bloco 4: Cálculo e exibição do resultado final
# Este bloco só é executado após o término do loop 'for'.

# O cálculo da média
media = soma_das_notas / num_de_notas

print("-" * 20)
print("\n--- Resultado Final ---") # \n para uma nova linha
print(f"Você inseriu {num_de_notas} notas.")
print(f"A soma total das notas é: {soma_das_notas:.2f}")
print(f"A média aritmética das notas é: {media:.2f}")