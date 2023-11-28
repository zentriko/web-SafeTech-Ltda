
const user = document.getElementById("usuario")
const pass = document.getElementById("contrasena")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")
const check = document.getElementById("miCheckbox");


function showError(input ) {
    input.classList.add("invalid-input");
    swal("Existen campos con formato incorrecto",
    " ",
    "warning",
    );

    // Aquí puedes mostrar el mensaje de error de alguna manera, como usar parrafo.innerHTML
}

// Función para quitar la clase 'invalid-input' y eliminar el mensaje de error
function clearError(input) {
    input.classList.remove("invalid-input");
    // Puedes borrar el mensaje de error aquí
}

form.addEventListener("submit", e=>{
    console.log("entro al form")
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexUser = /^[A-Za-zñÑ\d]+$/;
    

    parrafo.innerHTML = ""
    //verificaciones formatos

    if (user.value.length < 3 || !regexUser.test(user.value)) {
        entrar = true;
        showError(user, "Nombre no válido");
    } else {
        clearError(user);
    }

    if (!check.checked) {
        entrar = true;
    }

    if (pass.value.length < 8) {
        entrar = true;
        showError(pass, "Contraseña no válida");
    } else {
        clearError(pass);


    }
    

    if (!entrar) {
        swal({
        
            title: "Inicio de sesión exitoso!",
            text: "Datos correctos",
            icon: "success",
            timer: 1300, // Duración en milisegundos
            buttons: false, // Oculta el botón "OK"
        }).then(() => {
            // Redirigir a la página deseada después de cerrar el SweetAlert
            form.submit();
        });
        // Aquí puedes agregar código para enviar el formulario al servidor, por ejemplo:
     
    }

})


