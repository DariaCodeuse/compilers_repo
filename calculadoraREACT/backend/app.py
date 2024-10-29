from flask import Flask, request, jsonify
from lex import all_tokens  # Importa la función que hiciste

app = Flask(__name__)

# Ruta que procesa la expresión enviada desde el frontend
@app.route('/api/lex', methods=['POST'])
def process_expression():
    data = request.get_json()  # Obtener la expresión del frontend
    expression = data.get('expression', '')

    # Procesar la expresión con el lexer
    tokens = all_tokens(expression)

    # Devolver los tokens en formato JSON
    return jsonify(tokens)

if __name__ == '__main__':
    app.run(debug=True)