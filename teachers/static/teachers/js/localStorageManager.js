const setSavedItems = () =>{
    const previosSavedName = localStorage.getItem('Identifier');
    if(previosSavedName !== null){
        document.getElementById('nameOfSubmissioner').value = previosSavedName;
    }

    const previosSavedPeriod = localStorage.getItem('Period')
    if(previosSavedPeriod !== null){
        document.getElementById('period').value = previosSavedPeriod;
    }


    const previosSavedGroupMembers = localStorage.getItem('groupMembers')
    if(previosSavedGroupMembers !== null){
        document.getElementById('groupMembers').value = previosSavedGroupMembers;
    }

}


const saveName = () =>{
    const previosSaved = localStorage.getItem('Identifier')
    if(previosSaved == null){
        const nameID = document.getElementById('nameOfSubmissioner').value
        localStorage.setItem('Identifier', nameID)
    }
    else{
        const nameID = document.getElementById('nameOfSubmissioner').value
        localStorage.removeItem('Identifier');
        localStorage.setItem('Identifier', nameID)    
    }
}

const savePeriod = () =>{
    const previosSaved = localStorage.getItem('Period')
    if(previosSaved == null){
        const nameID = document.getElementById('period').value
        localStorage.setItem('Period', nameID)
    }
    else{
        const nameID = document.getElementById('period').value
        localStorage.removeItem('Period');
        localStorage.setItem('Period', nameID)    
    }
}

const saveGroupMemebers = () =>{
    const previosSaved = localStorage.getItem('groupMembers')
    if(previosSaved == null){
        const nameID = document.getElementById('groupMembers').value
        localStorage.setItem('groupMembers', nameID)
    }
    else{
        const nameID = document.getElementById('groupMembers').value
        localStorage.removeItem('groupMembers');
        localStorage.setItem('groupMembers', nameID)    
    }
}