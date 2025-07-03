# Programa: Validador de Usuário e Senha
print("Cadastro de Usuário\n" + "=" * 30)

while True:
    # Solicita nome de usuário
    usuario = input("Digite seu nome de usuário: ").strip()
    
    # Solicita senha
    senha = input("Digite sua senha: ").strip()
    
    # Verifica se senha é igual ao usuário
    if senha.lower() == usuario.lower():
        print("\nErro: A senha não pode ser igual ao nome de usuário!\n")
    else:
        print("\nCadastro realizado com sucesso!")
        print(f"Usuário: {usuario}")
        print(f"Senha: {'*' * len(senha)}")  # Exibe asteriscos no lugar da senha
        break