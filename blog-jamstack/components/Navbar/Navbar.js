import { useEffect, useState } from "react";
import Image from "next/image";
import logo from "./logo.png";
import { FaLinkedin, FaGithub, FaGlobe } from "react-icons/fa";
import Categorias from "../Categorias";

export default function Navbar() {
  const [windowWidth, setWindowWidth] = useState(0);

  useEffect(() => {
    const handleResize = () => {
      setWindowWidth(window.innerWidth);
    };

    handleResize();

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  const getIconSize = () => {
    if (windowWidth < 450) {
      return 20; // Tamaño pequeño para pantallas más pequeñas
    } else {
      return 30; // Tamaño grande para pantallas más grandes
    }
  };
  return (
    <div>
      <header>
        <a href="#" className="logo">
          <Image src={logo} width={150} />
        </a>
        <div className="menutoggle" onclick="togglemenu();"></div>
        <ul className="navigation">
          <li>
            <a className="link4" href="#about">
              <FaLinkedin size={getIconSize()} />
            </a>
          </li>
          <li>
            <a className="link4" href="#menu">
              <FaGithub size={getIconSize()} />
            </a>
          </li>
          <li>
            <a className="link4" href="#contactus">
              <FaGlobe size={getIconSize()} />
            </a>
          </li>
        </ul>
      </header>
      <Categorias />
    </div>
  );
}
