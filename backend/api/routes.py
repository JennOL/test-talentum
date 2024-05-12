import os
from flask import request, jsonify, abort
from services.weather_service import WeatherService

def configure_routes(app):
    # Obtener la ruta del archivo weather.json y la clave API de las variables de entorno
    weather_data_path = os.getenv('WEATHER_DATA_PATH', '/data/weather.json')
    api_key = os.getenv('SECRET_KEY', 'default_secret_key')

    # Inicializar WeatherService con la ruta a los datos del clima
    weather_service = WeatherService(weather_data_path)

    @app.route('/')
    def hello_world():
        # Ruta básica para probar si el servidor está funcionando
        return 'Hello, Talentum!'
    
    @app.route('/weather', methods=['GET'])
    def get_weather():
        if request.args.get('key') is None:
            return jsonify({'error': 'API key not provided'}), 400
        
        if request.args.get('city') is None:
            return jsonify({'error': 'City not provided'}), 400
        
        # Extraer la clave API y el nombre de la ciudad de los parámetros de consulta
        client_api_key = request.args.get('key')
        city_name = request.args.get('city')
        # Normalizar el nombre de la ciudad a minúsculas para asegurar comparación sin distinción de mayúsculas/minúsculas
        city_name = city_name.lower()

        # Abortar con un error 401 si la clave API proporcionada no coincide con la clave API esperada
        if client_api_key != api_key:
            abort(401)  # No autorizado si la clave API no es correcta

        # Obtener los datos del clima para la ciudad solicitada y devolverlos en formato JSON
        weather_data = weather_service.get_weather_by_city(city_name)
        if weather_data:
            return jsonify(weather_data)
        else:
            return jsonify({'error': 'City not found'}), 404
        