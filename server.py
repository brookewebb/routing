from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return('Hello World!')

@app.route('/dojo')
def dojo():
    return('Dojo!')

@app.route('/say/<name>')
def say(name):
    return 'Hi ' + name + '!'

@app.route('/repeat/<int:num>/<word>')
def repeat(word, num):
    return word * num

if __name__=="__main__":
    app.run(debug=True)
