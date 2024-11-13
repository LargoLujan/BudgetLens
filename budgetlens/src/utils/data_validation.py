def validate_data(data):
    # Asegurarse de que el formato de los datos sea correcto
    if "values" not in data or not isinstance(data["values"], list):
        raise ValueError("Datos inválidos: se espera una lista de valores en 'values'.")
    return True
