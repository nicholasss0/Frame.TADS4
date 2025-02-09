from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"  

MOCKED_USER = "admin"
MOCKED_PASSWORD = "1234"
MAX_ATTEMPTS = 4


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

tables = generateTables()





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
    return render_template("997lines.html", tables=tables)


@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    table = next((t for t in tables if t['id'] == id), None)
    if table:
        table.update({
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
        })
    return redirect(url_for('greatTable'))

@app.route('/delete/<int:id>')
def delete(id):
    global tables

    filtered_tables = []

    for table in tables:
        if table['id'] != id:
            filtered_tables.append(table)
    tables = filtered_tables

    return redirect(url_for('greatTable'))


@app.route('/authLogin', methods=["GET", "POST"])
def authLogin():
    if 'attempts' not in session:
        session['attempts'] = 0
        return render_template("authLogin.html", message=f"Você ainda tem mais {session['attempts']} tentativas")

    message = "Insira seu usuário e senha"

    if session['attempts'] >= MAX_ATTEMPTS:
        return render_template("authLogin.html", message="Você excedeu o número de tentativas. Tente novamente mais tarde.")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == MOCKED_USER and password == MOCKED_PASSWORD:
            session.pop('attempts', None)  # Reseta as tentativas após sucesso
            message = f"Bem-vindo {MOCKED_USER}"
        else:
            session['attempts'] += 1
            if session['attempts'] >= MAX_ATTEMPTS:
                message = "Você excedeu o número de tentativas. Tente novamente mais tarde."
            else:
                message = "Usuário ou senha não confere. Você ainda tem mais {session['attempts']} tentativas"

    return render_template("authLogin.html", message=message)


if "__main__" == __name__:
   app.run(debug=True, host='0.0.0.0')
