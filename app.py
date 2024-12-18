from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def start():

    if request.method == "POST":
        selection = request.form.get("selection")

        if selection == "toTagCanvas":
            return redirect(url_for("tagCanvas"))
        else:
            return '''<script>
                    window.alert("faça sua escolha!")
                </script>'''
             
    return render_template("start.html")

@app.route('/tagCanvas')
def tagCanvas():
    return render_template("tagCanvas.html")


if "__main__" == __name__:
   app.run(debug=True, host='0.0.0.0')
