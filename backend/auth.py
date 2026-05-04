from flask import render_template, request, redirect, session, url_for
from flask_bcrypt import Bcrypt
from database.db_utils import get_db

bcrypt = Bcrypt()

def register():
    if request.method == "POST":
        conn, cursor = get_db()

        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["password"]

        hash_senha = bcrypt.generate_password_hash(senha).decode("utf-8")

        cursor.execute(
            "INSERT INTO usuarios (nome, email, password) VALUES (?, ?, ?)",
            (nome, email, hash_senha)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


def login():
    if request.method == "POST":
        conn, cursor = get_db()

        email = request.form["email"]
        senha = request.form["password"]

        cursor.execute(
            "SELECT id, password FROM usuarios WHERE email = ?",
            (email,)
        )

        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.check_password_hash(user[1], senha):
            session["user_id"] = user[0]
            session["email"] = email
            return redirect(url_for("home"))

        return "Credenciais inválidas", 401

    return render_template("login.html")


def logout():
    session.clear()
    return redirect(url_for("login"))