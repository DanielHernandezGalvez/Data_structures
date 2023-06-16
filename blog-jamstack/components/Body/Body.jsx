import React, { useEffect, useState } from "react";
import Image from "next/image";
import Link from "next/link";

export default function Body() {
  const [data, setData] = useState([]);

  const getData = () => {
    try {
      const info = require("../../data/data.json");
      setData(info);
    } catch (error) {
      console.error("Error al obtener los datos:", error);
    }
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <div className="card-container">
      {data.map((dato) => (
        <>
          <div className="card" key={dato.id}>
            <Link href="/javascript/descargarexcel">
              <h3>{dato.title}</h3>
              <div className="image-container">
                <Image
                  src={dato.img}
                  width={150}
                  height={150}
                  className="rounded-image"
                />
              </div>
              <p>Etiquetas: {dato.category}</p>
              <p>{dato.description}</p>
            </Link>
          </div>
        </>
      ))}
    </div>
  );
}
