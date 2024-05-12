import json

class DataLoader:
    def __init__(self, file_path):
        """
        Inicializa DataLoader con la ruta al archivo JSON.

        Parámetros:
            file_path (str): Ruta al archivo JSON que se cargará.
        """
        self.file_path = file_path

    def load_data(self):
        """
        Carga y retorna los datos desde un archivo JSON.

        Devuelve:
            dict: Los datos cargados del archivo JSON.
        """
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return data
