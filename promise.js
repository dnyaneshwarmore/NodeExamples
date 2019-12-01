 mypromise = async()=>{
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{console.log ("waiting for 5 seconds")},5000);
        resolve("waited for 5 seconds");
    });
}

console.log("fuck the world");

mypromise()
// .then((result)=>{
//     console.log(result)
// })
// console.log("she is bitch");

function printString(string, callback){
    console.log(string)
    callback()
}

printString("A",()=>{
    printString("B", ()=>{
        printString("C", ()=>{})
    })
})
