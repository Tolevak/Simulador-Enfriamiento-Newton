import matplotlib.pyplot as plt

def calcular_enfriamiento(t_inicial, t_ambiente, k, tiempo_total, paso_tiempo=!):
   
"""
se aplica el Metodo de Euler para simular el enfriamiento.
 retorna dos listas: tiempos y temperaturas.
"""
    
# listas para guardar el historial
    
tiempos = [0] temperaturas = [t_inicial]
temperaturas = [t_inicial]

# variables acumuladoras 
t_actual = t_inicial
tiempo_actual = 0

#bucle principal
while tiempo_actual < tiempo_total:
    # 1. calcular la derivada 
    derivada = -k * (t_actual - t_ambiente)
    # 2. calcular el cambio 
    cambio = derivada * paso_tiempo
    #3. actualizar valores
    t_actual += cambio
    tiempo_actual += paso_tiempo
    #4. guardar en listas
    tiempos.append(tiempo_actual)
    temperaturas.append(t_actual)
    
return tiempos, temperaturas
    


    pass

def graficar_datos(tiempos, temperaturas):
    """
    Función para generar la gráfica con Matplotlib.
    """
    # Aquí irá la configuración de la gráfica
    pass

def main():
    # 1. Solicitar datos al usuario
    print("--- Simulador de Enfriamiento de Newton ---")
    
    # 2. Ejecutar simulación
    
    # 3. Mostrar resultados
    print("Simulación finalizada.")

if __name__ == "__main__":
    main()
