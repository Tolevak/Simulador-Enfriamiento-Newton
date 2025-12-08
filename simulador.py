import matplotlib.pyplot as plt

def calcular_enfriamiento(t_inicial, t_ambiente, k, tiempo_total, paso_tiempo=1):
    # --- INICIO DE LA FUNCIÓN ---
    # Listas para guardar el historial
    tiempos = [0]
    temperaturas = [t_inicial]

    # Variables acumuladoras
    t_actual = t_inicial
    tiempo_actual = 0

    # Bucle principal
    while tiempo_actual < tiempo_total:
        # 1. Calcular la derivada
        derivada = -k * (t_actual - t_ambiente)
        
        # 2. Calcular el cambio
        cambio = derivada * paso_tiempo
        
        # 3. Actualizar valores
        t_actual += cambio
        tiempo_actual += paso_tiempo
        
        # 4. Guardar en listas
        tiempos.append(tiempo_actual)
        temperaturas.append(t_actual)
        
    return tiempos, temperaturas

def graficar_datos(tiempos, temperaturas):
    """
    Función para generar la gráfica con Matplotlib.
    """
    # Aquí irá la configuración de la gráfica en la siguiente sesión
    pass

def main():
    # --- INICIO DEL PROGRAMA PRINCIPAL ---
    # 1. Solicitar datos al usuario
    print("--- Simulador de Enfriamiento de Newton ---")
    try:
        t_ini = float(input("Ingresa Temperatura Inicial del objeto (°C): "))
        t_amb = float(input("Ingresa Temperatura Ambiente (°C): "))
        k = float(input("Ingresa constante k: "))
        total = int(input("Tiempo total a simular (segundos): "))
            
        # 2. Ejecutar simulación
        print("\nCalculando..")
        # OJO: Aquí faltaba una coma entre eje_x y eje_y
        eje_x, eje_y = calcular_enfriamiento(t_ini, t_amb, k, total)

        # 3. Mostrar resultados
        print(f"Simulación finalizada.")
        print(f"Temperatura final del objeto: {eje_y[-1]:.2f} °C después de {total} s")
        # pendiente graficar los datos de eje x y

    except ValueError:
        print("Error: Por favor ingresa solo números válidos.")

if __name__ == "__main__":
    main()
