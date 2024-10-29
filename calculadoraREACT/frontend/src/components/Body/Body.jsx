import Calculator from '../Calculator/Calculator';
import Table from '../Table/Table';
import './Body.css'

export default function Body () {

  return(
    <div className="body">
      <div className='box-body'>
        <Calculator/>
        <Table/>
      </div>
      
    </div>
  )

}