def conversor_temperatura():
    print("\n=== CONVERSOR DE TEMPERATURA ===")
    
    print("Unidades disponíveis:")
    print("C - Celsius")
    print("F - Fahrenheit") 
    print("K - Kelvin")
    
    try:
        temperatura = float(input("\nDigite a temperatura: "))
        unidade_origem = input("Digite a unidade de origem (C/F/K): ").upper()
        unidade_destino = input("Digite a unidade de destino (C/F/K): ").upper()
        
        unidades_validas = ['C', 'F', 'K']
        
        if unidade_origem not in unidades_validas or unidade_destino not in unidades_validas:
            print("Erro! Unidades devem ser C, F ou K.")
            return
        
        if unidade_origem == unidade_destino:
            resultado = temperatura
        else:
            # Converter para Celsius primeiro
            if unidade_origem == 'F':
                celsius = (temperatura - 32) * 5/9
            elif unidade_origem == 'K':
                celsius = temperatura - 273.15
            else:
                celsius = temperatura
            
            # Converter de Celsius para unidade destino
            if unidade_destino == 'F':
                resultado = (celsius * 9/5) + 32
            elif unidade_destino == 'K':
                resultado = celsius + 273.15
            else:
                resultado = celsius
        
        print(f"\n{temperatura:.1f}°{unidade_origem} = {resultado:.2f}°{unidade_destino}")
        
    except ValueError:
        print("Erro! Digite valores numéricos válidos.")

# Executar o conversor
conversor_temperatura()