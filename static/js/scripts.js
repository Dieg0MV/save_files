let miCanvas = document.querySelector('#myCanvas');
let lineas = [];
let pintarLinea = false;
// Marca el nuevo punto
let nuevaPosicionX = 0;
let nuevaPosicionY = 0;

miCanvas.width = 400;
miCanvas.height = 400;


/*
Me gustaria declarar mi amor 
pero solo puedo declarar variables
*/

//======================================================================
// FUNCIONES
//======================================================================

/**
 * Función que empieza a dibujar la línea
 */
function empezarDibujo(event) {
    event.preventDefault();
    pintarLinea = true;
    lineas.push([]);
    actualizarPosicion(event);
    guardarLinea();
}

/**
  Función que guarda la posición de la nueva línea
 */
function guardarLinea() {
    lineas[lineas.length - 1].push({
        x: nuevaPosicionX,
        y: nuevaPosicionY
    });
}

/*
  Función que dibuja la línea
 */
function dibujarLinea(event) {
    event.preventDefault();
    if (pintarLinea) {
        let ctx = miCanvas.getContext('2d');
        // Estilos de línea
        ctx.lineJoin = ctx.lineCap = 'round';
        ctx.lineWidth = 10;
        // Color de la línea
        ctx.strokeStyle = '#000';
        // Marca el nuevo punto
        actualizarPosicion(event);
        // Guarda la línea
        guardarLinea();
        // Redibuja todas las líneas guardadas
        ctx.beginPath();
        lineas.forEach(function (segmento) {
            ctx.moveTo(segmento[0].x, segmento[0].y);
            segmento.forEach(function (punto) {
                ctx.lineTo(punto.x, punto.y);
            });
        });
        ctx.stroke();
    }
}

/**
 * Función que deja de dibujar la línea
 */
function pararDibujar(event) {
    event.preventDefault();
    pintarLinea = false;
    guardarLinea();
}

/**
 * Función que actualiza la posición del nuevo punto
 */
function actualizarPosicion(event) {
    let rect = miCanvas.getBoundingClientRect();
    if (event.changedTouches == undefined) {
        // Versión ratón
        nuevaPosicionX = event.clientX - rect.left;
        nuevaPosicionY = event.clientY - rect.top;
    } else {
        // Versión touch, pantalla táctil
        nuevaPosicionX = event.changedTouches[0].clientX - rect.left;
        nuevaPosicionY = event.changedTouches[0].clientY - rect.top;
    }
}

//======================================================================
// EVENTOS
//======================================================================

// Eventos ratón
miCanvas.addEventListener('mousedown', empezarDibujo, false);
miCanvas.addEventListener('mousemove', dibujarLinea, false);
miCanvas.addEventListener('mouseup', pararDibujar, false);
miCanvas.addEventListener('mouseout', pararDibujar, false);

// Eventos pantallas táctiles
miCanvas.addEventListener('touchstart', empezarDibujo, false);
miCanvas.addEventListener('touchmove', dibujarLinea, false);
miCanvas.addEventListener('touchend', pararDibujar, false);
miCanvas.addEventListener('touchcancel', pararDibujar, false);


