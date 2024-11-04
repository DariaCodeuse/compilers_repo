import unicodedata

# Variables de entrada
nombres = 'María Karla'.upper()
pApellido = 'Díaz'.upper()
sApellido = 'Aguilar'.upper()
diaN = '22'.upper()
mesN = '06'.upper()
añoN = '2003'.upper()
sexo = 'Mujer'.upper()
stdo = 'Chiapas'.upper()

# Listas y diccionarios
palabras_restringidas = [
    "BACA", "BUEI", "CACA", "COGE", "FETO", "JOTO", "KULO", "MAME", "PENE", "PUTA", "RUIN", "COLA", "VACA", "PEDO"
]

claves_estados = {
    "AGUASCALIENTES": "AS", "BAJA CALIFORNIA": "BC", "BAJA CALIFORNIA SUR": "BS", "CAMPECHE": "CC",
    "CHIAPAS": "CS", "CHIHUAHUA": "CH", "CIUDAD DE MEXICO": "DF", "COAHUILA": "CL",
    "COLIMA": "CM", "DURANGO": "DG", "GUANAJUATO": "GT", "GUERRERO": "GR",
    "HIDALGO": "HG", "JALISCO": "JC", "MEXICO": "MC", "MICHOACAN": "MN",
    "MORELOS": "MS", "NAYARIT": "NT", "NUEVO LEON": "NL", "OAXACA": "OC",
    "PUEBLA": "PL", "QUERETARO": "QT", "QUINTANA ROO": "QR", "SAN LUIS POTOSI": "SP",
    "SINALOA": "SL", "SONORA": "SR", "TABASCO": "TC", "TAMAULIPAS": "TS",
    "TLAXCALA": "TL", "VERACRUZ": "VZ", "YUCATAN": "YN", "ZACATECAS": "ZS"
}

# Función para eliminar acentos
def noAcentos(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    return ''.join(char for char in texto_normalizado if unicodedata.category(char) != 'Mn')

# Función para reemplazar inicial "Ñ" con "X"
def reemplazar_ñ_con_x(texto):
    if texto[0] == "Ñ":
        return "X" + texto[1:]
    return texto

# Censura de palabras restringidas
def censura(palabra):
    letras = list(palabra)
    for i, letra in enumerate(letras):
        if letra in 'AEIOU':
            letras[i] = 'X'
            break
    return ''.join(letras)

# Obtener clave de estado
def clvEstado(nombreEstado):
    return claves_estados.get(nombreEstado, "Clave no encontrada")

# Obtener clave de sexo
def clvSexo(sexo):
    return 'H' if sexo == 'HOMBRE' else 'M'

# Obtener primera vocal de un apellido (sin acentos)
def primera_vocal(palabra):
    palabra = noAcentos(palabra)
    for letra in palabra[1:]:  # Ignora la primera letra
        if letra in 'AEIOU':
            return letra
    return 'X'

# Obtener la primera letra del primer nombre válido
def primerNombre(nombres):
    nombres = noAcentos(nombres)
    lista_nombres = nombres.split()
    if lista_nombres[0] in ['MARIA', 'JOSE']:
        return lista_nombres[1][0]
    return lista_nombres[0][0]

def sigConsonante(palabra):
    palabra = noAcentos(palabra)  # Elimina acentos
    for letra in palabra[1:]:  # Empieza desde la segunda letra
        if letra  not in 'AEIOU':  # Si es consonante
            return letra
    return 'X'

def generatorCURP(nombre, primer_apellido, segundo_apellido, dia, mes, anio, sexo, estado):
    # Aplicación de reemplazo de "Ñ" y obtención de iniciales
    pA = reemplazar_ñ_con_x(primer_apellido)
    sA = reemplazar_ñ_con_x(segundo_apellido)
    nom = reemplazar_ñ_con_x(nombre)

    # Generación de las primeras 4 letras de la CURP
    pCuatro = pA[0] + primera_vocal(pA) + sA[0] + primerNombre(nom)

    # Reemplazo de palabra antisonante en las primeras cuatro letras
    if pCuatro in palabras_restringidas: pCuatro = censura(pCuatro)

    # Fecha de nacimiento en formato CURP
    fechaN = anio[2:] + mes + dia

    # Clave de sexo y estado
    sexo = clvSexo(sexo)
    estado = clvEstado(estado)

     # Siguientes consonantes
    consoPA = sigConsonante(pA)
    consoSA = sigConsonante(sA)
    consoPN = sigConsonante(nom)
    
    # Construcción final de CURP (sin homoclave)
    curp = pCuatro + fechaN + sexo + estado + consoPA + consoSA + consoPN + "00"

    return curp
    
# print(generatorCURP(nombres,pApellido,sApellido,diaN,mesN,añoN,sexo,stdo))