class CountGeo:
    def __init__(self):
        pass
    
    def load_geojson(self):
        pass
    
    def count_area(self):
        pass
    
    def count_circuit(self):
        pass
    
    def get_data(self):
        area = count_area()
        circuit = count_circuit()
        
        return area, circuit
    
poligon = CountGeo()
print(poligon.get_date())
