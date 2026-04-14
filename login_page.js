
document.querySelector(".submitInfo").addEventListener("click", handleSubmit);

function handleSubmit(){
    const email = document.getElementById("emailInfo").value;
    const password = document.getElementById("pass").value;
    fetch("https://fast-api-login-app.onrender.com/login/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if(data.detail){
            if(Array.isArray(data.detail)){
                alert(data.detail[0].msg)  //pydantic validation error
            } else {
                alert(data.detail)  //some other error
            }
        }
        else{
            window.location.href = "logged_in.html"
        }
    })
}
