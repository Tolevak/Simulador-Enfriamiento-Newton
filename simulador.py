import matplotlib.pyplot as plt
import csv
import os

def obtener_numero(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0 and "Tiempo" in mensaje:
                print("   [!] El tiempo no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print(f"   [X] Error: Debes ingresar un número válido. Intenta de nuevo.")

def calcular_euler(t_inicial, t_ambiente, k, tiempo_total, paso_tiempo):
    """
    Aplica el algoritmo numérico de Euler.
    Retorna dos listas: (eje_x_tiempos, eje_y_temperaturas)
    """
    tiempos = [0]
    temps = [t_inicial]
    
    t_actual = t_inicial
    tiempo_actual = 0
    
    while tiempo_actual < tiempo_total:
        # Fórmula: dT/dt = -k * (T - Ta)
        derivada = -k * (t_actual - t_ambiente)
        
        # Euler: T_nuevo = T_actual + (derivada * dt)
        t_actual += derivada * paso_tiempo
        tiempo_actual += paso_tiempo
        
        tiempos.append(tiempo_actual)
        temps.append(t_actual)
        
    return tiempos, temps

def guardar_csv(nombre, tiempos, temps):
    """Guarda los resultados en un archivo compatible con Excel."""
    filename = f"reporte_{nombre}.csv"
    try:
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Tiempo (s)", "Temperatura (°C)"])
            for t, temp in zip(tiempos, temps):
                writer.writerow([t, f"{temp:.2f}"])
        print(f"   [💾] Datos guardados en: {filename}")
    except Exception as e:
        print(f"   [X] No se pudo guardar el archivo: {e}")

def main():
    print("==========================================")
    print("   SIMULADOR DE ENFRIAMIENTO DE NEWTON    ")
    print("==========================================")
    
    # Configuración inicial de la gráfica
    plt.figure(figsize=(10, 6))
    plt.title("Comparativa de Escenarios de Enfriamiento")
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True, linestyle='--', alpha=0.7)
    
    contador = 1
    
    while True:
        print(f"\n--- Nuevo Escenario #{contador} ---")
        
        # 1. Entrada de datos 
        nombre = input("1. Nombre del objeto (ej. Café): ") or f"Objeto_{contador}"
        t_ini = obtener_numero("2. Temperatura Inicial (°C): ")
        t_amb = obtener_numero("3. Temperatura Ambiente (°C): ")
        k = obtener_numero("4. Constante de enfriamiento k (ej. 0.05): ")
        total = obtener_numero("5. Tiempo total a simular (segundos): ", int)
        dt = obtener_numero("6. Paso de tiempo (Delta t): ")

        # 2. Procesamiento
        eje_x, eje_y = calcular_euler(t_ini, t_amb, k, total, dt)
        
        # 3. Análisis Rápido
        temp_final = eje_y[-1]
        print(f"   -> Resultado: Temp final de {temp_final:.2f}°C")
        
        # 4. Graficación
        etiqueta = f"{nombre} (k={k}, Ti={t_ini}°)"
        plt.plot(eje_x, eje_y, label=etiqueta, linewidth=2)
        
        # 5. Persistencia (Opcional)
        guardar = input("   ¿Guardar reporte Excel? (s/n): ").lower()
        if guardar == 's':
            guardar_csv(nombre, eje_x, eje_y)
            
        # 6. Continuidad
        otro = input("\n¿Quieres agregar otro objeto a la gráfica? (s/n): ").lower()
        if otro != 's':
            break
        contador += 1

    print("\n[i] Generando gráfica final... Cierra la ventana para terminar.")
    plt.legend()
    plt.tight_layout()
    plt.show()
    print("--- Fin de la simulación ---")

if __name__ == "__main__":
    main()
