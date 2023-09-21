document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('borrar').addEventListener('click', function() {
        Swal.fire({
            title: '¿Estás seguro de guardar los cambios?',
            icon: 'warning',
            showDenyButton: true,
            showCancelButton: true,
            confirmButtonText: 'Guardar',
            confirmButtonColor: '#1CA631',
            denyButtonText: 'No guardar',
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire('¡Cambios guardados!', '', 'success')
            } else if (result.isDenied) {
                Swal.fire('NO se guardaron los cambios', '', 'info')
            }
        })
    });

    document.getElementById('enviar').addEventListener('click', function() {
        Swal.fire({
            title: '¿Estás seguro de guardar los cambios?',
            icon: 'warning',
            showDenyButton: true,
            showCancelButton: true,
            confirmButtonText: 'Guardar',
            confirmButtonColor: '#1CA631',
            denyButtonText: 'No guardar',
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire('¡Cambios guardados!', '', 'success')
            } else if (result.isDenied) {
                Swal.fire('NO se guardaron los cambios', '', 'info')
            }
        })
    });
});