import { Link } from 'react-router-dom';
import cart from './cart.png'

const Links = () => {
    return (
        <>
             <div className="menu">
                    <ul>
                        <li>
                            <Link href='/' className='menu-h1'>
                                
                            </Link>
                        </li>
                    </ul>
                    <ul>
                        <li>
                            <Link to='/producto'>
                                Mancuernas
                            </Link>
                        </li>
                        <li>
                            <a href="#categorias">
                                Discos
                            </a>
                        </li>
                        <li>
                            <a href="#contacto">
                                Accesorios
                            </a>
                        </li>
                        <Link to='/carrito'>
                        <button className='btn-carrito '>
                                carrito
                                <img src={cart} width='20px' alt='carrito' />
                            </button>
                        </Link>
                        
                    </ul>
                </div>
        </>
    );
}

export default Links;
