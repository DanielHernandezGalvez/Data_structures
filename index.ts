// to print the log use *tsc index.ts* then *node index.js*
// console.log("Hola mundo")

// 5! = 5 * 4 * 3 * 2 * 1

function factorial(n: number): number {
    if (n < 0 || !Number.isInteger(n)) {
      throw new Error("El número debe ser un entero no negativo.");
    }
    if (n === 0) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }

console.log(factorial(5));