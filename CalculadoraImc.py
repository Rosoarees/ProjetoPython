def calcular_imc():
  
  
    print("          CALCULADORA DE IMC")
  
    
  
    while True:
        try:
            peso = float(input("• Digite o seu peso em kg: ").replace(",", "."))
            if peso <= 0 or peso > 300:
                print(" Peso inválido! Digite um valor entre 0.1 e 300 kg.")
                continue
            break
        except ValueError:
            print(" Erro! Digite apenas números. Use ponto ou vírgula como separador.")
    
  
    while True:
        try:
            altura = float(input("• Digite a sua altura em metros: ").replace(",", "."))
            if altura <= 0.5 or altura > 2.5:
                print(" Altura inválida! Digite um valor entre 0.5 e 2.5 metros.")
                continue
            break
        except ValueError:
            print("  Erro! Digite apenas números. Use ponto ou vírgula como separador.")
    
   
    imc = peso / (altura ** 2)
    
   
    classificacao = classificar_imc(imc)
    
   
   
    print("          RESULTADO")
   
    print(f"• Peso: {peso:.1f} kg")
    print(f"• Altura: {altura:.2f} m")
    print(f"• IMC: {imc:.1f}")
    print(f"• Classificação: {classificacao['categoria']}")
    print(f"• Situação: {classificacao['status']}")
   
    
  
    exibir_recomendacoes(imc, classificacao['categoria'])
    
    return imc

def classificar_imc(imc):
   
    if imc < 18.5:
        return {"categoria": "Abaixo do peso", "status": "  Cuidado!"}
    elif 18.5 <= imc < 25:
        return {"categoria": "Peso normal", "status": " Saudável"}
    elif 25 <= imc < 30:
        return {"categoria": "Sobrepeso", "status": " Atenção!"}
    elif 30 <= imc < 35:
        return {"categoria": "Obesidade Grau I", "status": " Risco moderado"}
    elif 35 <= imc < 40:
        return {"categoria": "Obesidade Grau II", "status": " Risco alto"}
    else:
        return {"categoria": "Obesidade Grau III", "status": " Risco muito alto"}

def exibir_recomendacoes(imc, categoria):
  
    print("\n    jRECOMENDAÇÕES:")
    
    if categoria == "Abaixo do peso":
        print("• Consulte um nutricionista para ganho de peso saudável")
        print("• Aumente o consumo de alimentos nutritivos")
        print("• Pratique exercícios de força")
        
    elif categoria == "Peso normal":
        print("• Mantenha seus hábitos saudáveis!")
        print("• Continue com alimentação balanceada")
        print("• Pratique atividades físicas regularmente")
        
    elif categoria == "Sobrepeso":
        print("• Considere reduzir calorias na alimentação")
        print("• Aumente a prática de exercícios físicos")
        print("• Consulte um nutricionista para orientação")
        
    else:
        print("• Procure um médico ou nutricionista urgentemente")
        print("• Adote uma alimentação equilibrada e controlada")
        print("• Pratique exercícios com orientação profissional")
        print("• Considere acompanhamento multidisciplinar")

def tabela_classificacao():
   
    print("\n TABELA DE CLASSIFICAÇÃO IMC (OMS):")
    print("Abaixo de 18.5 - Abaixo do peso")
    print("18.5 a 24.9    - Peso normal")
    print("25.0 a 29.9    - Sobrepeso")
    print("30.0 a 34.9    - Obesidade Grau I")
    print("35.0 a 39.9    - Obesidade Grau II")
    print("Acima de 40.0  - Obesidade Grau III")

def main():
   
    try:
        while True:
            calcular_imc()
            
           
            continuar = input("\n🔁 Deseja calcular outro IMC? (s/n): ").lower()
            if continuar != 's':
                print("\nObrigado por usar a Calculadora de IMC! ")
                break
                
            print("\n" + "="*50 + "\n")
            
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário. Até logo! ")
    except Exception as e:
        print(f"\n Erro inesperado: {e}")


def calculadora_simples():
  
    try:
        peso = float(input("Digite o seu peso em kg: ").replace(",", "."))
        altura = float(input("Digite a sua altura em metros: ").replace(",", "."))
        
        if peso <= 0 or altura <= 0:
            print("Erro: Valores devem ser positivos!")
            return
        
        imc = peso / (altura ** 2)
        classificacao = classificar_imc(imc)
        
        print(f"\nSeu IMC é: {imc:.1f}")
        print(f"Classificação: {classificacao['categoria']}")
        print(f"Situação: {classificacao['status']}")
        
    except ValueError:
        print("Erro: Digite valores numéricos válidos!")

if __name__ == "__main__":
   
    main()
    
   