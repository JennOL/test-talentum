class Weather:
    def __init__(self, city, temp, temp_min, temp_max, humidity, wind_speed, description):
        # Inicializa una nueva instancia de Weather con detalles específicos del clima.
        self.city = city # (str): Nombre de la ciudad
        self.temp = temp  # (float): Temperatura actual en Celsius
        self.temp_min = temp_min  # (float): Temperatura mínima en Celsius
        self.temp_max = temp_max  # (float): Temperatura máxima en Celsius
        self.humidity = humidity  # (int): Humedad relativa en porcentaje
        self.wind_speed = wind_speed  # (float): Velocidad del viento en m/s
        self.description = description  # (str): Descripción textual del clima

    def to_json(self):
        """
        Convertir los datos del clima a formato JSON para facilitar la respuesta de la API.

        Devuelve:
            dict: Representación en formato JSON de los datos del clima.
        """
        return {
            "city": self.city,
            "temp": self.temp,
            "temp_min": self.temp_min,
            "temp_max": self.temp_max,
            "humidity": self.humidity,
            "wind_speed": self.wind_speed,
            "description": self.description
        }
