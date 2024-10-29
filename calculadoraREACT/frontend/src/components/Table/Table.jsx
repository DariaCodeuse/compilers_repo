import './Table.css'

export default function Table () {

return(
  <div class="card">
    <div class="card_title">Resultados del análisis</div>
    <div class="card_data">
      <div class="card_right">
        <div class="item">id</div>
        <div class="item">name</div>
        <div class="item">date</div>
        <div class="item">active</div>
      </div>
      <div class="card_left">
        <div class="item">int</div>
        <div class="item">varchar</div>
        <div class="item">datetime</div>
        <div class="item">boolean</div>
      </div>
    </div>
  </div>
)

}