# Analizador Léxico y Sintáctico
Este proyecto es un programa que realiza un análisis léxico y sintáctico de una estructura `for` dada. Actualmente, el programa analiza estructuras de bucles `for` en el siguiente formato:
![syntax-error](https://github.com/user-attachments/assets/a1605919-6627-4bc2-b6d0-d32bdcccfaae)

## Darkmode 
![main-darkmode](https://github.com/user-attachments/assets/5a1c8305-3039-405e-9d6b-57011fae5aac)

#Workning
![working](https://github.com/user-attachments/assets/581cc24d-8f82-4cfc-8310-2755f3d536fa)


```java
for (int i = 1; i <= 5; i++) {
    System.out.println("El valor de la cifra es: " + i);
}
```
El objetivo del programa es identificar los tokens presentes en la estructura y verificar que el código siga las reglas sintácticas correctas.



## Estructura del Proyecto

El proyecto está construido con Flask e incluye las siguientes carpetas y archivos principales:

- lex.py: Contiene el código para el análisis léxico, donde se identifican los tokens del código fuente.
- app.py: Controlador principal de la aplicación Flask, maneja las rutas y la interfaz web.
- syntax.py: Realiza el análisis sintáctico para validar la estructura del código analizado.
- templates/: Carpeta que contiene las plantillas HTML usadas por Flask.
- static/: Contiene archivos estáticos como CSS, JavaScript y fuentes.
    - css/: Hojas de estilo.
    - js/: Código JavaScript, incluyendo el interruptor para el modo oscuro.
    - fonts/: Fuentes utilizadas en el proyecto.

También se utiliza un archivo JSON que define los tokens del lenguaje. Este archivo contiene el diccionario de tipos de tokens como identificadores, palabras reservadas, operadores, delimitadores, etc.

## Ejecución del Programa (Debug Mode)
1. Clona el repositorio y navega al directorio del proyecto.
2. Ve al proyecto "\analizador" en tu terminal y ejecuta:

```
.\.venv\Scripts\activate
```
3. Ejecuta la aplicación en Modo Debug (por el momento):
```
flask --app app --debug run
```

## Mejoras Futuras
**El proyecto está en desarrollo, y algunas mejoras previstas incluyen:**

- Soporte para más estructuras del lenguaje de programación.
- Ampliación del análisis sintáctico para más casos de uso.
- Refactorización del código para optimizar el rendimiento.
- Ampliación del archivo JSON para incluir más tokens y reglas de análisis.
