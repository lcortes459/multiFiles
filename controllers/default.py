
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
# def index():???Soporte*2017***
# redirect(URL('guardin','default','index'))
# response.flash = T("Hello World")
# return dict(message=T('Welcome to web2py!'))
# [16:56, 3/11/2020] Camilillo Leuro: path yazmin ---> /var/www/avi_{empresa}/automatico/code/entradas/asignaciones/{año}/{mes}/nuevas
# [16:57, 3/11/2020] Camilillo Leuro: path sftpserver ---> /home/sftpserver/

from sqlalchemy import create_engine
import gluon.contrib.simplejson
from datetime import datetime, time, date
import math,sys,os,re,subprocess
import os.path, json


engine2 = create_engine(
    "mysql+pymysql://{user}:{pw}@localhost/{db}"
    .format(
        user="root",
        pw="j7t05fLcn0",
        db="avi_falabella"
    )
)

def asignacionNew():

    valores = request.vars
    countTableTmp = 0
    hoy = date.today().strftime("%Y-%m-%d")
    print('valores', valores)

    sqlVerificacion = """

        SELECT 
            COUNT(*)
        FROM 
            asignacion 
        WHERE 
            nombre='"""+str(valores.nombreAsignacionCreada).replace(' ','_')+"""'
        AND
            id_segmento = """+str(valores.segmentoAsignacion)+"""


    """
    print('sqlVerificacion', sqlVerificacion)
    with engine2.connect() as connection:
        countTable = connection.execute(sqlVerificacion)

    for x in countTable:
        countTableTmp = x[0]
        pass

    print('countTableTmp', countTableTmp)
    if countTableTmp == 0:

        sqlInsert = """

            INSERT INTO avi_falabella.asignacion
            (nombre,fecha_apertura,fecha_cierre,id_segmento,codigo,estado)
            VALUES('"""+str(valores.nombreAsignacionCreada).replace(' ','_')+"""',"""+str(hoy).replace('-','')+""","""+str(valores.fechaCierreAsignacionCreada).replace('-','')+""","""+str(valores.segmentoAsignacion)+""",1,'A');

        """
        print('sqlInsert', sqlInsert)
        with engine2.connect() as connection:
            countTable = connection.execute(sqlInsert)
            tmp = connection.execute(""" SELECT last_insert_id() """)

        for x in tmp:
            print('xxxxxx', x)
            if x[0]:
                resul = x[0]
            else:
                resul = 0
                pass
            pass
    else:
        resul = 0
        pass
    print('resul', resul)
    return resul

def meses( numeroMes ):

    mesNumero = int(numeroMes)


    if mesNumero == 1:

        mes = 'enero'

    elif mesNumero == 2:

        mes = 'febrero'

    elif mesNumero == 3:

        mes = 'marzo'

    elif mesNumero == 4:

        mes = 'abril'

    elif mesNumero == 5:

        mes = 'mayo'

    elif mesNumero == 6:

        mes = 'junio'

    elif mesNumero == 7:

        mes = 'julio'

    elif mesNumero == 8:

        mes = 'agosto'

    elif mesNumero == 9:

        mes = 'septiembre'

    elif mesNumero == 10:

        mes = 'octubre'

    elif mesNumero == 11:

        mes = 'noviembre'

    else:

        mes = 'diciembre'
        pass
    return mes

def get_download_url(upload_file):
    folder = "uploads"
    fullfilename = db.upload.upload_file.retrieve(
        upload_file, nameonly=True)[1]
    filename = fullfilename[fullfilename.find(folder) + len(folder) + 1:]
    filename = filename.replace("\\", "/")

    return URL("download", args=filename)

def index():
   
    empresa = request.vars
    print('empresa', empresa)

    sqlClientes = """

        SELECT 
            * 
        FROM 
            avi_falabella.Clientes
        WHERE 
            estado = 1 

    """
    with engine2.connect() as connection:
        countTable = connection.execute(sqlClientes)

    for x in countTable:
        countTable = x[0]
    pass

    if countTable>0:
        clientes = []
        for y in engine2.execute(sqlClientes):
            nombre       = y['nombre']
            descripcion  = y['descripcion']
            estado       = y['estado']
            clientes.append(y)
            pass
    else:
        print('Igual a cero')
        pass
    return locals()

def misCargues():
   
    misCargues = db().select( db.upload.ALL )
    
    return locals()

def segmentos():

    idCliente = request.vars.idCliente
    data = []

    

    sqlSegmentos = """
        SELECT
            *
        FROM
            avi_falabella.Segmentos
        WHERE
            id_cliente = """+str(int(idCliente))+"""

    """
    
    with engine2.connect() as connection:
        countTable = connection.execute(sqlSegmentos)

    if countTable>0:
        

        for y in engine2.execute(sqlSegmentos):
            

            data.append(
                dict(
                    idSegmento      = y[0],
                    nombreSegmento  = y[1],
                    estadoSegmento  = y[2],
                    id_cliente      = y[3]
                )
            )
            pass
    else:
        print('Igual a cero')
        pass

    
    
    return gluon.contrib.simplejson.dumps(data)

def asignacion():

    idSegmento = request.vars.idSegmento
    data = []

    

    sqlAsignacion = """
        SELECT
            *
        FROM
            avi_falabella.asignacion
        WHERE
            id_segmento = """+str(int(idSegmento))+"""
        AND
            estado = 'A'

    """
    
    with engine2.connect() as connection:
        countTable = connection.execute(sqlAsignacion)

    if countTable>0:
        

        for y in engine2.execute(sqlAsignacion):
            

            data.append(
                dict(
                    idAsignacion      = y[0],
                    nombreAsignacion  = y[1],
                    idSegmento        = y[4],
                    estadoAsignacion  = y[6]
                )
            )
            pass
    else:
        print('Igual a cero')
        pass

    
    
    return gluon.contrib.simplejson.dumps(data)

def insertEmpCliSegAsig():
    variables = request.vars

    print('variables',variables)
    
    db( db.tmpEmpClieSegAsignacion.id > 0).delete()

    inse = db.tmpEmpClieSegAsignacion.insert(\
        empresa       = variables.empresa,
        idAsignacion  = variables.idAsignacion,
        asignacion    = variables.asignacion,
        idEmpresa     = variables.idEmpresa,
        idSegmento    = variables.idSegmento,
        segmento      = variables.segmento,
        idCliente     = variables.idCliente,
        cliente       = variables.cliente,
        estadoCargue  = variables.estadoCargue
    )

    return int(inse)

def upload_fileMacro():

    #print('variables', request.vars)
    hoy = date.today().strftime("%Y-%m-%d")
    anio = str(hoy)[:4]
    mes  = meses(str(hoy)[5:7])
    empresa = 'falabella'
    original  = str(request.post_vars.file.filename).replace(' ','_').replace('-','_').replace('(','').replace(')','')
    if request.env.request_method != "POST":
        raise HTTP(404)
    upload_file = db.upload.upload_file.store(
        request.post_vars.file,
        filename=request.post_vars.file.filename
    )
    
    datosEmClSeAsi  = db.tmpEmpClieSegAsignacion 
    
    selInfoTmp = db( ).select( datosEmClSeAsi.ALL ).first()

    nombre_archivo, extension = os.path.splitext(upload_file)
    
    #print('Comprobar idAsignacionMacro', selInfoTmp.estadoCargue)

    tmp = db.upload.insert(
        upload_file    = upload_file,
        empresa        = selInfoTmp.empresa,
        idAsignacion   = selInfoTmp.idAsignacion,
        asignacion     = selInfoTmp.asignacion,
        idEmpresa      = selInfoTmp.idEmpresa,
        idSegmento     = selInfoTmp.idSegmento,
        segmento       = selInfoTmp.segmento,
        idCliente      = selInfoTmp.idCliente,
        cliente        = selInfoTmp.cliente,
        nombreOriginal = original,
        idTablaTmp     = selInfoTmp.id,
        estadoCargue   = selInfoTmp.estadoCargue,
        destinoCargue  = 'Macro'

    )   

    archivo = original


    db( db.upload.id == tmp ).update( nombrefilescarpeta = archivo )

    #print('empresa', empresa)

    if os.path.exists('/var/www/avi_'+str(empresa)+'/automatico/code/entradas/asignaciones/'+str(anio)+''):

        
        if os.path.exists('/var/www/avi_'+str(empresa)+'/automatico/code/entradas/asignaciones/'+str(anio)+'/'+str(mes)+''):
            

                
            if os.path.exists('/var/www/avi_'+str(empresa)+'/automatico/code/entradas/asignaciones/'+str(anio)+'/'+str(mes)+'/nuevas'):

                print(1)
                subprocess.call(

                    """
                        sudo chmod -R 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas
                    """,
                    shell=True
                )
                print(2)
                subprocess.call(
                    """
                        sudo chmod 777 /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+"""
                    """,
                    shell=True
                )
                print(3)
                subprocess.call(
                    """
                        cp /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+""" /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(archivo)+"""
                    """,
                    shell=True
                )
                print(4)
                subprocess.call(
                    """
                        sudo chmod 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(archivo)+"""
                    """,
                    shell=True
                )
                print(5)
            else:
                subprocess.call(
                    """
                        sudo mkdir /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas
                    """,
                    shell=True
                )

                subprocess.call(
                    """
                        sudo chmod -R 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas
                    """,
                    shell=True
                )


                subprocess.call(
                    """
                        sudo cp /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+""" /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/
                    """,
                    shell=True
                )

                subprocess.call(
                    """
                        sudo chmod -R 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(upload_file)+"""
                    """,
                    shell=True
                )

                subprocess.call(
                    """
                        sudo mv /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(upload_file)+"""  /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(archivo)+"""
                    """,
                    shell=True
                )
                pass

        else:
            
            subprocess.call(
                """
                    sudo mkdir /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""
                """,
                shell=True
            )

            subprocess.call(
                """
                    sudo chmod -R 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""
                """,
                shell=True
                )
            pass

            subprocess.call(
                """
                    sudo mkdir /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas
                """,
                shell=True
            )

            subprocess.call(
                """
                    sudo chmod -R 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas
                """,
                shell=True
            )


            subprocess.call(
                """
                    sudo cp /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+""" /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/
                """,
                shell=True
            )

            subprocess.call(
                """
                    sudo chmod -R 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(upload_file)+"""
                """,
                shell=True
            )

            subprocess.call(
                """
                    sudo mv /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(upload_file)+"""  /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(archivo)+"""
                """,
                shell=True
            )

            pass

    else:

        subprocess.call(
            """
                sudo mkdir /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""
            """,
            shell=True
        )

        subprocess.call(
            """
                sudo chmod -R 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""
            """,
            shell=True
            )
        pass

        subprocess.call(
            """
                sudo mkdir /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""
            """,
            shell=True
        )

        subprocess.call(
            """
                sudo chmod -R 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""
            """,
            shell=True
            )
        pass

        subprocess.call(
            """
                sudo mkdir /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas
            """,
            shell=True
        )

        subprocess.call(
            """
                sudo chmod -R 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas
            """,
            shell=True
        )


        subprocess.call(
            """
                sudo cp /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+""" /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/
            """,
            shell=True
        )

        subprocess.call(
            """
                sudo chmod -R 777 /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(upload_file)+"""
            """,
            shell=True
        )

        subprocess.call(
            """
                sudo mv /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(upload_file)+"""  /var/www/avi_"""+str(empresa)+"""/automatico/code/entradas/asignaciones/"""+str(anio)+"""/"""+str(mes)+"""/nuevas/"""+str(archivo)+"""
            """,
            shell=True
        )
        pass
    
    #ruta = '/home/sftpserver/BI_server/'
    #resul = enviosOtros( tmp )
    return response.json({
        "status": 'ok',
        "path": get_download_url(upload_file)
    })

def upload_file():
    """
    Esta función es invocada vía AJAX por el plugin dmuploader.
    """
    print('requestFile', request.vars)
    hoy = date.today().strftime("%Y-%m-%d")
    anio = str(hoy)[:4]
    mes  = meses(str(hoy)[5:7])
    empresa = 'Faleballa'
    original  = str(request.post_vars.file.filename).replace(' ','_').replace('-','_').replace('(','').replace(')','')
    if request.env.request_method != "POST":
        raise HTTP(404)
    upload_file = db.upload.upload_file.store(
        request.post_vars.file,
        filename=request.post_vars.file.filename
    )
    
    datosEmClSeAsi  = db.tmpEmpClieSegAsignacion 
    
    selInfoTmp = db( ).select( datosEmClSeAsi.ALL ).first()

    nombre_archivo, extension = os.path.splitext(upload_file)
    
    #print('Comprobar idAsignacion', selInfoTmp.asignacion)

    tmp = db.upload.insert(
        upload_file    = upload_file,
        empresa        = selInfoTmp.empresa,
        idAsignacion   = selInfoTmp.idAsignacion,
        asignacion     = selInfoTmp.asignacion,
        idEmpresa      = selInfoTmp.idEmpresa,
        idSegmento     = selInfoTmp.idSegmento,
        segmento       = selInfoTmp.segmento,
        idCliente      = selInfoTmp.idCliente,
        cliente        = selInfoTmp.cliente,
        nombreOriginal = original,
        idTablaTmp     = selInfoTmp.id,
        estadoCargue   = selInfoTmp.estadoCargue,
        destinoCargue  = 'BI'

    )   

    archivo = original

    #print('archivoFiless', archivo)    
    db( db.upload.id == tmp ).update( nombrefilescarpeta = archivo )


    if os.path.exists('/home/sftpserver/BI_SERVER/'+str(selInfoTmp.empresa)+''):

        
        if os.path.exists('/home/sftpserver/BI_SERVER/'+str(selInfoTmp.empresa)+'/'+str(selInfoTmp.cliente)+''):
            

                
            if os.path.exists('/home/sftpserver/BI_SERVER/'+str(selInfoTmp.empresa)+'/'+str(selInfoTmp.cliente)+'/'+str(selInfoTmp.segmento)+''):

                print(1)

                subprocess.call(

                    """
                        sudo chmod -R 777 /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""
                    """,
                    shell=True
                )

                
                print(2)
                subprocess.call(
                    """
                        sudo chmod 777 /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+"""
                    """,
                    shell=True
                )

                print(3)
                
                subprocess.call(
                    """
                        cp /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+""" /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(archivo)+"""
                    """,
                    shell=True
                )
                tmp =  """ cp /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+""" /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(archivo)+""""""
                print('3.1', tmp)
                print(4)

                subprocess.call(
                    """
                        mv /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(upload_file)+"""  /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(archivo)+"""
                    """,
                    shell=True
                )

                print(5)
            else:
                subprocess.call(
                    """
                        sudo mkdir /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""
                    """,
                    shell=True
                )

                subprocess.call(
                    """
                        sudo chmod -R 777 /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""
                    """,
                    shell=True
                )

                subprocess.call(
                    """
                        sudo chmod 777 /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+"""
                    """,
                    shell=True
                )


                subprocess.call(
                    """
                        sudo cp /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+""" /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/
                    """,
                    shell=True
                )


                subprocess.call(
                    """
                        sudo mv /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(upload_file)+"""  /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(archivo)+"""
                    """,
                    shell=True
                )
                pass

        else:
            
            subprocess.call(
                """
                    sudo mkdir /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""
                """,
                shell=True
            )

            subprocess.call(
            """
                sudo chmod -R 777 /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""
            """,
            shell=True
            )
            

            subprocess.call(
                """
                    sudo mkdir /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""
                """,
                shell=True
            )

            subprocess.call(
                """
                    sudo chmod -R 777 /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""
                """,
                shell=True
            )


            subprocess.call(
                """
                    cp /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+""" /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/
                """,
                shell=True
            )

            # subprocess.call(
            #     """
            #         sudo chmod 777 home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(archivo)+"""
            #     """,
            #     shell=True
            # )

            subprocess.call(
                """
                    sudo mv /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(upload_file)+"""  /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(archivo)+"""
                """,
                shell=True
            )

            pass

    else:

        subprocess.call(
            """
                sudo mkdir /var/www/avi_"""+str(selInfoTmp.empresa)+"""
            """,
            shell=True
        )

        subprocess.call(
            """
            sudo chmod -R 777 /var/www/avi_"""+str(selInfoTmp.empresa)+"""
            """,
        shell=True
        )
        

        subprocess.call(
            """
                sudo mkdir /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""
            """,
            shell=True
        )

        subprocess.call(
            """
                sudo chmod -R 777 /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""
            """,
            shell=True
        )
        

        subprocess.call(
            """
                sudo mkdir /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""
            """,
            shell=True
        )

        subprocess.call(
            """
                sudo chmod -R 777 /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""
            """,
            shell=True
        )


        subprocess.call(
            """
                cp /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/"""+str(upload_file)+""" /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/
            """,
            shell=True
        )

        # subprocess.call(
        #     """
        #         sudo chmod 777 home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(archivo)+"""
        #     """,
        #     shell=True
        # )

        subprocess.call(
            """
                sudo mv /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(upload_file)+"""  /home/sftpserver/BI_SERVER/"""+str(selInfoTmp.empresa)+"""/"""+str(selInfoTmp.cliente)+"""/"""+str(selInfoTmp.segmento)+"""/"""+str(archivo)+"""
            """,
            shell=True
        )
       
        pass

    subprocess.call(
        """
        sudo chmod -R 777 /var/www/avi_"""+str(selInfoTmp.empresa)+"""
        """,
        shell=True
    )


    # if os.path.exists('/home/sftpserver/BI_SERVER/'+str(selInfoTmp.empresa)+'/historico'):



    return response.json({
        "status": "ok",
        "path": get_download_url(upload_file)
    })

def iniciarProcesos():
    data = []
    variables = request.vars

    print('variablesProcesos', variables)

    

    if variables.opc == 'updateCampanas':
        # Proceso de update campanas y dashbard
        data = updateCampanasDashboard( variables.asignacionFile, variables )
        # Fin proceso de update campanas y dashbard
    elif variables.opc == 'gestion360':
        # Proceso de gestion 360
        data = gestion360( variables )
        # Fin proceso de gestion 360
    elif variables.opc == 'mejorGestion':
        # Proceso de mejor gestion
        data = mejorGestion('falabella',variables.clienteSegmento,variables.segmentoAsignacion,variables.asignacionFile,variables.archivo,variables)
        # Fin proceso de mejor gestion
    elif variables.opc == 'descargarArchivos':
        # Proceso de mejor gestion
        data = descargarArchivos(variables)
    else:
        # Proceso de macro
        data = macro(variables)
        # Fin proceso de macro
        pass
   
    return data

def _updateCampanasDashboard( idAsignacion, variables ):
    hoy = date.today().strftime("%Y-%m-%d")
    data = []
    valorResul = []
    informaResul = []
    print('updateCampanasDashboardidAsignacion', idAsignacion)
    return gluon.contrib.simplejson.dumps(data)

def updateCampanasDashboard( idAsignacion, variables ):
    hoy = date.today().strftime("%Y-%m-%d")
    data = []
    valorResul = []
    informaResul = []
    print('updateCampanasDashboardidAsignacion', idAsignacion)

    # '".date('Y-m-d')."' between c.Fecha_de_inicio and c.Fecha_de_fin and c.tipo = ''

    sqlVerificacion = """

        SELECT 
            ID_CAMPANA
        FROM 
            avi_falabella.Campanas 
        WHERE 
            id_asignacion = """+str(idAsignacion)+"""
        AND
            date(Fecha_de_creacion) = '"""+str(hoy)+"""'

    """


    #print('sqlVerificacion', sqlVerificacion)
    with engine2.connect() as connection:
        countTable = connection.execute(sqlVerificacion)
    #print('countTableInicial', countTable)
    
    for x in countTable:
        valorResul.append(x)
        pass

    #print('valorResul',valorResul)

    if len(valorResul) > 0:



        #print('Agragar mas')

        for c in valorResul:

            #print('cccccc', c[0])

            sqlUpdateCampanas = """

                UPDATE 
                    avi_falabella.Campanas 
                SET 
                    Estado = 'inactiva' 
                WHERE 
                    ID_CAMPANA = """+str(c[0])+"""

            """

            #print('sqlUpdateCampanas', sqlUpdateCampanas)

            with engine2.connect() as connection:
                connection.execute(sqlUpdateCampanas)

            

            sqlVerificacionCampanasId = """

                SELECT 
                    COUNT(*)
                FROM 
                    avi_falabella.Campanas 
                WHERE 
                    ID_CAMPANA = """+str(c[0])+"""
                AND
                    Estado = 'activa'
            """

            #print('sqlVerificacionCampanasId', sqlVerificacionCampanasId)
            with engine2.connect() as connection:
                countIdCampabaInacativaTmp = connection.execute(sqlVerificacionCampanasId)


            for ci in countIdCampabaInacativaTmp:
                countIdCampabaInacativa  = ci[0]
                pass


            #print('countIdCampabaInacativa', countIdCampabaInacativa)

            if countIdCampabaInacativa == 0:

                #print('Todo bien update campanas')

                sqlUpdateCampasDashboard = """

                    UPDATE
                        avi_falabella.campana_dashboard
                    SET
                        estado = 'inactiva'
                    WHERE 
                        id_campana = """+str(c[0])+"""
                """

                #print('sqlUpdateCampasDashboard', sqlUpdateCampasDashboard)

                with engine2.connect() as connection:
                    connection.execute(sqlUpdateCampasDashboard)

                sqlVerificacionCampanasDashboardId = """

                    SELECT
                        COUNT(*)
                    FROM 
                        avi_falabella.campana_dashboard
                    WHERE 
                        ID_CAMPANA = """+str(c[0])+"""
                    AND
                        Estado = 'activa'

                """
                #print('sqlVerificacionCampanasDashboardId', sqlVerificacionCampanasDashboardId)
                with engine2.connect() as connection:
                    countsqlUpdateCampasDashboardTmp = connection.execute(sqlVerificacionCampanasDashboardId)


                for cd in countsqlUpdateCampasDashboardTmp:
                    countsqlUpdateCampasDashboard  = cd[0]
                    pass

                #print('countsqlUpdateCampasDashboard', countsqlUpdateCampasDashboard)
                if countsqlUpdateCampasDashboard == 0:

                    print('Todo bien update campana_dashboard')

                else:

                    
                    informaResul.append(
                        dict(
                            idCampana = c[0],
                            detalle   = 'La campaña de ID: '+str(c[0])+' no pudo ser inactivada en la tabla campana_dashboard'
                        )
                    )
                    pass

            else:

                data.append(
                    dict(
                        indicador = 0,
                        resultado = 'error',
                        mensaje   = 'Las campañas pertenecientes a la asignación de ID '+str(idAsignacion)+' no se inactivaron',
                        idResultado = 0           
                    )
                )
                idResulInsert  = insertResulProces(variables.clienteSegmento,0,'',variables, 'Las campañas pertenecientes a la asignación de ID '+str(idAsignacion)+' no se inactivaron')
                return gluon.contrib.simplejson.dumps(data)

                pass



            pass

        if len(informaResul) > 0:

            idCampanasList = []
            for cp in informaResul:
                idCampanasList.append(cp)
                pass
            estado   = 'info',
            mensajes = 'Las campañas se inactivaron correctamente, Pero los siguientes ID_CAMPANA: '+str(idCampanasList)+' no se inactivaron en campana_dashboard'
        else:
            estado   = 'success',
            mensajes = 'Las campañas y campana_dashboard se inactivaron correctamente'
            pass

        data.append(
            dict(
                indicador = 1,
                resultado = estado,
                mensaje   = mensajes,
                idResultado = 0           
            )
        )

        idResulInsert  = insertResulProces(variables.clienteSegmento,1,'',variables,mensajes)
        return gluon.contrib.simplejson.dumps(data)
    else:
        data.append(
            dict(
                indicador = 1,
                resultado = 'info',
                mensaje   = 'No hay campañas activas para la asignación de ID '+str(idAsignacion)+' no se inactivaron',
                idResultado = 0           
            )
        )
        # data.append(
        #     dict(
        #         indicador = 0,
        #         resultado = 'error',
        #         mensaje   = 'Las campañas pertenecientes a la asignación de ID '+str(idAsignacion)+' no se inactivaron',
        #         idResultado = 0           
        #     )
        # )
        #updateCampanasDashboard( idAsignacion )
        idResulInsert  = insertResulProces(variables.clienteSegmento,1,'',variables, 'No hay campañas activas para la asignación de ID '+str(idAsignacion)+' no se inactivaron')
        return gluon.contrib.simplejson.dumps(data)
        pass

def gestion360( variables ):
    data = []
    print('Gestion 360')
    resultaGestion360 = subprocess.call(
        """
            php /var/www/avi_falabella/index.php reporte360 index 0
        """,
        shell=True
    )
    print('resultaGestion360', resultaGestion360)
    if resultaGestion360 == 0:

        idResulInsert  = insertResulProces(variables.clienteSegmento,resultaGestion360,'',variables, 'Ejecución exitosa')

        data.append(
            dict(
                indicador = 1,
                resultado = 'success',
                mensaje   = 'Ejecución exitosa',
                idResultado = 0           
            )
        )
    else:

        idResulInsert  = insertResulProces(variables.clienteSegmento,resultaGestion360,'',variables, 'Ejecución no exitosa')
        data.append(
            dict(
                indicador = 0,
                resultado = 'error',
                mensaje   = 'Ejecución no exitosa',
                idResultado = 0
            )
        )
        pass
    
    return gluon.contrib.simplejson.dumps(data) 

def mejorGestion( nombreempresa, idcliente, idsegmento, idasignacion, archivo, variables ):

    print('Mejor Gestion')
    print('nombreempresa', nombreempresa)
    print('idcliente', idcliente)
    print('idsegmento', idsegmento)
    print('idasignacion', idasignacion)
    print('archivo', archivo)
    data = []
    hoy = date.today().strftime("%Y-%m-%d")
    #archivoMejorGestion  = True if int(archivo) == 1 else False
    #tmp = """/var/www/reports/best_management_360/reportsBestManagedTodayMonth.py """+str(hoy).replace('-','')+""" """+str(nombreempresa)+""" """+str(idcliente)+""" """+str(idsegmento)+""" """+str(idasignacion)+""""""

    #   print('tmp',tmp)
    #resultaMejorGestion = subprocess.call(""" python3.6 /var/www/reports/best_management_360/reportsBestManagedTodayMonth.py """ .format() +str(hoy).replace('-','')+""" """+str(nombreempresa)+""" """+str(idcliente)+""" """+str(idsegmento)+""" """+str(idasignacion)+""" """, shell=True)

    #resultaMejorGestion = subprocess.call("python3.6 /var/www/reports/best_management_360/reportsBestManagedTodayMonth.py {0} {1} {2} {3} {4} {5}".format(str(hoy).replace('-',''),nombreempresa,idcliente,idsegmento,idasignacion,archivo), shell=True)

    fecha               = str(hoy).replace('-','')
    enterpriseName      = nombreempresa
    idCliente           = idcliente
    idSegmento          = idsegmento 
    idAsignacion        = idasignacion
    isDownloadable      = archivo
    isAppendOrReplace   = '0'

    #print('tmp', "python3.6 /var/www/reports/best_management_360/reportsBestManagedTodayMonth.py {0} {1} {2} {3} {4} {5} {6}".format(fecha,enterpriseName,idCliente,idSegmento,idAsignacion,isDownloadable,isAppendOrReplace))
    resultaMejorGestion = subprocess.call("python3.6 /var/www/reports/best_management_360/reportsBestManagedTodayMonth.py {0} {1} {2} {3} {4} {5} {6} >> /var/www/reports/best_management_360/reportsBestManagedTodayMonth.log".format(fecha,enterpriseName,idCliente,idSegmento,idAsignacion,isDownloadable,isAppendOrReplace), shell=True)

    print('resultaMejorGestion', resultaMejorGestion)
    archivoDescarga = 'best_management_360_last_'+str(nombreempresa)+'_'+str(idCliente)+'_'+str(idSegmento)+'_'+str(idAsignacion)+'.xlsx'

    if resultaMejorGestion == 0:


        print(2)
        subprocess.call(
            """
                sudo chmod 777 /home/sftpserver/reports/falabella/"""+str(archivoDescarga)+"""
            """,
            shell=True
        )

        print(3)

        subprocess.call(
            """
                sudo chmod -R 777 /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/static/archivosDescargas/
            """,
            shell=True
        )
        print(4)
        subprocess.call(
            """
                cp /home/sftpserver/reports/falabella/"""+str(archivoDescarga)+""" /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/static/archivosDescargas/
            """,
            shell=True
        )

        print(5)


        idResulInsert  = insertResulProces(idcliente,resultaMejorGestion,archivoDescarga,variables,'Ejecución exitosa')
        nuevoArchivo   = str(archivoDescarga)+'_'+str(idResulInsert) 
        #db( db.verificacionProcesos.id == idResultado  ).update(upload_file=nuevoArchivo)

        print('6', idResulInsert)

        data.append(
            dict(
                indicador = 1,
                resultado = 'success',
                mensaje   = 'Todo okis',
                idResultado = idResulInsert           
            )
        )
    else:

        idResulInsert  = insertResulProces(idcliente,resultaMejorGestion,archivoDescarga,variables,'Error ejecucion')
        data.append(
            dict(
                indicador = 0,
                resultado = 'Error ejecución',
                mensaje   = 'Error ejecución',
                idResultado = 0  
            )
        )
        pass

    return gluon.contrib.simplejson.dumps(data) 

def macro( variables ):
    print('Macro Variables', variables)
    data = []
    dataMacro = []
    """    CAMPOS QUE SE DEBEN ENVIAR ???Soporte*2017***
        - empresa => Nombre empresa en plataforma.
        - Cliente => Nombre del cliente.
        - idcliente => id del cliente del AVI.
        - segmento => Nombre del segmento.
        - idsegmento => id del segmento del AVI.
        - Lista con el nombre de los archivos cargados.
        - nueva_asig => True o False según se escoja.
        - id_asignacion => id de la asignación seleccionada.
        - fecha_actual => YYYYMMDDHHMMSS.
        C. COSAS CONTEMPLAR DENTRO DE LA "MACRO"

        - AGREGAR sys.exit() con retorno 2 en caso que la ejecución de la "macro" genere un error.
        - Exportar reporte de cedulas que tienen longitud diferente de 8 o 9 caracteres.
        - generar salida de retorno con valor 1 para exportar archivo de cedulas que no cumplieron con la longitud en ruta '/opt/intelbpo/automaticos/<empresa>/macro/reporte_cedulas/reporte_cedulas_nocumple_YYYYMMDDHHMMSS.csv' => YYYYMMDDHHMMSS corresponde al parametro fecha_actual de la 

    """
    hoy = date.today().strftime("%Y-%m-%d")
    datosEmClSeAsi  = db.tmpEmpClieSegAsignacion 
    selInfoTmp = db( ).select( datosEmClSeAsi.ALL ).first()

    archivos = db( db.upload.idTablaTmp == selInfoTmp.id ).select( db.upload.ALL )
    lisArchivos = []
    for x in archivos:
        lisArchivos.append(x.nombreOriginal)
        pass

    #print('lisArchivos', lisArchivos)
    # dataMacro.append(
    #     dict(
    #         empresa       = 'falabella',
    #         Cliente       = variables.clienteNombre,
    #         idcliente     = variables.clienteSegmento,
    #         segmento      = variables.segmentoNombre,
    #         idsegmento    = variables.segmentoAsignacion, 
    #         nombre        = lisArchivos,
    #         nueva_asig    = selInfoTmp.estadoCargue,
    #         id_asignacion = variables.asignacionFile,
    #         fecha_actual  = str(request.now)[:19].replace('-','').replace(' ','').replace(':','')int(variables.asignacionFile), if int(selInfoTmp.estadoCargue) == 1 else False
    #     )
    # )
    dataMacro = dict(
        empresa       = 'falabella',
        cliente       = variables.clienteNombre,
        idcliente     = variables.clienteSegmento,
        segmento      = variables.segmentoNombre,
        idsegmento    = variables.segmentoAsignacion, 
        nombre        = lisArchivos,
        nueva_asig    = True if int(selInfoTmp.estadoCargue) == 1 else False,
        idasignacion  = variables.asignacionFile,
        fecha_actual  = str(request.now)[:19].replace('-','').replace(' ','').replace(':','')
    )
    print('dataMacro', dataMacro)



    # with open('out.txt', 'w+') as fout:
    #     with open('err.txt', 'w+') as ferr:
    #         out = subprocess.call(['python3.6', '/var/www/filesInteliBPO/mainEjecu.py', """{}""".format(
    #             json.dumps(dataMacro))], stdout=fout, stderr=ferr)
    #         # reset file to read from it
    #         fout.seek(0)
    #         print('fout.read()', fout.read())
    #         # save output (if any) in variable
    #         output = fout.read()

    #         # reset file to read from it
    #         ferr.seek(0)
    #         # save errors (if any) in variable
    #         errors = ferr.read()

    #         print('outputsssss',output)
    #         print('errorsssssss',errors)
    # print('out.returncodesssss', out.returncode)

    # with open('out.txt', 'w+') as fout:
    #     with open('err.txt', 'w+') as ferr:
    #         out = subprocess.run(['python3.6', '/opt/intelbpo/automaticos/avi_falabella/macro/src/main.py', """{}""".format(
    #             json.dumps(dataMacro))], stdout=fout, stderr=ferr)
    #         # reset file to read from it
    #         fout.seek(0)
    #         # save output (if any) in variable
    #         output = fout.read()
    #         #reset file to read from it
    #         ferr.seek(0)
    #         # save errors (if any) in variable
    #         errors = ferr.read()

    #         print('output',output)
    #         print('errors',errors)
    #         #out.returncodeinsertResulProces( out.returncode )
    # resultaMacro  = out.returncode
    # print('resultaMacro',resultaMacro)

    #tmp = "sudo python3.6 /opt/intelbpo/automaticos/avi_falabella/macro/src/main.py {}".format(json.dumps(dataMacro))
    #print('Prinnnnnnn', tmp)

    #resultaMacro = subprocess.call(['sudo python3.6','/opt/intelbpo/automaticos/avi_falabella/macro/src/main.py', """{}""".format(json.dumps(dataMacro))," >> /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/static/archivosDescargas/errors_2.txt"], shell=False)

    resultaMacro = subprocess.call(['sudo','python3.6','/opt/intelbpo/automaticos/avi_falabella/macro/src/main.py', """{}""".format(json.dumps(dataMacro))], shell=False)
    print('resultaMacro', resultaMacro)

    if resultaMacro <= 1 :
        data.append(
            dict(
                indicador = 1,
                resultado = 'success',
                mensaje   = 'Todo okis'           
            )
        )
    else:

        data.append(
            dict(
                indicador = 0,
                resultado = 'error',
                mensaje   = 'Todo mal macro'           
            )
        )
        pass
    # if out.returncode:
        

    #     resulEjecu = db( db.verificacionProcesos.id == out.returncode ).select( db.verificacionProcesos.ALL ).last()


    #     print('resulEjecu', resulEjecu.resultadoEjecucion, '**************************', resulEjecu.nombreEjecucion)
    #     print('resultaMacro', resultaMacro)

    #     if resultaMacro <= 1 :
    #         data.append(
    #             dict(
    #                 indicador = 1,
    #                 resultado = 'success',
    #                 mensaje   = 'Todo okis'           
    #             )
    #         )
    #     else:

    #         data.append(
    #             dict(
    #                 indicador = 0,
    #                 resultado = 'error',
    #                 mensaje   = 'Todo mal macro'           
    #             )
    #         )
    #         pass
    # else:

    #     data.append(
    #         dict(
    #             indicador = 0,
    #             resultado = 'error',
    #             mensaje   = 'Todo mal macro'           
    #         )
    #     )

    #     pass
    return gluon.contrib.simplejson.dumps(data) 

def descargarArchivos( variables ):

    data = []

    print('descargarArchivos', variables)
    archivo  = db(db.verificacionProcesos.id==variables.idArchivoDescarga).select(db.verificacionProcesos.upload_file).last()
    print('archivo', archivo)
    print('archivo.upload_file', archivo.upload_file)
    fecha = str(request.now)[:19].replace('-','').replace(' ','').replace(':','')
    nuevoArchivo  = "descargaMG_"+str(fecha)+""
    
    if os.path.exists('/var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/static/archivosDescargas/'+str(archivo.upload_file)+''):
        
        subprocess.call(
            """
                cp /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/static/archivosDescargas/"""+str(archivo.upload_file)+""" /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/archivosDescargas/
            """,
            shell=True
        )

        subprocess.call(
            """
                sudo mv /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/archivosDescargas/"""+str(archivo.upload_file)+""" /var/www/filesInteliBPO/web2py/applications/InteliBpoFilesII/uploads/archivosDescargas/"""+str(nuevoArchivo)+"""
            """,
            shell=True
        )
        
        pass


    if archivo:
        idResulInsert  = insertResulProces(variables.clienteSegmento,1,nuevoArchivo,variables,'Archivo descargado exitosamente')
        data.append(
            dict(
                indicador = 1,
                resultado = 'success',
                mensaje   = 'Archivo descargado exitosamente',
                idResultado = archivo.upload_file           
            )
        )
    else:
        idResulInsert  = insertResulProces(variables.clienteSegmento,0,nuevoArchivo,variables,'Archivo no descargado exitosamente')
        data.append(
            dict(
                indicador = 0,
                resultado = 'error',
                mensaje   = 'Archivo no descargado exitosamente',
                idResultado = 0           
            )
        )

        pass
    return gluon.contrib.simplejson.dumps(data) 

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
