import './navbar.css'
import Logo from './Logo'
import BurguerMenu from './BurguerMenu'
import Links from './Links'


const Navbar = () => {
    return (
            <nav className="menu-container">
                <BurguerMenu />
                <Logo />
                <Links />
            </nav>
    );
}

export default Navbar;
