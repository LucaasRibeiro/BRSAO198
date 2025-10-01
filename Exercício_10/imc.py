def calculadora_imc():
    print("\n=== CALCULADORA DE IMC ===")
    
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        if peso <= 0 or altura <= 0:
            print("Erro! Peso e altura devem ser valores positivos.")
            return
        
        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"
        
        print(f"\nPeso: {peso:.1f} kg")
        print(f"Altura: {altura:.2f} m")
        print(f"IMC: {imc:.1f}")
        print(f"Classificação: {classificacao}")
        
    except ValueError:
        print("Erro! Digite valores numéricos válidos.")

# Executar a calculadora de IMC
calculadora_imc()