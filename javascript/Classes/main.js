const kramer = new Object();
kramer.name = "Dinz";
kramer.age = 27;

// ***Clase*** //

class People {
  constructor(name, lastname) {
    this.name = name;
    this.lastname = lastname;
  }

  hi() {
    return "hola soy " + this.name + " " + this.lastname;
  }
}

const dinz = new People("dinz", "kramer");

const sonia = new People("sonia", "alejandra");

// ***Herencia**** //

class Student extends People {
  constructor(name, lastname, carrer) {
    super(name, lastname);
    this.carrer = carrer;
  }

  // va a sobreescribir al del padre
  hi() {
    return super.hi() + " estudiante de " + this.carrer;
  }
}

// objeto hijo
const maria = new Student("maria", "becerra", "diseño");

// ***Referencias*** //

/* Valores primitivos
String, number,
biginit, boolean, 
undeguned y simbol*/

let number = 4

function edit(num, value) {
  num = value;
  console.log("El valor interno es: " + num)
}

edit(number, 10)
console.log("El valor interno es: " + number)

class A {
  constructor(number) {
    this.number = number;
  }
}

let a = new A(4)

function editObject(obj, value){
  obj.number = value;
  console.log("El valor interno es: " + obj.number)
}

editObject(a, 10)
console.log("el valor externo es: "+ a.number)
