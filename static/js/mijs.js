

$(Document).ready(function(){

    //var elems = document.querySelectorAll('.modal');
    //var  instances = M.Modal.init(elems,{dismissible: false});
    //$('#modal1').modal();

    $("#myTable").on('click', '.td-name', function() {
    // get the current row
    var currentRow = $(this).closest("tr");
    var nombre = currentRow.find(".td-name").html(); // get current row 1st table cell TD value
    //var col2 = currentRow.find(".pd-name").html(); // get current row 2nd table cell TD value
    var categoria = currentRow.find(".td-categoria").html();
    var resena = currentRow.find(".td-resena").html();
    var promulgacion = currentRow.find(".td-promulgacion").html();
    var file = currentRow.find(".td-file").html();

    $("#cabezara").text("Ordenanza")
    $("#nombre").text(nombre)
    $("#categoria").text("Categoría: " + categoria)
    $("#promulgacion").text("Fecha: " + promulgacion)
    $("#resena").text(resena)

    
    //para abrir el Modal de materialize luego de quecher alguna funcion
    var elem= document.querySelector('.modal');
    var instance = M.Modal.init(elem);
    instance.open();

    
    });
   


})


