document.getElementById('borrar').addEventListener('click', function() {
    Swal.fire({
        title : 'Aprobar cambios',
        text : '¿Estas seguro que quieres hacer los cambios?',
        confirmButtonColor: '#1CA631',
        icon: 'warning',
        confirmButtonText: 'Guardar cambios',
        showCancelButton: true,
        cancelButtonText: 'Cerrar',
        cancelButtonColor: '#F0313C'
    });
});

document.getElementById('enviar').addEventListener('click', function() {
    Swal.fire({
        title : 'Aprobar cambios',
        text : '¿Estas seguro que quieres hacer los cambios?',
        confirmButtonColor: '#1CA631',
        icon: 'warning',
        confirmButtonText: 'Guardar cambios',
        showCancelButton: true,
        cancelButtonText: 'Cerrar',
        cancelButtonColor: '#F0313C'
    });
});