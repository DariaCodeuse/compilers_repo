import React, { useState } from 'react';

function Table() {
  const [tokens, setTokens] = useState([]);  // Estado para guardar los tokens
  const [expression, setExpression] = useState('');  // Estado para la expresión del usuario

  // Función para enviar la expresión al backend
  const fetchTokens = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/lex', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression }),  // Enviar la expresión
      });

      const data = await response.json();
      setTokens(data);  // Guardar los tokens recibidos
    } catch (error) {
      console.error('Error fetching tokens:', error);
    }
  };

  // Manejar el envío del formulario
  const handleSubmit = (e) => {
    e.preventDefault();
    fetchTokens();
  };

  return (
    <div>
      {/* Formulario para ingresar la expresión */}
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={expression} 
          onChange={(e) => setExpression(e.target.value)} 
          placeholder="Escribe tu expresión"
        />
        <button type="submit">Enviar</button>
      </form>

      {/* Mostrar los tokens en una tabla */}
      {tokens.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Token</th>
              <th>Descripción</th>
            </tr>
          </thead>
          <tbody>
            {tokens.map((token, index) => (
              <tr key={index}>
                <td>{token[0]}</td>  {/* Valor del token */}
                <td>{token[1]}</td>  {/* Descripción del token */}
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default Table;
