# --- Verificador de Senha - Versão Simples ---

print("--- Criação de Senha ---")

# 1. Pedimos a senha inicial e guardamo-la.
senha_criada = input("Por favor, crie uma senha: ")

# 2. Pedimos a primeira tentativa de confirmação.
confirmacao_senha = input("Digite a senha novamente para confirmar: ")

# 3. O loop 'while' entra em ação.
# A condição é: "Enquanto a senha criada for DIFERENTE (!=) da confirmação..."
while senha_criada != confirmacao_senha:
    print("\nAs senhas não correspondem! Por favor, tente novamente.")
    # Pedimos a confirmação NOVAMENTE. Esta linha é crucial!
    # Se não pedirmos de novo, o loop será infinito.
    confirmacao_senha = input("Digite a senha novamente para confirmar: ")

# 4. Se o programa chegou aqui, significa que o loop terminou.
# E o loop só termina quando a condição (senha_criada != confirmacao_senha) se torna FALSA.
# Ou seja, quando as senhas são IGUAIS.
print("\nSenha definida com sucesso! ✅")