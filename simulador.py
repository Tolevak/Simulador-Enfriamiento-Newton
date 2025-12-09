import matplotlib.pyplot as plt

def calcular_enfriamiento(t_inicial, t_ambiente, k, tiempo_total, paso_tiempo):
    # --- Lógica Matemática ---
    tiempos = [0]
    temperaturas = [t_inicial]
    t_actual = t_inicial
    tiempo_actual = 0

    while tiempo_actual < tiempo_total:
        derivada = -k * (t_actual - t_ambiente)
        cambio = derivada * paso_tiempo
        t_actual += cambio
        tiempo_actual += paso_tiempo
        
        tiempos.append(tiempo_actual)
        temperaturas.append(t_actual)
        
    return tiempos, temperaturas

def main():
    print("--- Simulador Multi-Escenario (Comparativo RF3.3) ---")
    
    # Gráfica
    plt.figure(figsize=(10, 6))
    plt.title("Comparación de Enfriamiento: Múltiples Escenarios")
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True)
    
    contador_escenarios = 1
    continuar = True
    
    while continuar:
        try:
            print(f"\n--- Escenario #{contador_escenarios} ---")
            nombre = input("Nombre del objeto (ej. Café, Metal): ")
            t_ini = float(input("Temp. Inicial objeto (°C): "))
            t_amb = float(input("Temp. Ambiente (°C): "))
            k = float(input("Constante k (ej. 0.05): "))
            total = int(input("Tiempo total (segundos): "))
            dt = float(input("Paso de tiempo (ej. 1): "))
            
            # Calcular
            eje_x, eje_y = calcular_enfriamiento(t_ini, t_amb, k, total, dt)
            
            # Agregar curva a la gráfica
            etiqueta = f"{nombre} (k={k}, Ti={t_ini})"
            plt.plot(eje_x, eje_y, label=etiqueta)
            
            print(f"-> Escenario {nombre} procesado.")
            
            # Preguntar si quiere otro
            respuesta = input("\n¿Agregar otro escenario a la gráfica? (s/n): ").lower()
            if respuesta != 's':
                continuar = False
            else:
                contador_escenarios += 1
                
        except ValueError:
            print("Error: Ingresa números válidos.")
    
    # Al final de todo, mostramos la gráfica completa
    print("\nGenerando gráfica comparativa...")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
