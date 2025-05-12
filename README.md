# {Tutorial: Guía paso a paso para simular y controlar el brazo UR5 con MoveIt, Gazebo y Python (ROS Noetic)}

El siguiente tutorial tiene como objetivo desarrollar "Pick and place" para el brazo róbotico colaborativo "UR5" 
---

## 📋 Requisitos Previos

🖥️ Hardware mínimo recomendado

- Procesador de 2 núcleos o más
- 4 GB de RAM mínimo (se recomienda 8 GB o más para una experiencia fluida con Gazebo)
- Tarjeta gráfica dedicada o integrada compatible con OpenGL (recomendado para simulación en Gazebo)
- Al menos 20 GB de espacio libre en disco

💻 Entorno y sistema operativo

- Ubuntu 20.04 LTS (recomendado como sistema principal o en una partición dedicada)
- Evitar máquinas virtuales si se trabajará con simulación en Gazebo, ya que pueden generar problemas de rendimiento y compatibilidad gráfica

📚 Conocimientos técnicos sugeridos

- Uso básico de la terminal de Linux
- Conocimientos fundamentales de ROS: Nodos, tópicos, servicios y catkin
- Conceptos básicos de MoveIt y RViz
- Programación básica en Python
- Conocimiento básico de cinemática de robots (opcional pero útil)

---

## 📖  Introducción

En este tutorial aprenderás a simular, planificar trayectorias y controlar un brazo robótico UR5 con un gripper Robotiq 2F-85 utilizando el entorno de simulación Gazebo, el planificador MoveIt, y la visualización en RViz, todo funcionando en ROS Noetic sobre Ubuntu 20.04. Además, se cubre la conexión y control del robot físico desde una computadora remota mediante scripts en Python y MoveIt Commander.

Este proyecto combina varios componentes clave del ecosistema ROS:

- **Gazebo**: Simulador 3D que permite probar comportamientos físicos del robot.
- **MoveIt**: Herramienta de planificación de movimiento que integra cinemática, colisiones y control.
- **RViz**: Visualizador en 3D donde puedes observar el modelo del robot, planificar y ejecutar movimientos.
- **Python + ROS**: Scripts personalizados para automatizar tareas como pick and place.

Este tutorial es ideal para estudiantes de robótica, investigadores o desarrolladores que deseen aprender cómo integrar simulación y hardware real usando ROS.


## Configuración del entorno

