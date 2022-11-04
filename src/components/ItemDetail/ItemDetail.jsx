import './itemdetails.css'

const ItemDetail = ({producto}) => {
    return (
        <div className='contenedorDetails'>
              <div className='cuadrado'>    
                 <img src={`../img/${producto.img}`} alt='...'/>
             </div>
            <div  className='cuadrado'>
                <h2>${producto.title}</h2>
                    <p>Categoría:<b> ${producto.category}</b></p>
                    <p>precio:<b> ${producto.precio} </b></p>
                    <button className='boton'>Comprar</button>
                </div>
        </div>
    );
}

export default ItemDetail;
