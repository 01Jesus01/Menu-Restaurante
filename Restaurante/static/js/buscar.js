resultadoBusqueda.style.display = "none";

inputBusqueda.addEventListener('input', function () {
    const query = inputBusqueda.value.trim();
    if (query.length > 0) {
        fetch(`/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                mostrarResultados(data);
                // Mostrar el contenedor de resultados después de obtener los datos
                resultadoBusqueda.style.display = "block";
            });
    } else {
        // Si la búsqueda está vacía, ocultar el contenedor de resultados
        resultadoBusqueda.innerHTML = '';
        resultadoBusqueda.style.display = "none";
    }
});


function mostrarResultados(data) {
    resultadoBusqueda.innerHTML = '';
    const query = inputBusqueda.dataset.query; // Obtener el valor de query del elemento input
    if (data.length === 0) {
        resultadoBusqueda.innerHTML = '<p>No se encontraron resultados</p>';
    } else {
        data.forEach(platillo => {
            const elementoPlatillo = document.createElement('div');
            const enlacePlatillo = document.createElement('a');
            enlacePlatillo.textContent = `${platillo.Nombre}`;
            enlacePlatillo.dataset.query = query;
            enlacePlatillo.addEventListener('click', function() {
                // Obtener el valor de query del enlace al que se hizo clic
                const clickedQuery = this.dataset.query;
                window.location.href = `/Menu/busqueda/?q=${platillo.Nombre}`;
                console.log("Nombre del platillo:", platillo.Nombre);                 
            });
            elementoPlatillo.appendChild(enlacePlatillo);
            resultadoBusqueda.appendChild(elementoPlatillo);
        });
    }
}
