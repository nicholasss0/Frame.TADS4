from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


MOCKED_USER = "admin"
MOCKED_PASSWORD = 1234


@app.route('/', methods=["GET", "POST"])
def start():

    if request.method == "POST":
        selection = request.form.get("selection")

        if selection == "toTagCanvas":
            return redirect(url_for("tagCanvas"))
        if selection == "toTakePhoto":
            return redirect(url_for("takePhoto"))
        if selection == "toGreatTable":
            return redirect(url_for("greatTable"))
        if selection == "authLogin":
            return redirect(url_for("authLogin"))
        else:
            return '''<script>
                    window.alert("faça sua escolha!")
                </script>'''
             
    return render_template("start.html" )

@app.route('/tagCanvas')
def tagCanvas():
    return render_template("tagCanvas.html")


@app.route('/takePhoto')
def takePhoto():
    return render_template("takePhoto.html")


@app.route('/greatTable', methods = ["GET", "POST"])
def greatTable():
    # fazer os botões editar e excluir funconarem
    if request.method == "POST":
        pass
    tables = generateTables()
    return render_template("997lines.html", tables=tables)



@app.route('/authLogin', methods = ["GET", "POST"])
def authLogin():
    message=""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == MOCKED_USER and password == MOCKED_PASSWORD:
            message = f"Bem vindo {MOCKED_USER}"
        elif username == "" or password == "":
            message = "Usuário e senha são obrigatórios"
        else:
            message = "Usuário ou senha não confere"

    return render_template("authLogin.html", message=message)

def generateTables():
    rows = []
    for i in range(1, 997):
        rows.append({
            "id": i,
            "first_name": "João",
            "last_name": "Silva",
            "email": "joao.silva@example.com",
        })
    return rows


if "__main__" == __name__:
   app.run(debug=True, host='0.0.0.0')
