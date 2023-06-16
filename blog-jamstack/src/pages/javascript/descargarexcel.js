import React from "react";
import Navbar from "../../../components/Navbar/Navbar";

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
          <code>
            npm i --save https://cdn.sheetjs.com/xlsx-0.19.3/xlsx-0.19.3.tgz
          </code>
        </div>
        <p>
          Paso 2: Importar la biblioteca XLSX En el archivo donde deseas
          utilizar la biblioteca XLSX, debes importarla. Puedes hacerlo de la
          siguiente manera:
        </p>
        <div className="codigo">
          <code>import XLSX from "xlsx"; </code>
        </div>
        <p>
          Paso 3: Definir la función para exportar la tabla Ahora, vamos a
          definir una función llamada handleExportToExcel, que se encargará de
          exportar la tabla HTML a un archivo Excel. Aquí tienes un ejemplo de
          cómo puedes hacerlo:
        </p>
        <div className="codigo">
          <code>
            {`const handleExportToExcel = () => {\n 
                `}
          </code>
          <code>
            // Función para exportar la tabla como un archivo Excel\n const
            table = document.getElementById("my-table");\n // Se obtiene la
            referencia al elemento HTML que contiene la tabla que queremos
            exportar let workbook = XLSX.utils.table_to_book(table); // Se
            utiliza la biblioteca XLSX para convertir la tabla HTML a un libro
            de Excel // Nota: La variable 'workbook' es un objeto de libro de
            Excel que contiene todas las hojas y celdas del libro.
            XLSX.writeFile(workbook, 'archivo.xlsx); // Se utiliza la función
            'writeFile' de XLSX para descargar el archivo Excel con el nombre
            "archivo.xlsx"
          </code>
        </div>
      </div>
    </>
  );
}
