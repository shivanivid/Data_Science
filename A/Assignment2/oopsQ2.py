
class Vehicle:
    
    def Fare(self, fare):
        return float(fare)


v = Vehicle()


Bus = v.Fare(input("Enter Bus fare:"))
Car = v.Fare(input("Enter Car Fare:"))
Train = v.Fare(input("Enter Train fare:"))
Truck = v.Fare(input("Enter Truck fare:"))
Ship = v.Fare(input("Enter Ship fare:"))

# 3. Third variable TotalFare to store the sum of all fares
TotalFare = Bus + Car + Train + Truck + Ship

# 4. Print the TotalFare
print("Total Fare for all Vehicle Types:", TotalFare)