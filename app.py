from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola, Mundo!'

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/listar_notas')
def listar_notas():
    return render_template('listar_notas.html')

if __name__ == '__main__':
    app.run(debug=True)