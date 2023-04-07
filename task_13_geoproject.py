import geopandas as gpd
import json
from shapely.geometry import shape
geojson_path = "sciezka_do_mojego_geojsona"

class CountGeo:
    def __init__(self, path):
        self.path = path
        self.loaded_geojson = None
        self.geometry_1 = shape(self.loaded_geojson["geometry"])
    
    
    def load_geojson(self):
        self.loaded_geojson = gpd.read_file(self.path)
    
    def count_area(self):
         return self.geometry_1.area
    
    def count_circuit(self):
        perimeter = 0
    
        for feature in self.loaded_geojson['features']:
            geometry_2 = shape(feature['geometry'])
            perimeter += geometry_2.length
        
            return perimeter
    
    def get_data(self):
        area = self.count_area()
        circuit = self.count_circuit()
        
        return area, circuit
    
result_counting_poligon = CountGeo(geojson_path)
result_counting_poligon.load_geojson()
result_counting_poligon.loaded_geojson