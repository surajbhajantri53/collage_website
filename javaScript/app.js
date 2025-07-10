class Calculator {
  constructor(a, b) {
    this.a = a;
    this.b = b;
  }

  add() {
    return this.a + this.b;
  }

  sub() {
    return this.a - this.b;
  }

  multi() {
    return this.a * this.b;
  }

  divide() {
    return this.b !== 0 ? this.a / this.b : "Cannot divide by zero";
  }
}

// Creating an object (instance) of Calculator class with values 10 and 5
const calc = new Calculator(10, 5);

// Calling methods without passing parameters again
console.log("Addition:", calc.add());
console.log("Subtraction:", calc.sub());
console.log("Multiplication:", calc.multi());
console.log("Division:", calc.divide());