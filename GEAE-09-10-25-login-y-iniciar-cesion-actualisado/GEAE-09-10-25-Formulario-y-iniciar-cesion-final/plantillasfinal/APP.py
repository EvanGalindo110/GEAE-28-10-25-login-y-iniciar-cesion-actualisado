from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "clave_secreta"

@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/animales')
def animales():
    return render_template('animales.html')

@app.route('/lugares')
def lugares():
    return render_template('lugares.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/veiculos')
def veiculos():
    return render_template('veiculos.html')


@app.route('/login', methods=['GET', 'POST'])
def crear_cuenta():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        dia = request.form.get('dia')
        mes = request.form.get('mes')
        año = request.form.get('año')
        genero = request.form.get('genero')
        correo = request.form.get('correo')
        contraseña = request.form.get('contraseña')
        
        session['usuario'] = nombre
        session['nombre'] = nombre

        with open("usuarios.txt", "a") as archivo:
            archivo.write(f"{correo},{contraseña},{nombre},{apellido},{dia},{mes},{año},{genero}\n")

        return redirect(url_for('inicio'))

    return render_template('login.html')


@app.route('/iniciar cesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        correo = request.form.get('correo')
        contraseña = request.form.get('contraseña')

        try:
            with open("usuarios.txt", "r") as archivo:
                usuarios = archivo.readlines()
        except FileNotFoundError:
            usuarios = []

        for usuario in usuarios:
            datos = usuario.strip().split(',')
            if len(datos) >= 2 and correo == datos[0] and contraseña == datos[1]:
                session['usuario'] = datos[2]  
                return redirect(url_for('inicio'))

        return render_template('iniciar cesion.html', error="La contraseña o el Gmail son incorrectos")

    return render_template('iniciar cesion.html')



@app.route('/cerrar')
def cerrar():
    session.pop('usuario', None)
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(debug=True)


