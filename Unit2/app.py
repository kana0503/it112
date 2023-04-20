from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, static_folder='./templates')

@app.route('/', methods =['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/fortune', methods = ['POST', 'GET'])
def fortune():
    if request.method == 'POST':
        name = request.form['user']
        color = request.form['color']
        number = request.form['number']
        result = {
            'name' : name,
            'color' : color,
            'number' : number,
        }
        return render_template('fortune.html', result = result) 
    return render_template('fortune.html')

if __name__ == '__main__':
    app.run(debug=True)