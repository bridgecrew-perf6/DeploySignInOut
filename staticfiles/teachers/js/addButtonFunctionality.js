let inputCounter = 0;
let OptionCounter = 1;

function addInput(){
    inputCounter++;
    const div = document.createElement("div")
    div.className = `inputContainer${inputCounter}`;
    console.log(`inputContainer${inputCounter}`);
    div.innerHTML = `<input type='text' name= input${inputCounter} placeholder=input${inputCounter} required/>`
    document.getElementById("inputsContainer").appendChild(div);
    OptionCounter = 0;
}

function addOptions(){
    OptionCounter++;
    const newDiv = document.createElement("div")
    newDiv.className = "Option"
    newDiv.innerHTML = `<input type='text' name= input${inputCounter}-Option${OptionCounter} placeholder=input${inputCounter}-Option${OptionCounter} required/>`
    console.log(`inputContainer${inputCounter}`);
    document.querySelector(`.inputContainer${inputCounter}`).appendChild(newDiv);
}
