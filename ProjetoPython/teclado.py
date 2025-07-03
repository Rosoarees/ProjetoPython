# --- Somador Interativo com Sinal de Parada (Sentinela) ---

# --- Bloco 1: Preparação ---
# Vamos criar a nossa variável acumuladora. É essencial que ela comece com 0.
# Pense nela como o visor de uma calculadora que acabámos de ligar.
soma_total = 0

# Mensagens iniciais para orientar o usuário. Um bom programa é claro sobre o que faz.
print("--- Máquina de Somar Infinita ---")
print("Digite os números que deseja somar.")
print("Quando terminar, digite 0 para ver o resultado.")
print("-" * 35) # Imprime uma linha para organização visual

# --- Bloco 2: O Coração do Programa (O Loop) ---
# Usamos o padrão 'while True' para criar um loop que, por padrão, nunca para.
# A parada será controlada por uma condição LÓGICA DENTRO do loop.
while True:
    try:
        # 1. Pedimos a entrada do usuário. Esta pergunta será repetida a cada ciclo.
        entrada = input("Digite um número (ou 0 para parar): ")
        
        # 2. Convertemos a entrada (que é sempre texto) para um número inteiro.
        numero = int(entrada)
        
        # 3. Verificamos a Sentinela. Esta é a nossa condição de parada.
        # É a lógica mais importante do loop.
        if numero == 0:
            print("Sinal de parada recebido. Calculando...")
            break  # O comando 'break' interrompe o loop 'while' imediatamente.
        
        # 4. Se o código chegou até aqui, significa que o número não era 0.
        # Então, podemos adicioná-lo à nossa soma.
        soma_total = soma_total + numero
        # (Lembre-se da forma mais curta e "Pythônica": soma_total += numero)
        
        # (Opcional) Mostrar a soma parcial pode ser útil para o usuário.
        # print(f"Soma parcial: {soma_total}")

    except ValueError:
        # Este bloco 'except' é o nosso "plano B".
        # Ele é executado se o usuário digitar algo que não pode ser convertido para 'int' (ex: "olá").
        print("Erro: Por favor, digite apenas números inteiros válidos.")

# --- Bloco 3: Apresentação do Resultado ---
# O programa só chega a esta linha DEPOIS que o 'break' é executado.
print("-" * 35)
print(f"✅ A soma final de todos os números digitados é: {soma_total}")