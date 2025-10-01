def calculadora_consumo():
    print("\n=== CALCULADORA DE CONSUMO DE COMBUSTÍVEL ===")
    
    # Dados fornecidos
    distancia_percorrida = 300  # km
    combustivel_gasto = 25  # litros
    
    # Cálculo do consumo médio
    consumo_medio = distancia_percorrida / combustivel_gasto
    
    # Exibição dos resultados
    print(f"Distância percorrida: {distancia_percorrida} km")
    print(f"Combustível gasto: {combustivel_gasto} litros")
    print(f"Consumo médio: {consumo_medio:.2f} km/l")

# Executar a calculadora de consumo
calculadora_consumo()