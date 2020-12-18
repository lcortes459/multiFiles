var clienteSegmentoMg, segmentoAsignacionMg, asignacionFileMg;
var clienteNombreMg, segmentoNombreMg, asignacionNombreMg,cargandoPreMg, resulMg,opcMg,archivoMg;
var empresa = 'falabella';
var mg = {
  ready: function() {
      
      this.start();
      
  },
  start: function() {},

  vamosMejorGestion: function () {
    
    $('#contenidoPrincipal').hide('slow/400/fast', function() {
      $('#contenidoClieSegAsigMejorGestion').show('slow/400/fast', function() {
        $('#idClientesMg').focus();
      });
    });
  },
  regresarPrincipal: function() {
    
    
    
    $('#contenidoClieSegAsigMejorGestion').hide('slow/400/fast', function() {
      $('#contenidoPrincipal').show();
    });
  
  },

  clienteSegmentoMg: function( idSelect) {

    clienteSegmentoMg = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedmg].value); 

    clienteNombreMg =  idSelect.options[idSelect.selectedmg].text;

    if ( parseInt(clienteSegmentoMg) > 0 ) {

      mg.consulatarSegmentos( parseInt(clienteSegmentoMg) );
    }else{

      $('#idSegmentosMg,#idAsignacionesMg').prop("disabled", true);  
    }
     
  },
  segmentoAsignacion: function( idSelect) {

    segmentoAsignacion = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedmg].value);  //crossbrowser solution =)

    segmentoNombre =  idSelect.options[idSelect.selectedmg].text;

    if ( parseInt(segmentoAsignacion) > 0 ) {

      mg.consulatarAsignacion( parseInt(segmentoAsignacion) );
    }else{

      $('#idSegmentosMg').prop("disabled", true);  
    }
     
  },
  asignacionFile: function( idSelect) {

    asignacionFile = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedmg].value);  //crossbrowser solution =)

    asignacionNombre =  idSelect.options[idSelect.selectedmg].text;


    if ( parseInt(asignacionFile) > 0 ) {

      $('#btnVamosMg').prop("disabled", false);
    }else{

      $('#btnVamosMg').prop("disabled", true);  
    }
     
  },

  consulatarSegmentos: function( idClient ) {
    
    $.ajax({
      url: 'segmentos',
      type: 'GET',
      dataType: 'json',
      data: {idCliente: idClient},
    })
    .done(function( data ) {
      $('#idSegmentosMg').prop("disabled", false);

      if ( data.length > 0 ) {
        var dataHtml = new Array();
        $('#idSegmentosMg').html('');
        var conteo = 0;
        $.each(data, function(mg, val) {

          if ( conteo === 0 ) {

            dataHtml.push(

              `

              <option value="0">Seleccione un segmento</option>
              <option value="`+val.idSegmento+`">`+val.nombreSegmento+`</option>


              `
            )

          }else{

            dataHtml.push(

              `

     
              <option value="`+val.idSegmento+`">`+val.nombreSegmento+`</option>


              `
            )
          }

          conteo = conteo + 1;    
        });

        $('#idSegmentosMg').html(dataHtml);
      }else {

        $('#idSegmentosMg').html('<option value="0">Este cliente no tiene segmentos</option>');
      }
    });
    
  },
  consulatarAsignacion: function( idSegment ) {
    
    $.ajax({
      url: 'asignacion',
      type: 'GET',
      dataType: 'json',
      data: {idSegmento: idSegment},
    })
    .done(function( data ) {
      $('#idAsignacionesMg').prop("disabled", false);
      $('#idAsignacionesMg').html('');
      var conteo = 0;
      var dataHtml = new Array();
      if ( data.length > 0 ) {
        $.each(data, function(mg, val) {

          if ( conteo === 0 ) {

            dataHtml.push(

              `
              <option value="0">Seleccione una asignacion</option>
              <option value="`+val.idAsignacion+`">`+val.nombreAsignacion+`</option>

              `
            )

          }else{

            dataHtml.push(

              `
              <option value="`+val.idAsignacion+`">`+val.nombreAsignacion+`</option>

              `
            )
          }

          conteo = conteo + 1;    
        });

        $('#idAsignacionesMg').html(dataHtml);
      }else {

        $('#idAsignacionesMg').html('<option value="0">Este segmento no tiene asignación</option>');
      }
    });
    
  },
};
mg.ready();