def get_user_type(user_id):
    # Aquí simulamos el tipo de usuario. En producción, se conectará a la base de datos.
    # Devuelve "premium" o "free" según el tipo de usuario en la base de datos como ejemplo.
    simulated_db = {
        1: "premium",
        2: "free",
        # Agrega más usuarios según sea necesario o cambia logica dependiendo del negocio
    }
    return simulated_db.get(user_id, "free")
