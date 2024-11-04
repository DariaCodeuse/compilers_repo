import ply.lex as lex

tokens = [
    'NOMBRE', 'PRIMER_APELLIDO', 'SEGUNDO_APELLIDO', 
    'DIA', 'MES', 'ANIO', 'SEXO', 'ESTADO'
]

# Definiciones de patrones para cada token con sufijos
t_NOMBRE = r'[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+_nom'
t_PRIMER_APELLIDO = r'[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+_pa'
t_SEGUNDO_APELLIDO = r'[A-Za-zÁÉÍÓÚÑáéíóúñ\s]+_sa'
t_DIA = r'\b(0[1-9]|[12][0-9]|3[01])_d\b'
t_MES = r'\b(0[1-9]|1[0-2])_m\b'
t_ANIO = r'\b(19|20)\d{2}\b'
t_SEXO = r'\b(HOMBRE|MUJER)\b'
t_ESTADO = r'[A-Z\s]+_es'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Función auxiliar para quitar sufijos de los valores
def remover_sufijos(valor):
    sufijos = ['_nom', '_pa', '_sa', '_d', '_m', '_es']
    for sufijo in sufijos:
        valor = valor.replace(sufijo, '')
    return valor

# Función para analizar datos usando el lexer y procesar cada variable
def getTokens(nombre, primer_apellido, segundo_apellido, dia, mes, anio, sexo, estado):
    ciudadano = {
        'NOMBRE': nombre.upper() + '_nom',
        'PRIMER_APELLIDO': primer_apellido.upper()  + '_pa',
        'SEGUNDO_APELLIDO': segundo_apellido.upper()  + '_sa',
        'DIA': str(dia).zfill(2) + '_d',
        'MES': str(mes).zfill(2) + '_m',
        'ANIO': str(anio),
        'SEXO': sexo.upper() ,
        'ESTADO': estado.upper() + '_es'
    }

    tokens_resultantes = []

    # Analizar cada dato individualmente
    for tokType, tokValue in ciudadano.items():
        lexer.input(tokValue)  # Cargar el valor en el lexer
        token = lexer.token()  # Extraer el token

        # Mostrar detalles de depuración
        print(f"Analizando {tokType}: {tokValue}")
        print("Token generado:", token)

        # Validar y almacenar el token
        if token and token.type == tokType:
            tokens_resultantes.append(remover_sufijos(token.value)) # Quitar sufijo antes de almacenar
        else:
            # Si el tipo de token no coincide
            return f"Error: {tokType} inválido: {tokValue}"

    return tokens_resultantes

# # Ejemplo de prueba
# nombres = 'Karla'
# pApellido = 'Díaz'
# sApellido = 'Aguilar'
# diaN = 22
# mesN = 6
# anioN = 2003
# sexo = 'Mujer'
# stdo = 'Chiapas'

# resultado = getTokens(nombres, pApellido, sApellido, diaN, mesN, anioN, sexo, stdo)
# print("\nResultado Final:", *resultado)
