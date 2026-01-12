import matplotlib.pyplot as plt
import csv  # libreria para generar excel
import os   # para manejar nombres de archivos

def calcular_enfriamiento(t_inicial, t_ambiente, k, tiempo_total, paso_tiempo):
    """
    Motor matemático: Método de Euler.
    """
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

def guardar_reporte_csv(nombre_escenario, tiempos, temperaturas):
    """
    Genera un archivo .csv compatible con Excel.
    """
    filename = f"reporte_{nombre_escenario}.csv"
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Tiempo (s)", "Temperatura (°C)"]) # los encabezados
            for t, temp in zip(tiempos, temperaturas):
                writer.writerow([t, f"{temp:.2f}"])
        print(f"   [💾] ¡Reporte guardado exitosamente como '{filename}'!")
    except Exception as e:
        print(f"   [X] Error al guardar archivo: {e}")

def analizar_objetivo(tiempos, temperaturas, temp_objetivo=60):
    """
    Busca en qué momento se alcanza una temperatura específica (ej. para beber).
    """
    for t, temp in zip(tiempos, temperaturas):
        if temp <= temp_objetivo:
            return t
    return None # nunca llegó a esa temperatura en el tiempo simulado

def main():
    print("--- Simulador PRO: Enfriamiento de Newton + Reportes ---")
    
    plt.figure(figsize=(10, 6))
    plt.title("Comparativa de Enfriamiento con Análisis")
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Temperatura (°C)")
    plt.grid(True)
    
    contador = 1
    continuar = True
    
    while continuar:
        try:
            print(f"\n=== ESCENARIO #{contador} ===")
            nombre = input("1. Nombre del objeto (ej. Cafe): ")
            t_ini = float(input("2. Temp. Inicial (°C): "))
            t_amb = float(input("3. Temp. Ambiente (°C): "))
            k = float(input("4. Constante k (ej. 0.05): "))
            total = int(input("5. Tiempo total (segundos): "))
            dt = float(input("6. Paso de tiempo (ej. 1): "))
            
            # --- CÁLCULO ---
            eje_x, eje_y = calcular_enfriamiento(t_ini, t_amb, k, total, dt)
            
            # --- ANÁLISIS AUTOMÁTICO ---
            # suponemos que 60°C es la temperatura ideal para beber
            tiempo_meta = analizar_objetivo(eje_x, eje_y, temp_objetivo=60)
            msg_meta = ""
            if tiempo_meta is not None:
                msg_meta = f" | Llega a 60°C en {tiempo_meta}s"
                print(f"   [i] ANÁLISIS: El objeto alcanza 60°C a los {tiempo_meta} segundos.")
                # marcar el punto en la gráfica
                plt.plot(tiempo_meta, 60, 'ro') # punto rojo
            
            # --- EXPORTACIÓN DE DATOS ---
            guardar = input("   ¿Generar reporte Excel (CSV)? (s/n): ").lower()
            if guardar == 's':
                guardar_reporte_csv(nombre, eje_x, eje_y)
            
            # --- GRAFICACIÓN ---
            etiqueta = f"{nombre} (k={k}){msg_meta}"
            plt.plot(eje_x, eje_y, label=etiqueta)
            
            # --- BUCLE ---
            respuesta = input("\n¿Agregar otro escenario? (s/n): ").lower()
            if respuesta != 's':
                continuar = False
            else:
                contador += 1
                
        except ValueError:
            print("Error: Ingresa números válidos.")
    
    print("\nAbriendo gráfica final...")
    plt.legend()
    plt.axhline(y=60, color='g', linestyle=':', alpha=0.5, label="Temp. Bebible (60°C)")
    plt.show()

if __name__ == "__main__":
    main()
