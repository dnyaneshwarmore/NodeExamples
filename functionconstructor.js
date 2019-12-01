function Person(name){
    this.name = name;
    this.greetings = function(){
        console.log("Hiii My name is ", this.name);
    }
}

console.log(new Person("dnyaneshwar"));