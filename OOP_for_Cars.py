class Car:
  def __init__(self, make, model, color, year):
      self.make = make
      self.model = model
      self.color = color
      self.year = year

  def drive(self):
      print(f"The {self.color} {self.year} {self.make} {self.model} is now driving.")

  def stop(self):
      print(f"The {self.color} {self.year} {self.make} {self.model} has stopped.")

# Creating an instance (object) of the Car class
my_car = Car("Toyota", "Corolla", "Blue", 2020)

# Calling methods on the object
my_car.drive()
my_car.stop()
