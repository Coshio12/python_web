from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return '<h2>Hola Mundo de Flask</h2>'

if __name__ == '__main__':
    app.run(debug=True)