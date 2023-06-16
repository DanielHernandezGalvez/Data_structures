import React, { useState } from "react";
import Link from "next/link";

const Categorias = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="navbar">
      <div className={`nav-items ${isOpen && "open"}`}>
        <Link className="link4" href="/">
          Home
        </Link>
        <Link className="link4" href="/skills">
          Python
        </Link>
        <Link className="link4" href="/proyectos">
          Javascript
        </Link>
        <Link className="link4" href="/las">
          PHP
        </Link>
        <Link className="link4" href="/las">
          React
        </Link>
        <Link className="link4" href="/las">
          Next
        </Link>
      </div>

      <div
        className={`nav-toggle ${isOpen && "open"}`}
        onClick={() => setIsOpen(!isOpen)}
      >
        <span></span>
        <span></span>
        <span></span>
      </div>
    </nav>
  );
};

export default Categorias;
