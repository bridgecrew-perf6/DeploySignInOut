window.onload = function() {
    const previosSavedName = localStorage.getItem('Identifier');
    const previosSavedPeriod = localStorage.getItem('Period');
    if (previosSavedName!=null && previosSavedPeriod != null){
        $('input[name=checkNameOfSubmissioner').val(previosSavedName)
        $('input[name="recivedPeriod"').val(previosSavedPeriod)
    }
    if (previosSavedName==null && previosSavedPeriod!=null){
        $('input[name="recivedPeriod"').val(previosSavedPeriod)
    }
    if (previosSavedName!=null && previosSavedPeriod==null){
        $('input[name="recivedPeriod"').val(previosSavedPeriod)
    }
}