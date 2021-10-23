from flask import Flask, render_template, request, redirect, flash
# from controllers import users
from controllers import bases
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
@app.get('/')
def home():
    return render_template('index.html')

@app.post('/guardar')
def guardarUsuario():
    print('validar')
    data = request.form
    
    print(data['contra'])
    
    if( data.getlist('gridCheck')):
        
        datos = bases.listaBases(data)
        print(datos)
        return render_template('index.html',datosDB = datos)
    else:
        
        bases.crear(data)
        return redirect('/')
app.run(debug=True)