import sqlite3
from flask import Flask, render_template, url_for


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask('__name__')


@app.route('/')
def base():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('base.html', posts=posts)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/registrar')
def registrar():
    return render_template('registrar.html')


@app.route('/consultar')
def consultar():
    return render_template('consultar.html')


@app.route('/atualizar')
def atualizar():
    return render_template('atualizar.html')


if __name__ == "__main__":
    app.run(debug=True)
