import './Calculator.css'

export default function Calculator () {

  return(
    <div class="calculator">
      <div class="output">
        <span class="result"></span>
      </div>
      <div class="buttons">
        <button class="bg-main-dark">(</button>
        <button class="bg-main-dark">)</button>
        <button class="bg-pumpink">C</button>
        <button class="bg-musg-green">/</button>

        <button>7</button>
        <button>8</button>
        <button>9</button>
        <button class="bg-musg-green">*</button>

        <button>4</button>
        <button>5</button>
        <button>6</button>
        <button class="bg-musg-green">-</button>

        <button>1</button>
        <button>2</button>
        <button>3</button>
        <button class="bg-musg-green">+</button>

        <button>0</button>
        <button>.</button>
        <button class="bg-wine">=</button>
        <button class="btn-tree">
          <img src="/tree.svg" alt="Tree Icon" style={{ width: '24px', height: '24px' }} />
        </button>
      </div>
    </div>
  )

}