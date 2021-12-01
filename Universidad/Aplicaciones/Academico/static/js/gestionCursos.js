(function () {
    
    const btnElimicacion = document.querySelectorAll(".btnEliminacion");

    btnElimicacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });

})();



