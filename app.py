from flask import Flask, render_template, request
from static.entities import euclides, mcd


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/minimo_comun_divisor', methods=['GET', 'POST'])
def minimo_comun_divisor():
    
    if request.method == 'POST':
        
        numero1 = int(request.form.get('numero1'))
        numero2 = int(request.form.get('numero2'))
        
        lcd = mcd.mcd(numero1, numero2)
        
        return render_template('result_mcd.html', lcd = lcd)
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')