// JavaScript
document.querySelectorAll('.mostrar-valor').forEach(function(element) {
    element.addEventListener('change', function() {
        document.getElementById('console-event').innerHTML = 'Estado: ' + this.nextSibling.innerHTML;
    });
});
