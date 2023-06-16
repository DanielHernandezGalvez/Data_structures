import React from "react";
import Navbar from "../../../components/Navbar/Navbar";
import Footer from "../../../components/Footer";

export default function descargarexcel() {
  return (
    <>
      <Navbar />

      <div className="container-bg">
        <h1>
          Cómo exportar una tabla HTML a un archivo Excel utilizando la
          biblioteca XLSX
        </h1>

        <p>
          Paso 1: Instalar la biblioteca, debes instalar la biblioteca XLSX
          utilizando npm. Abre una terminal o línea de comandos y ejecuta el
          siguiente comando:{" "}
        </p>
        <div className="codigo">
          <p>
            npm i --save https://cdn.sheetjs.com/xlsx-0.19.3/xlsx-0.19.3.tgz
          </p>
        </div>
        <p>
          Paso 2: Importar la biblioteca XLSX En el archivo donde deseas
          utilizar la biblioteca XLSX, debes importarla. Puedes hacerlo de la
          siguiente manera:
        </p>
        <div className="codigo">
          <p>import XLSX from "xlsx"; </p>
        </div>
        <p>
          Paso 3: Definir la función para exportar la tabla Ahora, vamos a
          definir una función llamada handleExportToExcel, que se encargará de
          exportar la tabla HTML a un archivo Excel. Aquí tienes un ejemplo de
          cómo puedes hacerlo:
        </p>
        <div className="codigo">
          <p>
            {`const handleExportToExcel = () => {
              `}{" "}
            <br />
            <span className="verde">
              // Función para exportar la tabla como un archivo Excel
            </span>{" "}
            <br />
            {`const table = document.getElementById("my-table");
            `}{" "}
            <br />
            <span className="verde">
              // Se obtiene la referencia al elemento HTML que contiene la tabla
              que queremos exportar
            </span>
            <br />
            {` let workbook = XLSX.utils.table_to_book(table);
            `}
            <br />
            <span className="verde">
              // Se utiliza la biblioteca XLSX para convertir la tabla HTML a un
              libro de Excel
            </span>
            <br />
            <span className="verde">
              // Nota: La variable 'workbook' es un objeto de libro de Excel que
              contiene todas las hojas y celdas del libro.
            </span>
            <br />
            {`XLSX.writeFile(workbook, 'archivo.xlsx);`} <br />
            <span className="verde">
              // Se utiliza la función 'writeFile' de XLSX para descargar el
              archivo Excel con el nombre "archivo.xlsx"
            </span>
          </p>
        </div>
        <p>
          Paso 4: Llamar a la función de exportación. Por último, debes llamar a
          la función handleExportToExcel en el evento que desees, por ejemplo,
          al hacer clic en un botón. Aquí tienes un ejemplo de cómo puedes
          hacerlo:
        </p>
        <div className="codigo">
          <p>
            const exportButton = document.getElementById("export-button");{" "}
            <br />
            exportButton.addEventListener("click", handleExportToExcel);
          </p>
        </div>
      </div>
      <Footer />
    </>
  );
}
