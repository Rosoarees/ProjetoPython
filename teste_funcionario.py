from funcionario import Funcionário

funcionario = Funcionário("Matheus", "matheus@blablabla.com.br")

funcionario.cadastro_hora("Jan", 300)
funcionario.cadastro_hora("Fev", 200)
funcionario.cadastro_salario_hora("Jan", 30)
funcionario.cadastro_salario_hora("Fev", 30)

print(funcionario)
print(f"Salário Janeiro: R$ {funcionario.calcula_salario('Jan')}")
print(f"Salário Fevereiro: R$ {funcionario.calcula_salario('Fev')}")