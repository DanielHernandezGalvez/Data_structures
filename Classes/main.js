const kramer = new Object();
kramer.name = "Dinz";
kramer.age = 27;
console.log(kramer);

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
console.log(dinz.hi());

const sonia = new People("sonia", "alejandra")
console.log(sonia.hi());
