# --- Leitor de Vetor (Lista) de 5 Números ---

# Bloco 1: Inicialização
# Criamos a nossa lista vazia. É o nosso gaveteiro antes de colocar qualquer coisa dentro.
numeros = []

print("--- Por favor, insira 5 números inteiros ---")

# Bloco 2: Coletando os dados com um loop 'for'
# Vamos repetir o processo de pedir um número exatamente 5 vezes.
# Usamos '_' como nome da variável do loop porque não precisamos usar o seu valor (0, 1, 2, 3, 4),
# só nos importa que o loop execute 5 vezes. É uma convenção em Python.
for _ in range(5):
    while True:
        try:
            # Pedimos um número ao usuário
            numero_lido = int(input("Digite um número: "))
            
            # O método .append() adiciona o item no FINAL da lista.
            # É como abrir a próxima gaveta vazia e colocar algo dentro.
            numeros.append(numero_lido)
            
            break # Sai do loop 'while' de validação se o número for válido.
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Bloco 3: Exibindo o resultado
print("-" * 20)
print("\nOs números digitados foram:")

# Python tem uma forma muito fácil de mostrar uma lista inteira.
print(f"A lista completa é: {numeros}")


# Bónus: Mostrando os números um por um, de forma mais elegante
print("\nMostrando um número por linha:")
for numero in numeros:
    # Este loop 'for' é diferente: ele não usa 'range'.
    # Ele percorre cada item que já está DENTRO da lista 'numeros'.
    print(numero)