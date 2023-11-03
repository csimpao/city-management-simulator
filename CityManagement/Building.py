class Building():
    def __init__(self, building="", metal=0, wood=0):
        self.building = building
        self.wood = wood
        self.metal = metal
        
    def get_building(self):
        return self.building
    
    def get_metal(self):
        return self.metal
    
    def get_wood(self):
        return self.wood