import React from "react";
import Image from "next/image";
import logo from "./logo.png";

export default function Navbar() {
  return (
    <div>
      <header>
        <a href="#" className="logo">
          <Image src={logo} width={60} />
        </a>
        <div className="menutoggle" onclick="togglemenu();"></div>
        <ul className="navigation">
          <li>
            <a className="link4" href="#banner">
              Home
            </a>
          </li>
          <li>
            <a className="link4" href="#about">
              About
            </a>
          </li>
          <li>
            <a className="link4" href="#menu">
              Menu
            </a>
          </li>
          <li>
            <a className="link4" href="#expert">
              Expert
            </a>
          </li>
          <li>
            <a className="link4" href="#testimonials">
              Testimonials
            </a>
          </li>
          <li>
            <a className="link4" href="#contactus">
              Contact Us
            </a>
          </li>
        </ul>
      </header>
    </div>
  );
}
