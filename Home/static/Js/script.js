document.addEventListener("DOMContentLoaded", function() {
    let contador = 0;

    function incrementarContador(event) {
        // Prevenir la acción predeterminada del botón
        event.preventDefault();

        contador++;
        console.log(contador);
        if (contador === 3) {
            mostrarModal();
            // Esto desactiva el boton a llegar a 3
            document.getElementById("Boton").disabled = true;
        }
    }

    function mostrarModal() {
        // Aquí puedes poner el código para mostrar tu modal
        alert('El contador ha llegado a tres');
    }

    document.getElementById("Boton").addEventListener("click", incrementarContador);
});

