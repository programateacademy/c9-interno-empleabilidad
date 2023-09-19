document.querySelectorAll('.switch-toggle input').forEach(function(element) {
    element.addEventListener('change', function() {
        document.getElementById('console-event').innerHTML = 'Estado: ' + this.nextSibling.innerHTML;
    });
});
