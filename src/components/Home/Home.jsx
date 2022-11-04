import { useState, useEffect } from "react"
import { Link } from "react-router-dom";
import {consultarBDD} from '../../assets/funciones.js'
const Home = () => {
     
    const [productos, setProductos] = useState([]);

    useEffect(() => {
        consultarBDD('./json/productos.json').then(productos => {
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
                        <button className="btn-comprar" ><Link className="btn-comprar" to={`/itemdetailcontainer/${prod.id}`}>Ver detalles</Link></button>
                    </div>  
                    </div>
                </div>
                </div>
                ) 
                setProductos(cardProductos)
        })
    },[])
    
    
    return (
        <>
        <h1>Pesas</h1>
            {productos}
        </>
    );
}

export default Home;
