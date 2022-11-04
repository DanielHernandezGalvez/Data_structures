import cart from './cart.png'

const Links = () => {
    return (
        <>
             <div className="menu">
                    <ul>
                        <li>
                            <a href='/' className='menu-h1'>
                                
                            </a>
                        </li>
                    </ul>
                    <ul>
                        <li>
                            <a href="#home">
                                Mancuernas
                            </a>
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
                        <button className='btn-carrito '>
                                carrito
                                <img src={cart} width='20px' alt='carrito' />
                            </button>
                    </ul>
                </div>
        </>
    );
}

export default Links;
