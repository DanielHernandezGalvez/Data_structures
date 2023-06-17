import React from "react";
import Navbar from "../../../components/Navbar/Navbar";
import Footer from "../../../components/Footer";
import Recomendados from "../../../components/Recomendados";

export default function descargarpdf() {
  return (
    <>
      <Navbar />

      <div className="container-bg">
        <h1>
          Descargar documentos PDF usando JavaScript con las bibliotecas jsPDF y
          html2canvas
        </h1>

        <p>
          Paso 1: Instala las bibliotecas necesarias. Abre tu terminal y ejecuta
          el siguiente comando:
        </p>
        <div className="codigo">
          <p>npm install jspdf html2canvas</p>
        </div>
        <p>Paso 2: Importa las bibliotecas en tu archivo JavaScript:</p>
        <div className="codigo">
          <p>
            import jsPDF from 'jspdf'; <br />
            import html2canvas from 'html2canvas';{" "}
          </p>
        </div>
        <p>Paso 3: Crea una función para manejar la exportación a PDF:</p>
        <div className="codigo">
          <p>
            {`const handleExportToPDF = () => {
              `}{" "}
            <br />
            <span className="verde">
              // Función para exportar la tabla como un archivo PDF
            </span>{" "}
            <br />
            {`const input = document.getElementById("my-table");
            `}{" "}
            <br />
            <span className="verde">
              // Se obtiene la referencia al elemento HTML que contiene la tabla
              que queremos exportar
            </span>
            <br />
            {`   html2canvas(input).then((canvas) => {

            `}
            <br />
            <span className="verde">
              // Se utiliza la biblioteca html2canvas para crear un objeto
              canvas a partir de la tabla HTML
            </span>
            <br />
            {`const imgData = canvas.toDataURL("image/png");`} <br />
            <span className="verde">
              // Se obtiene la URL de la imagen en formato PNG que representa el
              contenido de la tabla
            </span>{" "}
            <br />
            {` const imgWidth = 210; `}
            <span className="verde">
              // Ancho de la imagen en milímetros
            </span>{" "}
            <br />
            {`const imgHeight = (canvas.height * imgWidth) / canvas.width; `}
            <span className="verde">
              // Se calcula la altura de la imagen en base al ancho y
              proporciones de la tabla
            </span>{" "}
            <br />
            {`const pdf = new jsPDF("p", "mm", "a4"); `}
            <span className="verde">
              // Se crea un nuevo objeto jsPDF para generar el archivo PDF{" "}
            </span>{" "}
            {` pdf.addImage(imgData, "PNG", 0, 0, imgWidth, imgHeight); `}
            <span className="verde">
              // Se agrega la imagen en formato PNG al documento PDF{" "}
            </span>{" "}
            <br />
            {`  pdf.save("table.pdf"); `} <br />
            <span className="verde">
              // Se descarga el documento PDF con el nombre "table.pdf"{" "}
            </span>{" "}
            <br />
            {`   }); `} <br />
            {`}; `}
          </p>
        </div>
        <p>
          Paso 4: Asegúrate de tener un elemento HTML con el id "my-table" que
          contenga la tabla que deseas exportar. Por ejemplo:
        </p>
        <div className="codigo">
          <p>
            {`  <table id="my-table"> `} <br />
          </p>
        </div>
        <p>
          Paso 5: Llama a la función handleExportToPDF cuando desees realizar la
          exportación a PDF, por ejemplo, en respuesta a un evento de clic en un
          botón:
        </p>
        <div className="codigo">
          <p>
            {`<button onclick="handleExportToPDF()">Exportar a PDF</button> `}{" "}
            <br />
          </p>
        </div>
        <p>
          Espero que te sea útil, que tengas un código sin errores y que la
          suerte siempre esté de tu lado.
        </p>
      </div>
      <Recomendados />
      <Footer />
    </>
  );
}
