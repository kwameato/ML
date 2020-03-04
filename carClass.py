
# class Car():
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = 0
    
#     def descriptiveName(self):
#         longName = str(self.year) + " " + self.make + " " + self.model
#         return longName
    
#     def readOdometer(self):
#         print(f"this car has {str(self.odometer)} miles on it ")
    
#     def updateOdometer(self,mileage):
#         if mileage >= self.odometer:
#             self.odometer = mileage
#         else:
#             print("you can't roll back an odometer") 
    
#     def incrementOdometer(self,miles):
#         self.odometer += miles


# myNewCar = Car("audi","A4", "2016")

# carNew = Car("Sabura", "Outback",2013)

# print(carNew.descriptiveName())
# print(carNew.readOdometer())


# # print(myNewCar.descriptiveName())
# # carNew.updateOdometer(2600)
# # carNew.updateOdometer(200)
# # carNew.readOdometer()

# # print(".........................")
# # print(myNewCar.descriptiveName())
# # myNewCar.updateOdometer(23)
# # myNewCar.updateOdometer(20)

# # myNewCar.readOdometer()


names = ['kelvin','Raymond']

print(names)