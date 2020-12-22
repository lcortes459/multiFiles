
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    # (T('Home'), False, URL('default', 'index'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

# if not configuration.get('app.production'):
#     _app = request.application
#     response.menu += [
#         (T('My Sites'), False, URL('admin', 'default', 'site')),
#         (T('This App'), False, '#', [
#             (T('Design'), False, URL('admin', 'default', 'design/%s' % _app)),
#             (T('Controller'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/controllers/%s.py' % (_app, request.controller))),
#             (T('View'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/views/%s' % (_app, response.view))),
#             (T('DB Model'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/models/db.py' % _app)),
#             (T('Menu Model'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/models/menu.py' % _app)),
#             (T('Config.ini'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/private/appconfig.ini' % _app)),
#             (T('Layout'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/views/layout.html' % _app)),
#             (T('Stylesheet'), False,
#              URL(
#                  'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % _app)),
#             (T('Database'), False, URL(_app, 'appadmin', 'index')),
#             (T('Errors'), False, URL(
#                 'admin', 'default', 'errors/' + _app)),
#             (T('About'), False, URL(
#                 'admin', 'default', 'about/' + _app)),
#         ]),
#         ('web2py.com', False, '#', [
#             (T('Download'), False,
#              'http://www.web2py.com/examples/default/download'),
#             (T('Support'), False,
#              'http://www.web2py.com/examples/default/support'),
#             (T('Demo'), False, 'http://web2py.com/demo_admin'),
#             (T('Quick Examples'), False,
#              'http://web2py.com/examples/default/examples'),
#             (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
#             (T('Videos'), False,
#              'http://www.web2py.com/examples/default/videos/'),
#             (T('Free Applications'),
#              False, 'http://web2py.com/appliances'),
#             (T('Plugins'), False, 'http://web2py.com/plugins'),
#             (T('Recipes'), False, 'http://web2pyslices.com/'),
#         ]),
#         (T('Documentation'), False, '#', [
#             (T('Online book'), False, 'http://www.web2py.com/book'),
#             (T('Preface'), False,
#              'http://www.web2py.com/book/default/chapter/00'),
#             (T('Introduction'), False,
#              'http://www.web2py.com/book/default/chapter/01'),
#             (T('Python'), False,
#              'http://www.web2py.com/book/default/chapter/02'),
#             (T('Overview'), False,
#              'http://www.web2py.com/book/default/chapter/03'),
#             (T('The Core'), False,
#              'http://www.web2py.com/book/default/chapter/04'),
#             (T('The Views'), False,
#              'http://www.web2py.com/book/default/chapter/05'),
#             (T('Database'), False,
#              'http://www.web2py.com/book/default/chapter/06'),
#             (T('Forms and Validators'), False,
#              'http://www.web2py.com/book/default/chapter/07'),
#             (T('Email and SMS'), False,
#              'http://www.web2py.com/book/default/chapter/08'),
#             (T('Access Control'), False,
#              'http://www.web2py.com/book/default/chapter/09'),
#             (T('Services'), False,
#              'http://www.web2py.com/book/default/chapter/10'),
#             (T('Ajax Recipes'), False,
#              'http://www.web2py.com/book/default/chapter/11'),
#             (T('Components and Plugins'), False,
#              'http://www.web2py.com/book/default/chapter/12'),
#             (T('Deployment Recipes'), False,
#              'http://www.web2py.com/book/default/chapter/13'),
#             (T('Other Recipes'), False,
#              'http://www.web2py.com/book/default/chapter/14'),
#             (T('Helping web2py'), False,
#              'http://www.web2py.com/book/default/chapter/15'),
#             (T("Buy web2py's book"), False,
#              'http://stores.lulu.com/web2py'),
#         ]),
#         (T('Community'), False, None, [
#             (T('Groups'), False,
#              'http://www.web2py.com/examples/default/usergroups'),
#             (T('Twitter'), False, 'http://twitter.com/web2py'),
#             (T('Live Chat'), False,
#              'http://webchat.freenode.net/?channels=web2py'),
#         ]),
#     ]

# -*- coding: utf-8 -*-
import math,sys,os,re,subprocess
import os.path, json,shlex
from sqlalchemy import create_engine



#resul = {'empresa': 'falabella', 'idasignacion': 21, 'idsegmento': '5', 'nueva_asig': True, 'segmento': 'Preventiva_Peru', 'nombre': ['Asignacion_PREV_REF_BOT_2TEST.xlsx'], 'idcliente': '3', 'fecha_actual': '20201113115517', 'cliente': 'Falabella_Peru'}


# print('resul',json.dumps(resul))
# # args = shlex.split(""" python3.6 /opt/intelbpo/automaticos/avi_falabella/macro/src/main.py {} """.format(json.dumps(resul)))

# # print(args)


# # p = subprocess.Popen(args) # Success!


# # print('p', p)

def runMacro( dataMacro ):
	resulMacro = ''
	print('aca es la macro')
	with open('out.txt', 'w+') as fout:
	    with open('err.txt', 'w+') as ferr:
	        out = subprocess.call(['python3.6', '/opt/intelbpo/automaticos/avi_falabella/macro/src/main.py', """{}""".format(
	            json.dumps(dataMacro))], stdout=fout, stderr=ferr)
	        # reset file to read from it
	        fout.seek(0)
	        # save output (if any) in variable
	        output = fout.read()

	        # reset file to read from it
	        ferr.seek(0)
	        # save errors (if any) in variable
	        errors = ferr.read()
	        resulMacro = out
	        print('output',output)
	        print('errors',errors)
	        print('resulMacro',resulMacro)

	print('resul', out)
	return resulMacro






def insertResulProces( idcliente,resultaMejorGestion,archivoDescarga, variables, mensaje ):


    resul = db.verificacionProcesos.insert(
        idEmpresa           = 1,
        empresa             = 'falabella',
        idCliente           = idcliente,
        cliente             = variables.clienteNombre,
        idSegmento          = variables.clienteSegmento,
        segmento            = variables.segmentoNombre,
        idAsignacion        = variables.asignacionFile,
        asignacion          = variables.asignacionFile,
        nombreEjecucion     = variables.opc,
        resultadoEjecucion  = resultaMejorGestion,
        upload_file         = archivoDescarga,
        mensaje             = mensaje
    )
    return resul
