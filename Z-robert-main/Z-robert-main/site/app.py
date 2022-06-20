from flask import Flask, render_template

consulta = Flask(__name__)

@consulta.route("/")
def pag():
    return render_template("cnpj.html")

if __name__ == "__main__":
    consulta.run(debug=True)
