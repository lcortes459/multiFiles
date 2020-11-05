# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
# def index():
# redirect(URL('guardin','default','index'))
# response.flash = T("Hello World")
# return dict(message=T('Welcome to web2py!'))

from sqlalchemy import create_engine



engine2 = create_engine(
    "mysql+pymysql://{user}:{pw}@10.142.0.62/{db}"
    .format(
        user="root",
        pw="j7t05fLcn0",
        db="avi_falabella"
    )
)

#engine = create_engine("mysql://root:j7t05fLcn0@34.75.120.5/avi_falabella")

def get_download_url(upload_file):
    folder = "uploads"
    fullfilename = db.upload.upload_file.retrieve(
        upload_file, nameonly=True)[1]
    filename = fullfilename[fullfilename.find(folder) + len(folder) + 1:]
    filename = filename.replace("\\", "/")

    return URL("download", args=filename)




def index():
   

    #print('engine2', engine2)

    # sqlClientes = """

    #     SELECT 
    #         * 
    #     FROM 
    #         avi_falabella.Clientes
    #     WHERE 
    #         estado = 1 

    # """
    # ctmp = engine.execute(sqlClientes)

    # with engine.begin() as conn:
    #     conn.execute(
    #         text(" SELECT * FROM avi_falabella.Clientes WHERE estado = 1 ")
    #     )

    # print('text', text)


    #print('ctmp', ctmp)
    # with engine2.connect() as connection:
    #     countTable = connection.execute(sqlClientes)

    # print('countTable', countTable)

    # for x in countTable:
    #     countTable = x[0]
    # pass

    # if countTable>0:
    #     print('Mayor a cero')
    #     clientes = []
    #     for y in countTable:
    #         nombre       = y['nombre']
    #         descripcion  = y['descripcion']
    #         estado       = y['estado']
    #         clientes.append(y)
    #         pass
    #     print('clientes', clientes)
    # else:
    #     print('Igual a cero')
    #     pass
    return locals()



# def conexionBd(base,passw,host,user):

#     try:

#         conexionBd = create_engine(
#             "mysql+pymysql://{user}:{pw}@{hos}/{db}"
#             .format(
#                 user=user,
#                 hos=host,
#                 pw=passw,
#                 db= base
#             )
#         )
#         return conexionBd
#     except Exception as e:
#         print("Error",e)
#         errorTmp = 'No conexion'
#         return errorTmp

    

def upload_file():
    """
    Esta función es invocada vía AJAX por el plugin dmuploader.
    """
    if request.env.request_method != "POST":
        raise HTTP(404)
    upload_file = db.upload.upload_file.store(
        request.post_vars.file,
        filename=request.post_vars.file.filename
    )
    print('tamano', len(upload_file))
    print('upload', upload_file)
    tmp = db.upload.insert(upload_file=upload_file)
    print('tmp', tmp)
    return response.json({
        "status": "ok",
        "path": get_download_url(upload_file)
    })



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
