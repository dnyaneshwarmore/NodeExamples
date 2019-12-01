function prototype(name){
    this.name = name;
    
}

person = new prototype("dmm");

//this will not work as greetings is not available
// console.log(person.greetings);

prototype.prototype.greetings = function() {
    console.log("yo bitch !!!!!!! I am ", this.name);
}

//this works fine
console.log(person.greetings())