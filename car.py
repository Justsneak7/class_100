class Car(object):
     def __init__(self, model, color, company, speed_limit):
         self.model = model
         self.color = color
         self.company = company
         self.speed_limit = speed_limit

     def start(self):
         print("the vehicle has started")

     def stop(self):
         print("the vehicle has stopped")

     def accelerate(self, accelerator):
         print("the vehicle is moving at a speed")
         print(accelerator)
     
     def changeGear(self, gearNo):
         print("the gear has been changed to ")
         print(gearNo)

tesla = Car("roadster7", "yellow", "tesla", "300")

tesla.start()

tesla.accelerate(37)

tesla.changeGear("3rd gear")

print(tesla.color)
print(tesla.speed_limit)
print(tesla.company)
print(tesla.model)