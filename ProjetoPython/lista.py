# Inicializa a lista
lista = [4, 5, 3, 5]
print("Lista inicial:", lista)  # [4, 5, 3, 5]

# Adiciona o número 2 no final
lista.append(2)
print("Após append(2):", lista)  # [4, 5, 3, 5, 2]

# Insere -3 na posição 2
lista.insert(2, -3)
print("Após insert(2, -3):", lista)  # [4, 5, -3, 3, 5, 2]

# Remove o primeiro elemento 4 encontrado
lista.remove(4)
print("Após remove(4):", lista)  # [5, -3, 3, 5, 2]

# Ordena a lista
lista.sort()
print("Após sort():", lista)  # [-3, 2, 3, 5, 5]

# Inverte a ordem dos elementos
lista.reverse()
print("Após reverse():", lista)  # [5, 5, 3, 2, -3]

# Conta quantas vezes o número 5 aparece
print("Contagem de 5:", lista.count(5))  # 2

# Remove e retorna o último elemento
print("Elemento removido com pop():", lista.pop())  # -3
print("Após pop():", lista)  # [5, 5, 3, 2]

# Ordena novamente
lista.sort()
print("Após sort():", lista)  # [2, 3, 5, 5]

# Remove o elemento na posição 2
del lista[2]
print("Após del lista[2]:", lista)  # [2, 3, 5]

# Remove os elementos das posições 2 até 5 (não existe posição 5, então remove até o final)
del lista[2:5]
print("Após del lista[2:5]:", lista)  # [2, 3]

# Limpa toda a lista
lista.clear()
print("Após clear():", lista)  # []