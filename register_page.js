document.querySelector(".registerBtn").addEventListener("click",handleSubmit);

function handleSubmit(){
    const email = document.getElementById("emailInfo").value;
    const password = document.getElementById("pass").value;
    console.log(email, password);
    alert("your account is successfully created go back to login page and log into your account");
}