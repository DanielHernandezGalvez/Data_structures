let array = [1, 2, "dinz", true];
let array2 = [4, 2, "kramer", false];

function showArray1(array) {
  //   console.log("--------------");
  for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
  }
}

// recorrer un array con for of es mejor y más sencillo
function showArray2(array) {
  //   console.log("--------------");
  for (let item of array) {
    // console.log(item);
  }
}

// showArray1(array);
// showArray2(array2)

// console.log(array[2]);

array.push(false);
showArray2(array);

// ***Programación funcional*** //

// funcion de primera clase

function hi() {
  console.log("hola");
}

const h = hi;

// hi()

// funcion de primera clase con parametros
function sum(a, b) {
  return a + b;
}

const s = sum;

// console.log(s(4,1));

// funciones de orden superior
function some(fn) {
  // console.log("se hace algo antes");

  fn();

  // console.log("se hace algo después");
}

// some(h)

// funcion de orden superior ejecuta funcion con parametros
function some2(fn, num1, num2) {
  console.log("se hace algo antes");

  const res = fn(num1, num2);

  console.log("el resultado es: ", res);
}

some2(s, 3, 5);

// funcion anonima
some2(
  function (a, b) {
    return a * b;
  },
  6,
  2
);

// la arrow function da azucar sintáctica
some2((a, b) => a * b, 10, 20);
