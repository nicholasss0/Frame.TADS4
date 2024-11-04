from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('contact.html')


@app.route('/about')
def about():
    return 'meu contato'

@app.route('/canvas_img')
def canvas_img():
    return render_template('canvas_img.html')


@app.route('/print_screen')
def print_screen():
    return render_template('print_screen.html')






if "__main__" == __name__:
    app.run(debug=True, port='8080', host='0.0.0.0')

