import React, { useState } from 'react';
import './Calculator.css';

export default function Calculator() {
  // Estado para almacenar la expresión matemática
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState('');
  const [showResult, setShowResult] = useState(false); // Nuevo estado para controlar la visibilidad

  // Manejar clics de botones (añadir a la expresión)
  const handleButtonClick = (value) => {
    if (showResult) {
      // Si ya se mostró el resultado, reiniciar expresión y ocultar resultado
      setExpression(value);
      setShowResult(false);
    } else {
      setExpression((prev) => prev + value);
    }
  };

  // Función para evaluar la expresión cuando se presiona el botón "="
  const handleEqualClick = () => {
    try {
      const evalResult = eval(expression);
      setResult(evalResult);
      setShowResult(true); // Mostrar solo el resultado
    } catch (error) {
      setResult('Error');
      setShowResult(true);
    }
  };

  // Función para limpiar la calculadora (cuando se presiona "C")
  const handleClear = () => {
    setExpression('');
    setResult('');
    setShowResult(false); // Restablecer para mostrar la expresión
  };

  return (
    <div className="calculator">
      <div className="output">
        {/* Mostrar la expresión solo si no se ha presionado el botón "=" */}
        <span className="expression">{!showResult ? (expression || '0') : ''}</span>
        <span className="result">{showResult ? result : ''}</span>
      </div>
      <div className="buttons">
        <button className="bg-main-dark" onClick={() => handleButtonClick('(')}>(</button>
        <button className="bg-main-dark" onClick={() => handleButtonClick(')')}>)</button>
        <button className="bg-pumpink" onClick={handleClear}>C</button>
        <button className="bg-musg-green" onClick={() => handleButtonClick('/')}>/</button>

        <button onClick={() => handleButtonClick('7')}>7</button>
        <button onClick={() => handleButtonClick('8')}>8</button>
        <button onClick={() => handleButtonClick('9')}>9</button>
        <button className="bg-musg-green" onClick={() => handleButtonClick('*')}>*</button>

        <button onClick={() => handleButtonClick('4')}>4</button>
        <button onClick={() => handleButtonClick('5')}>5</button>
        <button onClick={() => handleButtonClick('6')}>6</button>
        <button className="bg-musg-green" onClick={() => handleButtonClick('-')}>-</button>

        <button onClick={() => handleButtonClick('1')}>1</button>
        <button onClick={() => handleButtonClick('2')}>2</button>
        <button onClick={() => handleButtonClick('3')}>3</button>
        <button className="bg-musg-green" onClick={() => handleButtonClick('+')}>+</button>

        <button onClick={() => handleButtonClick('0')}>0</button>
        <button onClick={() => handleButtonClick('.')}>.</button>
        <button className="bg-wine" onClick={handleEqualClick}>=</button>
        <button className="btn-tree">
          <img src="/tree.svg" alt="Tree Icon" style={{ width: '24px', height: '24px' }} />
        </button>
      </div>
    </div>
  );
}
