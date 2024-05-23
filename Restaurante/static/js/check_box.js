document.addEventListener('DOMContentLoaded', (event) => {
    // Obtener todas las casillas de verificación con el atributo data-mesa-id
    const checkboxes = document.querySelectorAll('input[type="checkbox"][data-mesa-id]');

    // Iterar sobre las casillas de verificación
    checkboxes.forEach(checkbox => {
        // Obtener el ID de la mesa asociado a la casilla de verificación
        const mesaId = checkbox.getAttribute('data-mesa-id');

        // Cargar el estado de "entregado" desde Local Storage
        const entregado = localStorage.getItem(`entregado_${mesaId}`);

        // Log para verificar los valores recuperados
        console.log(`Mesa ID: ${mesaId}, Entregado en Local Storage: ${entregado}`);

        // Si se encuentra un estado guardado, actualizar la casilla de verificación
        if (entregado !== null) {
            checkbox.checked = (entregado === 'true');
        }

        // Escuchar el evento change en la casilla de verificación
        checkbox.addEventListener('change', function() {
            // Guardar el estado de "entregado" en Local Storage como una cadena 'true' o 'false'
            localStorage.setItem(`entregado_${mesaId}`, this.checked.toString());
            // Log para verificar los valores guardados
            console.log(`Mesa ID: ${mesaId}, Estado guardado: ${this.checked.toString()}`);
        });
    });
});
