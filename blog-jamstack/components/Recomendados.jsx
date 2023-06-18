import React, { useState, useEffect } from "react";
import Link from "next/link";
import Image from "next/image";

export default function Recomendados() {
  const [data, setData] = useState([]);

  function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  }

  const getData = () => {
    try {
      const info = require("../data/data.json");
      const shuffledData = shuffleArray(info).slice(0, 6); // Mezcla y selecciona solo 3 objetos
      setData(shuffledData);
      console.log(data);
    } catch (error) {
      console.error("Error al obtener los datos:", error);
    }
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <>
      <div className="recomended-container">
        <div className="titulo-recomendados">
          {" "}
          <h2>Puede interesarte: </h2>
        </div>
        {data.map((dato) => (
          <div className="recomended" key={dato.id}>
            <Link href={dato.url}>
              <h3>{dato.title}</h3>
              <div className="image-container">
                <Image
                  src={dato.img}
                  width={150}
                  height={150}
                  className="rounded-image"
                />
              </div>
              {/* <p>Etiquetas: {dato.category}</p>
            <p>{dato.description}</p> */}
            </Link>
          </div>
        ))}
      </div>
    </>
  );
}
