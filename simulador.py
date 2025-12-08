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

def graficar_datos(tiempos, temperaturas):
    
    plt.plot(tiempos, temperaturas, label="Curva de Enfriamiento", color="blue")
    plt.title("Simulación de Ley de Enfriamiento de Newton")
    plt.xlabel("Tiempo (segundos)") 
    plt.ylabel("Temperatura (°C)")  
    plt.axhline(y=temperaturas[-1], color='r', linestyle='--', label=f"Temp Final: {temperaturas[-1]:.2f}°C")
    plt.legend() 
    plt.grid(True)
    plt.show()

def main():
    print("--- Simulador de Enfriamiento (Cumpliendo RF) ---")
    try:
        # --- Entradas  ---
        t_ini = float(input("Temp. Inicial objeto (°C): "))
        t_amb = float(input("Temp. Ambiente (°C): "))
        k = float(input("Constante k: "))
        total = int(input("Tiempo total (segundos): "))
        dt = float(input("Paso de tiempo/Delta t (ej. 1): "))
            
        print("\nCalculando...")
        eje_x, eje_y = calcular_enfriamiento(t_ini, t_amb, k, total, dt)

        print(f"Simulación finalizada.")
        print(f"Temperatura final: {eje_y[-1]:.2f} °C")
        
        # --- Visualización ---
        print("Generando gráfica...")
        graficar_datos(eje_x, eje_y)

    except ValueError:
        print("Error: Ingresa solo números válidos.")

if __name__ == "__main__":
    main()
