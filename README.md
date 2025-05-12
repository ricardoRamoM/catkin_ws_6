# {Tutorial: Simulación y Ejecución de un Pick and Place con el Brazo UR5 y Gripper Robotiq usando ROS Noetic, Gazebo y MoveIt}

Este tutorial te guía paso a paso para simular y ejecutar una tarea de pick and place utilizando el brazo robótico UR5 y el gripper Robotiq 2F-85, integrando herramientas como Gazebo, MoveIt, RViz y Python en ROS Noetic sobre Ubuntu 20.04. Comenzarás configurando un entorno de simulación funcional y terminarás controlando el robot físico desde una computadora remota, aplicando los mismos scripts desarrollados en el entorno virtual. Ideal para quienes buscan unir teoría, simulación y práctica real en robótica colaborativa.

---

## 📋 Requisitos Previos

🖥️ **Hardware mínimo recomendado**

- Procesador de 2 núcleos o más
- 4 GB de RAM mínimo (se recomienda 8 GB o más para una experiencia fluida con Gazebo)
- Tarjeta gráfica dedicada o integrada compatible con OpenGL (recomendado para simulación en Gazebo)
- Al menos 20 GB de espacio libre en disco

💻 **Entorno y sistema operativo**

- Ubuntu 20.04 LTS (recomendado como sistema principal o en una partición dedicada)
- Evitar máquinas virtuales si se trabajará con simulación en Gazebo, ya que pueden generar problemas de rendimiento y compatibilidad gráfica

📚 **Conocimientos técnicos sugeridos**

- Uso básico de la terminal de Linux
- Conocimientos fundamentales de ROS: Nodos, tópicos, servicios y catkin
- Conceptos básicos de MoveIt y RViz
- Programación básica en Python
- Conocimiento básico de cinemática de robots (opcional pero útil)

---

## 📖  Introducción

En este tutorial aprenderás a simular, planificar trayectorias y controlar una tarea de pick and place utilizando el brazo robótico UR5 con el gripper Robotiq 2F-85, integrando herramientas del ecosistema de ROS Noetic sobre Ubuntu 20.04.

El flujo del proyecto abarca desde la simulación completa del sistema en el entorno virtual de Gazebo, la planificación y ejecución de movimientos mediante MoveIt, la visualización y prueba de trayectorias en RViz, hasta la conexión con el robot físico UR5 desde una computadora remota usando scripts en Python y MoveIt Commander.

Este proyecto combina varios componentes clave del ecosistema ROS:

    🧩 Gazebo: Simulador 3D que permite modelar entornos físicos realistas para probar comportamientos del robot antes de llevarlos al mundo real.

    🦾 MoveIt: Framework de planificación de movimiento que considera cinemática, obstáculos, límites articulares y más.

    👁️ RViz: Herramienta de visualización 3D utilizada para monitorear, planificar y validar los movimientos del robot en tiempo real.

    🐍 Python + ROS: Scripts personalizados para automatizar secuencias de pick and place y controlar el gripper mediante MoveIt Commander.

Una vez validado el sistema en simulación, se procede a establecer comunicación con el UR5 físico mediante conexión por red, permitiendo ejecutar exactamente la misma lógica desarrollada en el entorno virtual.

Este tutorial está diseñado para estudiantes, investigadores y entusiastas de la robótica que deseen aprender a integrar simulación y hardware real usando ROS, enfocándose en aplicaciones prácticas como la automatización de procesos mediante pick and place.


## Configuración del entorno

