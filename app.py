from flask import Flask, render_template, request
from static.entities import euclides, mcd


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/maximo_comun_divisor', methods=['GET', 'POST'])
def minimo_comun_divisor():
    
    if request.method == 'POST':
        
        numero1 = int(request.form.get('numero1'))
        numero2 = int(request.form.get('numero2'))
        
        resultado = mcd.mcd(numero1, numero2)
        
        return render_template('result', resultado = resultado)
    return render_template('index.html')

@app.route('/euclides', methods=['POST', 'GET'])
def algoritmo_euclides():
    
    if request.method == 'POST':
        
        numero1 = int(request.form.get('numero1'))
        numero2 = int(request.form.get('numero2'))
        
        resultado = euclides.euclides(numero1, numero2)
        
        return render_template('result.html', resultado = resultado)
    return render_template('index.html')

    

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')