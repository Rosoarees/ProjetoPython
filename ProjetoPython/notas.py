
soma_das_notas = 0
contador_de_notas = 0

print("--- Insira as notas dos alunos ---")
print("(Digite uma nota negativa, como -1, para calcular o resultado final)")

while True:
  
    entrada_usuario = input("Digite uma nota: ")
    nota = float(entrada_usuario)

    
    if nota < 0:
        print("Entendido. Calculando o resultado...")
        break 
    
    
    if nota > 10:
        print("Erro: A nota não pode ser maior que 10. Por favor, tente novamente.")
        continue 

   
    soma_das_notas += nota  
    contador_de_notas += 1 



if contador_de_notas > 0:
    media = soma_das_notas / contador_de_notas
    print("\n--- Resultado Final ---") 
    print(f"O valor total das notas é: {soma_das_notas}")
    print(f"Foram inseridas {contador_de_notas} notas válidas.")
    # Desafio Bónus: Calcular a média!
    print(f"A média das notas é: {media:.2f}") 
else:
    print("\nNenhuma nota foi inserida.")