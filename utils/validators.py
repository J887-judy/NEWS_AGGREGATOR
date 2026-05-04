def validar_email(email: str) -> bool:
    return "@" in email and "." in email

def validar_password(password: str) -> bool:
    return len(password) >= 6

def validar_nome(nome: str) -> bool:
    return len(nome.strip()) > 0
