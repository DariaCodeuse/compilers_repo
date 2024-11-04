# Generador de CURPs para Ciudadanos Mexicanos

Este proyecto proporciona una herramienta para generar **CURPs** (Claves Únicas de Registro de Población) para ciudadanos mexicanos. La CURP es un código alfanumérico de 18 caracteres utilizado en México para identificar oficialmente a los residentes del país.

## Características

- Generación automática de CURP basada en información personal.
- Compatible con las normas oficiales para la creación de CURPs en México.
- Interfaz de línea de comandos fácil de usar.

![form1](https://github.com/user-attachments/assets/534ea629-f829-4d9a-b66f-e15f3d2fc616)

![form2](https://github.com/user-attachments/assets/4a42ec24-a8d1-423e-870a-3de56de18aa0)

## Reglas para la Estructura de la CURP

La CURP es una clave alfanumérica de 18 caracteres que sigue las siguientes reglas:

1. **Primeras Cuatro Letras (Identificación del Nombre y Apellidos)**:
   - **1ra Letra**: Primera letra del primer apellido.
   - **2da Letra**: Primera vocal interna del primer apellido.
   - **3ra Letra**: Primera letra del segundo apellido.
   - **4ta Letra**: Primera letra del primer nombre.
      - Nota: Si el nombre es compuesto y comienza con *Maria* o *José*, estos nombres no se consideran y se toma el siguiente nombre.

2. **Fecha de Nacimiento**:
   - Se toma en el formato **AAMMDD**, donde:
      - **AA**: Últimos dos dígitos del año de nacimiento.
      - **MM**: Mes de nacimiento (dos dígitos).
      - **DD**: Día de nacimiento (dos dígitos).

3. **Sexo**:
   - **M** para mujeres y **H** para hombres.

4. **Entidad Federativa de Nacimiento**:
   - Código de dos letras correspondiente a la entidad federativa en México donde nació la persona.
   - Ejemplo: DF para Ciudad de México, NL para Nuevo León, etc.

5. **Consonantes Internas**:
   - **Siguiente consonante del primer apellido**: Primera consonante interna del primer apellido (excluyendo la primera letra).
   - **Siguiente consonante del segundo apellido**: Primera consonante interna del segundo apellido.
   - **Siguiente consonante del primer nombre**: Primera consonante interna del primer nombre.

6. **Homoclave y Dígito Verificador**:
   - Los últimos dos caracteres se generan con base en reglas establecidas por el Registro Nacional de Población (RENAPO), tomando en cuenta factores adicionales como duplicados y características especiales de nombres.
