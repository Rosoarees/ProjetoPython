# --- Identificador de Números Pares (Abordagem 'Pythônica') ---

print("\n--- Números Pares entre 1 e 100 ---")
print("Método 2: Usando o 'passo' da função range.")

# 1. O Loop 'for' inteligente
# Começamos em 2 (o primeiro par) e vamos até 101, pulando de 2 em 2.
# O 'passo' 2 garante que só receberemos números pares.
for numero in range(2, 101, 2):
    
    # 2. Como já garantimos que o número é par, não precisamos do 'if'.
    # Apenas exibimos o número diretamente.
    print(numero)

print("-" * 20)
print("Fim do programa.")