import mysql.connector

def listar(datos):
    
    DB = mysql.connector.connect(
    host=datos['host'],
    user=datos['user'],
    password=datos['contra'],
    port=datos['port']
    )
    
    cursor = DB.cursor(dictionary=True)
    cursor.execute('show databases;')
    return cursor.fetchall()
    

def crearDB(datos):
    print('conexion db')
    DB = mysql.connector.connect(
    host=datos['host'],
    user=datos['user'],
    password=datos['contra'],
    port=datos['port']
    )
    cursor = DB.cursor(dictionary=True)
    cursor.execute('create database '+datos['nombre']+';')  
    