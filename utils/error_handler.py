from flask import render_template

def handle_api_error(error_message):
    return render_template("error.html", message=f"Erro na API: {error_message}")

def handle_db_error(error_message):
    return render_template("error.html", message=f"Erro na base de dados: {error_message}")

def handle_generic_error(error_message):
    return render_template("error.html", message=f"Ocorreu um erro: {error_message}")
