# --- Somador de Números (parando com 0) ---

# Bloco 1: Inicialização
# Precisamos de um lugar para guardar a soma. Começamos com zero.
# Pense nisto como pegar um cesto de compras vazio antes de começar a fazer compras.
soma_dos_numeros = 0

print("--- Somador de Números ---")
print("Digite números inteiros para somar. Digite 0 para ver o resultado final.")

# Bloco 2: O Loop Infinito com Condição de Parada (Sentinela)
while True:
    try:
        # Pedimos o número ao usuário DENTRO do loop
        numero_digitado = int(input("Digite um número (ou 0 para sair): "))

        # Verificação da Sentinela: esta é a condição de parada.
        # É a primeira coisa que verificamos.
        if numero_digitado == 0:
            break  # O comando 'break' interrompe o loop 'while' imediatamente.

        # Se o número não for 0, nós o adicionamos à nossa soma.
        # Esta linha só é executada se o 'if' acima for falso.
        soma_dos_numeros += numero_digitado # Forma curta de: soma_dos_numeros = soma_dos_numeros + numero_digitado

    except ValueError:
        # Uma boa prática: avisar o usuário se ele não digitar um número.
        print("Entrada inválida. Por favor, digite apenas números inteiros.")

# Bloco 3: Exibição do Resultado
# Este código só é executado quando o loop é interrompido pelo 'break'.
print("-" * 20) # Uma linha para separar
print(f"A soma de todos os números digitados é: {soma_dos_numeros}")