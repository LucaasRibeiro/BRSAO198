def verificador_ano_bissexto():
    print("\n=== VERIFICADOR DE ANO BISSEXTO ===")
    
    try:
        ano = int(input("Digite o ano: "))
        
        if ano <= 0:
            print("Ano inválido! Digite um ano positivo.")
            return
        
        # Regras para ano bissexto:
        # 1. Divisível por 4
        # 2. Não pode ser divisível por 100, a menos que também seja divisível por 400
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"O ano {ano} é BISSEXTO!")
        else:
            print(f"O ano {ano} NÃO é bissexto.")
            
    except ValueError:
        print("Erro! Digite um número inteiro válido.")

# Executar o verificador
verificador_ano_bissexto()