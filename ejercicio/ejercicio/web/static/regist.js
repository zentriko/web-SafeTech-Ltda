document.addEventListener("DOMContentLoaded", function () {
    const nombre = document.getElementById("id_nombre");
    const apellido = document.getElementById("id_apellido");
    const email = document.getElementById("id_correo");
    const pass = document.getElementById("id_contrasena");
    const passw = document.getElementById("rpass");
    const form = document.getElementById("form");
    const parrafo = document.getElementById("warnings");
    const check = document.getElementById("miCheckbox");

    function showError(input, message) {
        input.classList.add("invalid-input");
        swal("Existen campos con formato incorrecto", message, "warning");
        // Aquí puedes mostrar el mensaje de error de alguna manera, como usar parrafo.innerHTML
    }

    // Función para quitar la clase 'invalid-input' y eliminar el mensaje de error
    function clearError(input) {
        input.classList.remove("invalid-input");
        // Puedes borrar el mensaje de error aquí
    }

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        let entrar = false;
        let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        let regexNombre = /^[A-Za-zñÑ]+$/;
        let regexApellido = /^[A-Za-zñÑ]+$/;

    
        parrafo.innerHTML = "";
        //verificaciones formatos
        if (nombre.value.length < 3 || !regexNombre.test(nombre.value)) {
            entrar = true;
            showError(nombre, "Nombre no válido");
        } else {
            clearError(nombre);
        }
    
        if (apellido.value.length < 3 || !regexApellido.test(apellido.value)) {
            entrar = true;
            showError(apellido, "Apellido no válido");
        } else {
            clearError(apellido);
            
        }

        if (apellido.value.trim() === "" || !regexApellido.test(apellido.value)) {
            entrar = true;
            showError(apellido, "Apellido no válido");
        } else {
            clearError(apellido);
        }
    
        if (!regexEmail.test(email.value)) {
            entrar = true;
            showError(email, "Email no válido");
        } else {
            clearError(email);
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
    
        if (passw.value !== pass.value) {
            entrar = true;
            showError(passw, "Las contraseñas no coinciden");
        } else {
            clearError(passw);
        }
    
        // Si todas las validaciones son exitosas, enviar el formulario al servidor
        if (!entrar) {
            swal({
                title: "Registro exitoso",
                text: "¡Tu registro ha sido completado con éxito!",
                icon: "success",
                timer: 1500, // Duración en milisegundos
                buttons: false, // Oculta el botón "OK"
            }).then(() => {
                // Redirigir a la página deseada después de cerrar el SweetAlert
                form.submit(); // Esto enviará el formulario al servidor
            });
            // Aquí puedes agregar código para enviar el formulario al servidor, por ejemplo:
         
        }
    });
    
});
