import {useState} from 'react';

const ItemCount = () => {
    const [ItemCount, setContador] = useState(1);
    const modificarContador = (operacion) => {
        if(operacion ==='+'){
            if(ItemCount < 10) //producto.stock
           setContador(ItemCount + 1)
        } else {
            if(ItemCount > 1)
                setContador(ItemCount - 1)
        }
        
    }
    return (
        <div className='itemcount'>
          <button onClick={() =>modificarContador('+')} id='+' className='btn-contador'>+</button>
            <div className='count'>
            {ItemCount}
            </div>
          <button onClick={() =>modificarContador('-')} id='-' className='btn-contador'>-</button>  
  
        </div>
    );
}

export default ItemCount;
