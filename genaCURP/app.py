from datetime import datetime
from flask import Flask, render_template, request
from curp import claves_estados, generatorCURP
from lex import getTokens

app = Flask(__name__)

estados = list(claves_estados.keys())

@app.route('/', methods=['GET', 'POST'])
def index():
    curp = None
    mensaje_error = None
    mensaje_exito = None

    if request.method == 'POST':
        # Recibir los datos del formulario
        nom = request.form['nombre']
        pApellido = request.form['primer_apellido']
        sApellido = request.form['segundo_apellido']
        fechaN = request.form['fecha_nacimiento']
        sexo = request.form['sexo']
        est = request.form['estado']
        # Convertir la fecha y desglosarla
        fecha = datetime.strptime(fechaN, '%Y-%m-%d')
        dia, mes, año = fecha.strftime("%d"), fecha.strftime("%m"), fecha.strftime("%Y")
        
        try:
            # Llamar al lexer para analizar los datos
            lexTokens = getTokens(nom, pApellido, sApellido, dia, mes, año, sexo, est)

            if isinstance(lexTokens, list) and len(lexTokens) == 8:
                curp = generatorCURP(*lexTokens)  # Generar CURP si los tokens son válidos
                mensaje_exito = "CURP Generada con éxito!"
            else:
                mensaje_error = lexTokens  # Asignar mensaje de error si hay un problema con los tokens

        except ValueError as e:
            mensaje_error = f"Error al procesar la CURP: {e}"

    # Renderizar la plantilla y pasar las variables necesarias
    return render_template(
        'index.html', 
        estados=estados, curp=curp, 
        mensaje_error=mensaje_error, mensaje_exito=mensaje_exito
    )

if __name__ == '__main__':
    app.run(debug=True)
