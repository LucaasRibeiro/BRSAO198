def classificador_idade():
    print("=== CLASSIFICADOR DE IDADE ===")
    
    try:
        idade = int(input("Digite sua idade: "))
        
        if idade < 0:
            print("Idade inválida! Digite um valor positivo.")
        elif idade <= 12:
            print(f"Com {idade} anos, você é uma Criança.")
        elif idade <= 17:
            print(f"Com {idade} anos, você é um Adolescente.")
        elif idade <= 59:
            print(f"Com {idade} anos, você é um Adulto.")
        else:
            print(f"Com {idade} anos, você é um Idoso.")
            
    except ValueError:
        print("Erro! Digite um número inteiro válido.")

# Executar o classificador
classificador_idade()