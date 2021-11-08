from flask import Flask,render_template
import prueba

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prueba')
def prueba():
    return render_template('preba.py')



if __name__ == '__main__':
    app.run(debug=True)