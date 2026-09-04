class Vehicle():
    def __init__(self, brand, model , base_price):
        self.brand = brand
        self.model =  model 
        self.base_price = base_price

    def get_details(self):
        return f"Brand : {self.brand} , Model : {self.model}, BasePrice : {self.base_price}"

class S_class(Vehicle):
    def __init__(self, version):
        super().__init__()
        self.version = version
    def get_details(self):    
        return f"Brand : {self.brand}, Model : {self.model}, BasePrice : {self.base_price}, Version : {self.version}"

class G_class(Vehicle):
    def __init__(self, version):
        super().__init__()
        self.version = version
    def get_details(self): 
        return f"Brand : {self.brand}, Model : {self.model}, BasePrice : {self.base_price}, Version : {self.version}"

class Inventory():
    def __init__(self):
     self.inventory = []
    def _add_vehicle(self, new_vehicle):
        self.inventory.append(new_vehicle)
    def calculate_fleet_value(self):
        total_cost= 0
        for vehicle in self.inventory:
            total_cost += vehicle.base_price
            return total_cost


dealership = Inventory()

s_class_sedan = S_class("Mercedes-Benz", "S-Class", 17000000, "Maybach S 580")
g_class_suv = G_class("Mercedes-Benz", "G-Class", 25500000, "AMG G 63")

dealership.add_vehicle(s_class_sedan)
dealership.add_vehicle(g_class_suv)

print("--- Executive Fleet Inventory ---")
for car in dealership.inventory:
    print(car.get_details())

print(f"\nTotal Dealership Valuation: ₹{dealership.calculate_fleet_value():,}")                                  



       
 
                