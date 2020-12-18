var clienteSegmento, segmentoAsignacion, asignacionFile;
var clienteNombre, segmentoNombre, asignacionNombre, idEmpreClieSegAsig, clienteSegmentoAsignacion, segmentoAsignacionNew, estadoCargue,cargandoPre, resul,opc,idArchivoDescarga;
var archivo = 1;
var empresa = 'falabella';
var conteMacro =`
  <div class="card h-100" style="border-color:#000;b_order-radius:15px;">
  <div class="card-header" style="background-color:#f7f7f7;color: #000;" id="headerFilesMacro">
  Cargue de archivos.
  </div>
  <br>
  <div class="card-boby container-fluid">
  <div class="row">
  <div class="col-md-4 col-sm-12">
  <div id="drag-and-drop-zoneMacro" class="dm-uploader p-5">

  <div class="btn btn-primary btn-block mb-5">
  <span>Click para subir resultado de <b>MACRO</b></span>
  <input type="file" title='Click to add Files'/>
  <input type="hidden" id="destino" value="Macro">
  </div>
  </div>
  </div>
  <div class="col-md-8 col-sm-12">
  <div class="card h-100" style="border-color:#5d9269;">
  <div class="card-header" style="background-color:#b8daff;">
  Listado de archivos (Recuerda que las extensiones permitidas son: <b>CSV | XLSX | TXT | XLS  </b>)
  </div>
  <div class="card-boby">
  <ul class="list-unstyled p-2 d-flex flex-column col" id="files">
  <li class="text-muted text-center empty">No files uploaded.</li>
  </ul>
  </div>
  </div>
  </div>
  </div>
  </div>
  <br>
  <div class="card-footer container-fluid">
  <div class="form-group row">
  <div class="col-md-2">
  <button  class="btn btn-primary btn-block" onclick="index.regresarCliSegSig();">
  <i class="fa fa-chevron-left"></i>  Regresar
  </button>
  </div>
  <div class="col-md-8"></div>
  <div class="col-md-2">
  <button  class="btn btn-primary btn-block rigth" onclick="index.siguiente();">Siguiente
  <i class="fa fa-chevron-right"></i>
  </button>
  </div>
  </div>
  </div>
  </div>
`;
var index = {
  ready: function() {
      //Swal.fire('Algo pasa');
      this.start();
      
  },
  start: function() {
    //index.selecEjecucion();
    $('#idClientes').focus();
    $('#btncrearAsignacion').click(function(event) {
    

      var nombreAsignacionCreada = $('#nombreAsignacion').val();
      var fechaCierreAsignacionCreada = $('#cierreAsignacion').val();  

      if ( (clienteSegmento) && (segmentoAsignacion) && (nombreAsignacionCreada) && (fechaCierreAsignacionCreada) ) {


        $.ajax({
          url: 'asignacionNew',
          type: 'GET',
          dataType: 'json',
          data: {
            clienteSegmento             : clienteSegmento,
            segmentoAsignacion          : segmentoAsignacion, 
            nombreAsignacionCreada      : nombreAsignacionCreada,
            fechaCierreAsignacionCreada : fechaCierreAsignacionCreada
          },
        })
        .done(function( data ) {

          if ( parseInt(data) > 0 ) {
            
            Swal.fire({
              title: 'Felicidades',
              text: 'Asignación creada con éxito.',
              type: 'error',
              showCancelButton: false,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'Continuar',
              allowOutsideClick:false,
              allowEscapeKey:false,
              allowEnterKey:false
            }).then((result) => {
              if (result.value) {
                asignacionFile = result.value;
                asignacionNombre = nombreAsignacionCreada;
                index.selecEjecucionNewAsig();
              }
            });
          } else if ( parseInt(data) === 0 ) {

            Swal.fire('Información','La asig: '+nombreAsignacionCreada+' ya existe para ese segmanto.','info');

          } else {
            
            Swal.fire('Error','Algo salio mal, Intenta nuevamente.','error');
            
          }
        });

      } else {
        
        Swal.fire({
          title: 'Error',
          text: 'Formulario incompleto......',
          type: 'error',
          showCancelButton: false,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Verificar',
          allowOutsideClick:false,
          allowEscapeKey:false,
          allowEnterKey:false
        }).then((result) => {
          if (result.value) {
            Swal.close();
            $('#nombreAsignacion,#cierreAsignacion').prop("disabled", false);  
          }
        });
      }
    });


  },
  masOpciones: function() {
    
   $("#exampleModalCenter").modal({
      keyboard: false,
      //backdrop: false
    });
  },
  clienteSegmentoAsignacion: function( idSelect) {

    clienteSegmentoAsignacion = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedIndex].value);  //crossbrowser solution =)

    

    if ( parseInt(clienteSegmentoAsignacion) > 0 ) {

      index.consulatarSegmentosAsignacion( parseInt(clienteSegmentoAsignacion) );
    }else{

      $('#idSegmentos,#idAsignaciones').prop("disabled", true);  
    }
     
  },
  segmentoAsignacionNew: function( idSelect) {

    segmentoAsignacionNew = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedIndex].value);  //crossbrowser solution =)

    segmentoNombre =  idSelect.options[idSelect.selectedIndex].text;

    if ( parseInt(segmentoAsignacionNew) > 0 ) {

      $('#nombreAsignacion').focus();
    }else{

      $('#idAsignaciones').prop("disabled", true);  
    }
     
  },
  consulatarSegmentosAsignacion: function( idClient ) {
    
    $.ajax({
      url: 'segmentos',
      type: 'GET',
      dataType: 'json',
      data: {idCliente: idClient},
    })
    .done(function( data ) {
      $('#idSegmentosAsignacion').prop("disabled", false);

      if ( data.length > 0 ) {
        var dataHtml = new Array();
        $('#idSegmentosAsignacion').html('');
        var conteo = 0;
        $.each(data, function(index, val) {

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

        $('#idSegmentosAsignacion').html(dataHtml);
      }else {

        $('#idSegmentosAsignacion').html('<option value="0">Este cliente no tiene segmentos</option>');
      }
      //$('#idSegmentos').attr({display: false});
      //index.limpiarSlect(idSegmentos);
    });
    
  },
  clienteSegmento: function( idSelect) {

    clienteSegmento = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedIndex].value);  //crossbrowser solution =)

    clienteNombre =  idSelect.options[idSelect.selectedIndex].text;

    if ( parseInt(clienteSegmento) > 0 ) {

      index.consulatarSegmentos( parseInt(clienteSegmento) );
    }else{

      $('#idSegmentos,#idAsignaciones').prop("disabled", true);  
    }
     
  },
  segmentoAsignacion: function( idSelect) {

    segmentoAsignacion = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedIndex].value);  //crossbrowser solution =)

    segmentoNombre =  idSelect.options[idSelect.selectedIndex].text;

    if ( parseInt(segmentoAsignacion) > 0 ) {

      index.consulatarAsignacion( parseInt(segmentoAsignacion) );
    }else{

      $('#idAsignaciones').prop("disabled", true);  
    }
     
  },
  asignacionFile: function( idSelect) {

    asignacionFile = (idSelect.vidSelectlue || idSelect.options[idSelect.selectedIndex].value);  //crossbrowser solution =)

    asignacionNombre =  idSelect.options[idSelect.selectedIndex].text;


    if ( parseInt(asignacionFile) > 0 ) {

      //index.consulatarAsignacion( parseInt(segmentoAsignacion) );


      console.log('******************');
      console.log('clienteNombre', clienteNombre);

      console.log('segmentoAsignacion', segmentoAsignacion);
      console.log('*******************');
      console.log('segmentoNombre', segmentoNombre);

      console.log('asignacionFile', asignacionFile);
      console.log('*******************');
      console.log('asignacionNombre', asignacionNombre);

      // if ( archivo === 1 ) {
      //   $('#btnVamosMg').prop("disabled", false);
      // }else{
      //   $('#btnVamos').prop("disabled", false);
      // }
      $('#btnVamos').prop("disabled", false);
    }else{

      // if ( archivo === 1 ) {
      //   $('#btnVamosMg').prop("disabled", false);
      // }else{
      //   $('#btnVamos').prop("disabled", false);
      // }
      $('#btnVamos').prop("disabled", false);
      
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
      $('#idSegmentos').prop("disabled", false);

      if ( data.length > 0 ) {
        var dataHtml = new Array();
        $('#idSegmentos').html('');
        var conteo = 0;
        $.each(data, function(index, val) {

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

        $('#idSegmentos').html(dataHtml);
      }else {

        $('#idSegmentos').html('<option value="0">Este cliente no tiene segmentos</option>');
      }
      //$('#idSegmentos').attr({display: false});
      //index.limpiarSlect(idSegmentos);
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
      $('#idAsignaciones').prop("disabled", false);
      $('#idAsignaciones').html('');
      var conteo = 0;
      var dataHtml = new Array();
      if ( data.length > 0 ) {
        $.each(data, function(index, val) {

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

        $('#idAsignaciones').html(dataHtml);
      }else {

        $('#idAsignaciones').html('<option value="0">Este segmento no tiene asignación</option>');
      }
      //$('#idSegmentos').attr({display: false});
      //index.limpiarSlect(idSegmentos);
    });
    
  },
  vamos: function( opcMg ) {

    estadoCargue    = $('input:radio[name=radioAsiganacion]:checked').val();

    console.log('opcMg', opcMg);
    if ( (clienteSegmento) && (segmentoAsignacion) && (asignacionFile) && ( estadoCargue)) {

      if (parseInt(opcMg) === 1) {

        $('#SelClienSegAsig,#contenidoNewAsig').hide('slow/400/fast', function() {
          $('#contenidoFilesMacBi').show('slow/400/fast', function() {
            // $('#macroExcel').html('');
            // $('#headerFilesMacBi').html('');
            // $('#headerFilesMacBi').html('<b>Cargue de archivo: ' +clienteNombre+' | '+segmentoNombre+' | '+asignacionNombre+'<b>');
            
            // $.ajax({
            //   url: 'insertEmpCliSegAsig',
            //   type: 'POST',
            //   dataType: 'json',
            //   data: {

            //     idEmpresa    : 1,
            //     empresa      : empresa,
            //     idCliente    : clienteSegmento,
            //     cliente      : clienteNombre,
            //     idSegmento   : segmentoAsignacion,
            //     segmento     : segmentoNombre, 
            //     idAsignacion : asignacionFile,
            //     asignacion   : asignacionNombre,
            //     estadoCargue : estadoCargue 

            //   }
            // })
            // .done(function( resul ) {
            //   idEmpreClieSegAsig = resul;
            //   $('#idClienSegAsi').val(idEmpreClieSegAsig);
            // });
            
          });
        });
      }else{


       $('#SelClienSegAsig,#contenidoNewAsig').hide('slow/400/fast', function() {
        $('#contenidoFilesMacro').show('slow/400/fast', function() {
          //$('#contenidoFilesVarios').html('');
          $('#headerFilesMacro').html('');
          $('#headerFilesMacro').html('<b>Cargue de archivo: ' +clienteNombre+' | '+segmentoNombre+' | '+asignacionNombre+'<b>');
          
          $.ajax({
            url: 'insertEmpCliSegAsig',
            type: 'POST',
            dataType: 'json',
            data: {

              idEmpresa    : 1,
              empresa      : empresa,
              idCliente    : clienteSegmento,
              cliente      : clienteNombre,
              idSegmento   : segmentoAsignacion,
              segmento     : segmentoNombre, 
              idAsignacion : asignacionFile,
              asignacion   : asignacionNombre,
              estadoCargue : estadoCargue 

            }
          })
          .done(function( resul ) {
            idEmpreClieSegAsig = resul;
            $('#idClienSegAsi').val(idEmpreClieSegAsig);
          });
          
        });
      });

      }
    }
  },
  siguiente: function () {
    
    $('#contenidoFilesMacro').hide('slow/400/fast', function() {
      $('#contenidoFilesVarios').show('slow/400/fast', function() {
        $('#contenidoFilesMacro').html('');
        $('#headerFilesVarios').html('');
        $('#headerFilesVarios').html('<b>Cargue de archivo: ' +clienteNombre+' | '+segmentoNombre+' | '+asignacionNombre+'<b>');
      });
    });
  },
  vamosMejorGestion: function () {
    
    $('#contenidoPrincipal').hide('slow/400/fast', function() {
      $('#contenidoClieSegAsigMejorGestion').show('slow/400/fast', function() {
        $('#idClientes').focus();
      });
    });
  },
  regresarPrincipal: function() {
    
    
    
    $('#contenidoClieSegAsigMejorGestion').hide('slow/400/fast', function() {
      $('#contenidoPrincipal').show();
    });
  
  },
  regresarCliSegSig: function() {
    
    $('#contenidoFilesMacro,#contenidoFilesMacBi').hide('slow/400/fast', function() {
      $('#SelClienSegAsig').show( 'slow/400/fast', function() {
        index.selecEjecucion();
      });
    });
  
  },
  regresarMacro: function() {
    
    $('#contenidoFilesVarios').hide('slow/400/fast', function() {
      $('#contenidoFilesMacro').show( function() {
         $('#contenidoFilesMacro').html(conteMacro); 
      });
    });
  
  },
  nuevaAsignacion :function() {
    
    $('#SelClienSegAsig').hide('slow/400/fast', function() {
      $('#contenidoNewAsig').show( 'slow/400/fast', function() {
        
        $('#idClientesAsignacion').val(clienteSegmento);
        $('#idClientesAsignacionMostrar').val(clienteNombre);
        $('#idSegmentosAsignacion').val(segmentoAsignacion);
        $('#idSegmentosAsignacionMostrar').val(segmentoNombre);
        $('#idClientesAsignacion,#idSegmentosAsignacion').prop("disabled", true);  
        $('#nombreAsignacion').focus();
      });
    });
  },
  regresarCliSegSigNewAsigna :function(selector) {
    
    $('#contenidoNewAsig').hide('slow/400/fast', function() {
      $('#SelClienSegAsig').show();
    });
  },
  inicioPrecesos: function() {

    archivo = 0;    

    Swal.fire({
      title: 'Comfirmación.',
      text: "¿Confirma que desea iniciar el proceso.?",
      icon: 'info',
      showCancelButton: true,
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'SI',
      cancelButtonText: 'No',
      focusConfirm: false,
      allowOutsideClick: false,
      allowEscapeKey: false,
      showCloseButton: false,
      allowEnterKey:false
    }).then((result) => {

      console.log('estadoCargue', estadoCargue);
      if (result.isConfirmed) {
        if (parseInt(estadoCargue) === 1) {
          
          index.macro();

        } else {
          //index.macro();
          //  Proceso de update campanas y dashbard  | php /var/www/avi_falabella/index.php execute_dash
          cargandoPre = index.creacionCuerpoPreloads('Proceso detención campañas 1/4   --- ID asignación '+asignacionFile+'');
          index.preloads(cargandoPre);
          $.ajax({
            url: 'iniciarProcesos',
            type: 'GET',
            dataType: 'json',
            data: index.creacionData('updateCampanas')
          })
          .done(function( dat ) {
            
            console.log('datUpdate',dat[0]);

            if (dat.length > 0) {
                
              if ( dat[0].indicador === 1 ) {
                index.gestion360();
              } else {
                
                Swal.fire('Error');
              }  

            }else {
              
              Swal.fire('Error');
            }
               
          });
          // Fin proceso de update campanas y dashbard
        }
      }
    });
  },
  mejorGestionMg: function() {

    archivo = 1;

    cargandoPre = index.creacionCuerpoPreloads('Proceso detención campañas 1/4 --- ID asignación '+asignacionFile+'');    
    index.preloads(cargandoPre);
    
    $.ajax({
      url: 'iniciarProcesos',
      type: 'GET',
      dataType: 'json',
      data: index.creacionData('updateCampanas')
    })
    .done(function( dat ) {
      
      console.log('datUpdate',dat[0]);

      if (dat.length > 0) {
          
        if ( dat[0].indicador === 1 ) {
          index.gestion360();
        } else {
          
          Swal.fire('Error');
        }  

      }else {
        
        Swal.fire('Error');
      }
         
    });
    // index.mejorGestion();
  },
  gestion360: function() {
    //   php /var/www/avi_falabella/index.php reporte360 index 0
    cargandoPre = index.creacionCuerpoPreloads('Proceso gestión 360 2/4 --- ID asignación '+asignacionFile+'');
    index.preloads(cargandoPre);
    $.ajax({
      url: 'iniciarProcesos',
      type: 'GET',
      dataType: 'json',
      data: index.creacionData('gestion360')
    })
    .done(function( dat ) {
      console.log('datMesjorGestión',dat[0]);

      if (dat.length > 0) {
            
        if ( dat[0].indicador === 1 ) {
          index.mejorGestion();
          //index.macro();
        } else {
          
          Swal.fire('Error');
        }  

      }else {
        
        Swal.fire('Error');
      }
    });
  },
  mejorGestion: function() {
    //  /var/www/reports/best_management_360/reportsBestManagedTodayMonth.py '+new Date()+' falabella '+clienteSegmento+' '+segmentoAsignacion+' 16
    cargandoPre = index.creacionCuerpoPreloads('Proceso mejor gestión 3/4 --- ID asignación '+asignacionFile+'');
    index.preloads(cargandoPre);
    $.ajax({
      url: 'iniciarProcesos',
      type: 'GET',
      dataType: 'json',
      data: index.creacionData('mejorGestion')
    })
    .done(function( dat ) {
      console.log('datMesjorGestión',dat[0]);

      if (dat.length > 0) {
            
        if ( dat[0].indicador === 1 ) {

          idArchivoDescarga = dat[0].idResultado
          
          if ( archivo == 1 ) {


            index.decargaArchivos();
            
          }else{
            index.macro();
          }
        } else {
          
          Swal.fire('Error');
        }  

      }else {
        
        Swal.fire('Error');
      }
    });
  },
  decargaArchivos: function() {
    cargandoPre = index.creacionCuerpoPreloads('Descarga de archivo mejor gestión 4/4 --- ID asignación '+asignacionFile+'');
    index.preloads(cargandoPre);
    $.ajax({
      url: 'iniciarProcesos',
      type: 'GET',
      dataType: 'json',
      data: index.creacionData('descargarArchivos')
    })
    .done(function( dat ) {

      if (dat.length > 0) {
            
        if ( dat[0].indicador === 1 ) {

          window.location.href='http://34.75.120.5/InteliBpoFilesII/static/archivosDescargas/'+dat[0].idResultado+' ';
          index.confirmaciones('Felicidades','<b>Lo lograstes</b>','');

          Swal.fire({
            position: 'top-end',  
            html: '<b>Lo lograstes <br> Archivo descargado con éxito</b>',
            icon: "success",   
            showCloseButton: false,
            showCancelButton: false,
            showConfirmButton: false,
            confirmButtonText: "Continuar",  
            focusConfirm: false,
            allowOutsideClick: false,
            allowEscapeKey: false,
            showCloseButton: false,
            allowEnterKey:false,
            timer: 2500
          });

          setTimeout(function(){ window.location.href='' }, 2505);

        } else {
          
          Swal.fire('Error');
        }  

      }else {
        
        Swal.fire('Error');
      }
    });
    // const swalWithBootstrapButtons = Swal.mixin({
    //     customClass: {
    //       confirmButton: 'btn btn-success',
    //       cancelButton: 'btn btn-danger'
    //     },
    //     buttonsStyling: false
    //   });

    //   swalWithBootstrapButtons.fire({
    //     title: 'Lo has logrado',
    //     text: "¿Que deseas hacer ahora?",
    //     icon: 'success',
    //     showCancelButton: true,
    //     confirmButtonText: 'Descargar MG',
    //     cancelButtonText: 'Ir a campañas',
    //     reverseButtons: true,
    //     focusConfirm: false,
    //     allowOutsideClick: false,
    //     allowEscapeKey: false,
    //     showCloseButton: false,
    //     allowEnterKey:false
    //   }).then((result) => {
    //       if (result.isConfirmed) {
    //         cargandoPre = index.creacionCuerpoPreloads('Descargando mejor gestión 4/4');
    //       } else if (
    //         result.dismiss === Swal.DismissReason.cancel
    //       ) {
    //         window.location.href='http://falabella.intelibpo.com/index.php/campanas';
    //       }
    //   });
  },
  macro: function() {
    
    //console.log('dataMacro', data);  python3 /opt/intelbpo/automaticos/avi_falabella/macro/src/main.py  '+data+' 
    cargandoPre = index.creacionCuerpoPreloads('Proceso macro 4/4 --- ID asignación '+asignacionFile+'');
    index.preloads(cargandoPre);
    $.ajax({
      url: 'iniciarProcesos',
      type: 'GET',
      dataType: 'json',
      data: index.creacionData('macro')
    })
    .done(function( dat ) {
      console.log('datMesjorMacro',dat[0]);

      if (dat.length > 0) {
            
        if ( dat[0].indicador === 1 ) {
          //index.confirmaciones('Felicidades','<b>Lo lograstes</b>','');

          const swalWithBootstrapButtons = Swal.mixin({
            customClass: {
              confirmButton: 'btn btn-success',
              cancelButton: 'btn btn-danger'
            },
            buttonsStyling: false
          });

          swalWithBootstrapButtons.fire({
            title: 'Lo has logrado',
            text: "¿Que deseas hacer ahora?",
            icon: 'success',
            showCancelButton: true,
            confirmButtonText: 'Ir a campañas',
            cancelButtonText: 'Cargues',
            reverseButtons: true,
            focusConfirm: false,
            allowOutsideClick: false,
            allowEscapeKey: false,
            showCloseButton: false,
            allowEnterKey:false
          }).then((result) => {
              if (result.isConfirmed) {
                window.location.href='http://falabella.intelibpo.com/index.php/campanas';
              } else if (
                result.dismiss === Swal.DismissReason.cancel
              ) {
                window.location.href='http://34.75.120.5/InteliBpoFiles/default/misCargues';
              }
          });
          
        } else {
          
          Swal.fire('Error');
        }  

      }else {
        
        Swal.fire('Error');
      }
    });
  },
  creacionCuerpoPreloads: function( part ){

    cargandoPrelads = `
      <div class="card-body" id="spinerDiv">
        <p align="center" style="font-size:0.9em;">Estamos ejecutando...<br>`+part+`.</p><hr>
        <i class="fa fa-spinner fa-spin fa-3x"  style="color:#00c600"></i>
      </<div> 
    `;

    return cargandoPrelads;

  },
  creacionData: function ( op){
    

    data = {

      clienteSegmento           : clienteSegmento,
      segmentoAsignacion        : segmentoAsignacion,
      asignacionFile            : asignacionFile,
      clienteNombre             : clienteNombre,
      segmentoNombre            : segmentoNombre,
      asignacionNombre          : asignacionNombre,
      idEmpreClieSegAsig        : idEmpreClieSegAsig,
      clienteSegmentoAsignacion : clienteSegmentoAsignacion,
      segmentoAsignacionNew     : segmentoAsignacionNew,
      estadoCargue              : estadoCargue,
      opc                       : op,
      archivo                   : archivo,
      idArchivoDescarga         : idArchivoDescarga

    };

    return data;
  },
  ejecusiones: function ( ruta, metodo, dataTy, datos, result ) {

    $.ajax({
      url: ruta,
      type: metodo,
      dataType: dataTy,
      data: datos
    })
    .done(function( dat ) {

      if ( data.indicador === result ) {
        
        resultado = data;

      } else {
        
        resultado = 'error'
      }
      
    });
  },
  preloads: function( html ) {

    Swal.close();

    Swal.fire({
      html: html,
      showCloseButton: false,
      showCancelButton: false,
      showConfirmButton: false,
      focusConfirm: true,
      allowOutsideClick: false,
      allowEscapeKey: false,
      showCloseButton: false,
      allowEnterKey:false
    });
  },
  confirmaciones: function( title, html, opc ) {


    Swal.fire({
      position: 'top-end',  
      html: html,
      icon: "success",   
      showCloseButton: false,
      showCancelButton: false,
      showConfirmButton: false,
      confirmButtonText: "Continuar",  
      focusConfirm: false,
      allowOutsideClick: false,
      allowEscapeKey: false,
      showCloseButton: false,
      allowEnterKey:false,
      timer: 1000
    });
  },
  limpiar: function( idForm ) {
    
    $('#'+idForm+'')[0].reset();
    $('#idSegmentos,#idAsignaciones').prop("disabled", true);
    $('#idClientes').focus();
  },
  procesos: function( proceso, nombreProceso, hide, show ) {

    archivo = 0;

    if (proceso === 1 ) {

      $('#contenidoClieSegAsig').html('');
    }else{

      $('#macroProcesada').html('');  
      
    }
    $('#'+hide+'').hide('slow/400/fast', function() {
       
       $('#'+show+'').show('slow/400/fast', function() {
           $('#contenidoClieSegAsigMejorGestion').html('');
           $('#idClientes').focus();

       }); 

    });

  },
  inicio: function ( opcInicio ) {
    
    if (opcInicio === 1) {

      window.location.href='http://falabella.intelibpo.com/index.php/campanas';

    }else{

      window.location.href='';
    }
  },
  creacionCampanas:function() {
    // cargandoPre = index.creacionCuerpoPreloads('Proceso creación de campañas 5/5');
    // index.preloads(cargandoPre);

    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: false
    });
    swalWithBootstrapButtons.fire({
      title: 'Felicidades.',
      text: "Lo has logrado.",
      icon: 'success',
      showCancelButton: true,
      showConfirmButton: false,
      confirmButtonText: 'Finalizar',
      cancelButtonText: 'Finalizar',
      reverseButtons: true,
      focusConfirm: false,
      allowOutsideClick: false,
      allowEscapeKey: false,
      showCloseButton: false,
      allowEnterKey:false
    }).then((result) => {
        if (result.isConfirmed) {
          window.location.href='http://falabella.intelibpo.com/index.php/campanas';
        } else if (
          result.dismiss === Swal.DismissReason.cancel
        ) {
          window.location.href='';
        }
    });
  },
  selecEjecucion: function() {
    var html = `
      <hr>
      <div class="container-fluid">
        <div class="row">
            <div class="form-group col-md-12">
              <button class="btn btn-block botonPer" onclick="index.proceso(1);">Mejor gestión &nbsp;&nbsp;<i style="color:green;" class="fa fa-thumbs-up"></i></button>
            </div>
            <div class="form-group col-md-12">
              <button class="btn btn-block botonPer" onclick="index.proceso(2);">Macro en excel &nbsp;&nbsp;<i style="color:green;" class="fa fa-file-excel-o"></i></button>
            </div>
            <div class="form-group col-md-12">
              <button class="btn btn-block botonPer" onclick="index.proceso(3);">Macro automatica &nbsp;&nbsp; <i style="color:green;" class="fa fa-cogs"></i></button>
            </div>
          </div>  
      </div>  
    `;
    Swal.fire({
      title:'¿Que deseas hacer?',
      html: html,
      showCloseButton: false,
      showCancelButton: false,
      showConfirmButton: false,
      focusConfirm: true,
      allowOutsideClick: false,
      allowEscapeKey: false,
      showCloseButton: true,
      allowEnterKey:false
    });

  },
  selecEjecucionNewAsig: function() {
    var html = `
      <hr>
      <div class="container-fluid">
        <div class="row">
            <div class="form-group col-md-12">
              <button class="btn btn-block botonPer" onclick="index.proceso(2);">Macro en excel &nbsp;&nbsp;<i style="color:green;" class="fa fa-file-excel-o"></i></button>
            </div>
            <div class="form-group col-md-12">
              <button class="btn btn-block botonPer" onclick="index.proceso(3);">Macro automatica &nbsp;&nbsp; <i style="color:green;" class="fa fa-cogs"></i></button>
            </div>
          </div>  
      </div>  
    `;
    Swal.fire({
      title:'¿Que deseas hacer?',
      html: html,
      showCloseButton: false,
      showCancelButton: false,
      showConfirmButton: false,
      focusConfirm: true,
      allowOutsideClick: false,
      allowEscapeKey: false,
      showCloseButton: true,
      allowEnterKey:false
    });

  },
  proceso: function( ejecucion ) {
    
    var texto;
    if ( parseInt(ejecucion) === 1 ) {
      var tmp = 'Tu ID asignación es:  <b>'+asignacionFile+'</b>';
      texto = 'Mejor gestión';
      Swal.fire({
        title: 'Recuerda el siguiente dato.',
        html: tmp,
        icon: 'info',
        showCancelButton: true,
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Continuar >>',
        cancelButtonText: 'Regresar',
        focusConfirm: false,
        allowOutsideClick: false,
        allowEscapeKey: false,
        showCloseButton: false,
        allowEnterKey:false
      }).then((result) => {
        if (result.isConfirmed) {
          index.mejorGestionMg();
        }else{
          index.selecEjecucion();
        }
      });

    } else if ( parseInt(ejecucion) === 2 ) {
      Swal.close();
      // texto = 'Macro en excel';
      index.vamos(2);

    }else{
      Swal.close();
      // texto = 'Macro automatica';
      index.vamos(1);
    }

  },
};
index.ready();