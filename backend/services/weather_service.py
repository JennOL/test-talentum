from data.data_loader import DataLoader
from models.weather import Weather

class WeatherService:
    def __init__(self, data_file):
        """
        Inicializa WeatherService con la ruta del archivo de datos.

        Parámetros:
            data_file (str): Ruta al archivo de datos del clima.
        """        
        self.data_loader = DataLoader(data_file)
        self.weather_data = self.process_data()

    def convertTemp(temp):
        return temp - 273.15

    def process_data(self):
        """
        Procesa los datos cargados y crea un diccionario de objetos Weather indexado por el nombre de la ciudad.

        Devuelve:
            dict: Diccionario donde las claves son nombres de ciudades en minúsculas y los valores son objetos Weather.
        """
        raw_data = self.data_loader.load_data()

        weather_list = {}
        for city_data in raw_data['cities']:
            weather_info = {
                'city': city_data['name'],
                'temp': self.convertTemp(city_data['main']['temp']),
                'temp_min': self.convertTemp(city_data['main']['temp_min']),
                'temp_max': self.convertTemp(city_data['main']['temp_max']),
                'humidity': city_data['main']['humidity'],
                'wind_speed': city_data['wind']['speed'],
                'description': city_data['weather'][0]['main']  # Asumiendo que hay al menos un elemento en 'weather'
            }
            city = city_data['name'].lower()
            weather_list[city] = Weather(**weather_info)
        return weather_list

    def get_weather_by_city(self, city_name):
        """
        Devuelve los datos climáticos en formato JSON para una ciudad específica. Si no se encuentra la ciudad, retorna un error.

        Parámetros:
            city_name (str): Nombre de la ciudad en minúsculas para buscar sus datos climáticos.

        Devuelve:
            dict: Datos del clima en formato JSON o un mensaje de error si la ciudad no se encuentra.
        """
        weather = self.weather_data.get(city_name)
        if weather:
            return weather.to_json()
        else:
            return {'error': 'City not found'}, 404
