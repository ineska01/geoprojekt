import geopandas as gpd

geojson_path = "C:\workspace\geoprojekt\geojson.geojson"


class CountGeo:
    def __init__(self, path):
        self.path = path
        self.loaded_geojson = None
        self.area = 0.0
        self.circuit = 0.0

    def load_geojson(self):
        self.loaded_geojson = gpd.read_file(self.path)

    def count_area(self):
        self.area = self.loaded_geojson.geometry.area

    def count_circuit(self):
        self.circuit = self.loaded_geojson["geometry"].apply(
            lambda x: x.length if x.geom_type == "Polygon" else None
        )

    def get_data(self):
        self.load_geojson()
        self.count_area()
        self.count_circuit()

        return self.area, self.circuit


result_counting_poligon = CountGeo(geojson_path)
a, c = result_counting_poligon.get_data()
print(result_counting_poligon.circuit)
print(a, c)
