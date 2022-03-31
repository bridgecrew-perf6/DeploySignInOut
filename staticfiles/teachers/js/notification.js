const Show = (message=message, duration=duration, bg=bg) => {
    Toastify({
        text: message,
        className: "info",
        duration: duration,
        close: true,
        style: {
            background: bg,
            display: "flex",
            fontSize: "1.25rem",
            gap: "10px",
        }
    }).showToast();
}
try{
    let message = document.getElementById("message").innerHTML;
    Show(message=message, duration=3500, bg="#fdad5c")
}catch(error){
    let message = document.getElementById("DoNotAllowed").innerHTML;
    Show(message=message, duration=5000, bg="red")
}
finally{
    const check = document.getElementById("check").innerHTML;
    if(check === "[]"){
        Show(message="There are no submitions abailable for this period", duration= 10000, bg="red")
    }
}



