import cart from './cart.png'

const Links = () => {
    return (
        <>
             <div className="menu">
                    <ul>
                        <li>
                            <a className='menu-h1'>
                                Pesas
                            </a>
                        </li>
                    </ul>
                    <ul>
                        <li>
                            <a href="#home">
                                home
                            </a>
                        </li>
                        <li>
                            <a href="#categorias">
                                categorías
                            </a>
                        </li>
                        <li>
                            <a href="#contacto">
                                contacto
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
