import math,sys,os,re,subprocess
import os.path, json

# dataMacro = {
# 	"empresa": "falabella", 
# 	"idasignacion": 21, 
# 	"idsegmento": "5", 
# 	"nueva_asig": True, 
# 	"segmento": "Preventiva_Peru", 
# 	"nombre": ["15142aae46bbc9198c74.html"], 
# 	"idcliente": "3", 
# 	"fecha_actual": "20201118111156", 
# 	"cliente": "Falabella_Peru"
# }

dataMacro = {
	'empresa': 'falabella', 
	'idasignacion': 21, 
	'idsegmento': '5', 
	'nueva_asig': True, 
	'segmento': 'Preventiva_Peru', 
	'nombre': ['15142aae46bbc9198c74.html'], 
	'idcliente': '3', 
	'fecha_actual': '20201118111156', 
	'cliente': 'Falabella_Peru'
}

# with open('out.txt', 'w+') as fout:
#     with open('err.txt', 'w+') as ferr:
#         out = subprocess.call(['python3.6', '/opt/intelbpo/automaticos/avi_falabella/macro/src/main.py', """{}""".format(
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
# print('out.returncodesssss', out)

resultaMacro = subprocess.call("sudo python3.6 /opt/intelbpo/automaticos/avi_falabella/macro/src/main.py {}".format(json.dumps(dataMacro)), shell=True)

#print('resultaMacro',resultaMacro)




#sudo python3.6 /opt/intelbpo/automaticos/avi_falabella/macro/src/main.py "{'empresa': 'falabella', 'idasignacion': 21, 'idsegmento': '5', 'nueva_asig': true, 'segmento': 'Preventiva_Peru', 'nombre': #['15142aae46bbc9198c74.html'], 'idcliente': '3', 'fecha_actual': '20201118111156', 'cliente': 'Falabella_Peru'}"



