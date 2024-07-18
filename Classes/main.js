const kramer = new Object();
kramer.name = "Dinz";
kramer.age = 27;
// console.log(kramer);

// Clase

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
// console.log(dinz.hi());

const sonia = new People("sonia", "alejandra");
// console.log(sonia.hi());

// Herencia

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
console.log(maria);
console.log(maria.hi());
