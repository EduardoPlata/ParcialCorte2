from models import bases


def listaBases(datos):
    
    datos_bases= bases.listar(datos)
    return datos_bases

def crear(datos):
    
    bases.crearDB(datos)
