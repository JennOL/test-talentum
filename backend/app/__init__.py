from flask import Flask
# Importar la función para configurar rutas del paquete api
from api.routes import configure_routes

def create_app():
    """
    Crear y configurar una instancia de la aplicación Flask.

    Devoluciones:
        app (Flask): Una instancia de la aplicación Flask configurada con rutas y ajustes de depuración.
    """
    # Crear una instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Configurar las rutas para la aplicación pasando la instancia de la app a la función configure_routes
    configure_routes(app)
    return app

