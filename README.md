# Simulador de Ley de Enfriamiento de Newton 🌡️

Este proyecto es una herramienta de simulación numérica desarrollada en Python que modela el enfriamiento de objetos en el tiempo.

## 📋 Descripción del Proyecto
El simulador permite visualizar cómo disminuye la temperatura de un cuerpo hasta alcanzar el equilibrio térmico con el ambiente, permitiendo comparar distintos materiales.

## ✅ Requisitos Funcionales (Cumplidos)
Este proyecto cubre la totalidad de los requisitos solicitados:
* **RF1 - Gestión de Parámetros:** El usuario puede ingresar T_inicial, T_ambiente, constante k y tiempo total.
* **RF2 - Cálculo Numérico:** Implementación del algoritmo de Euler paso a paso.
* **RF3 - Visualización:** Gráficas dinámicas con `matplotlib` que permiten comparar múltiples curvas (ej. Café vs. Metal).
* **RF4 - Persistencia:** Generación automática de reportes en Excel (.csv).

## ⚙️ Instalación y Requisitos
Para correr este código necesitas:
1. Python 3.x
2. Librería Matplotlib

Comando para instalar dependencias:
```bash
pip install -r requirements.txt
