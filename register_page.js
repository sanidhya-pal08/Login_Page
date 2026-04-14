document.querySelector(".registerBtn").addEventListener("click",handleSubmit);

function handleSubmit(){
    console.log("clicked");
    const email = document.getElementById("emailInfo").value;
    const password = document.getElementById("pass").value;
    fetch("https://fast-api-login-app.onrender.com/users/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            password:password
        })
    })
    .then(response => response.json())
    .then(data => {
    if(data.detail){
        if(Array.isArray(data.detail)){
            alert(data.detail[0].msg)  // pydantic validation error
        } else {
            alert(data.detail)  // your own HTTPException error
        }
    }
    else{
        window.location.href="logged_in.html"
    }
    })
}