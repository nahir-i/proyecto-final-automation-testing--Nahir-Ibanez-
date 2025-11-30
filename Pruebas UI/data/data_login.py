CASOS_LOGIN = [
    ("standard_user", "secret_sauce", True),     # Usuario válido, login exitoso
    ("locked_out_user", "secret_sauce", False),  # Usuario bloqueado, login fallido
    ("usuario_malo", "clave_mala", False),    # Credenciales inválidas, login fallido
]