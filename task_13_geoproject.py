import geopandas as gpd
geojson_path = "sciezka_do_mojego_geojsona"

class CountGeo:
    def __init__(self, path):
        self.path = path
        self.loaded_geojson = None
    
    def load_geojson(self):
        self.loaded_geojson = gpd.read_file(self.path)
    
    def count_area(self):
        pass
    
    def count_circuit(self):
        pass
    
    def get_data(self):
        area = self.count_area()
        circuit = self.count_circuit()
        
        return area, circuit
    
result_counting_poligon = CountGeo(geojson_path)
result_counting_poligon.load_geojson()
result_counting_poligon.loaded_geojson
result_counting_poligon.get_data()