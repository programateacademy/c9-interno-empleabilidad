document.addEventListener("DOMContentLoaded", function() {
    let contador = 0;

    function incrementarContador(event) {
        event.preventDefault();

        contador++;
        console.log(contador);
        if (contador === 3) {
            mostrarModal();
            document.getElementById("Boton").disabled = true;
        }
    }

    function mostrarModal() {
        alert('El contador ha llegado a tres');
    }

    document.getElementById("Boton").addEventListener("click", incrementarContador);
});

