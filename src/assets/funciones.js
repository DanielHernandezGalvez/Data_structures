export const consultarBDD = async () =>{
    const promise = await fetch('./json/productos.json')
    const productos = await promise.json()
  
        const cardProductos = productos.map(prod => 
            
            <div className="container" key={prod.id}>
            <div className="card">
                <div className="card-inner">
                <div className="front-face">
                    <img src={`./img/${prod.img}`} alt="..." />
                    <h2>{prod.title}</h2>
                </div>
                <div className="back-face">
                    <h2>{prod.title}</h2>
                    <p><b>$ {prod.precio}</b></p>
                    <a className="btn-comprar">Ver detalles</a>
                </div>  
                </div>
            </div>
            </div>
            ) 
           return cardProductos
  }
