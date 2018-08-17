from vechicle import Vechicle

class Car(Vechicle):
    
    def brag(self):
        print('Look how cool my car is!')



car1 = Car()
car1.drive()

Car.top_speed = 200
# This is not working anymore because is private
# car1.__warnings.append('New warning')
print(car1)




car2 = Car(200)
car2.drive()
car2.add_warning('Adding warning from a method')

car3 = Car(300)
car3.drive()
car3.get_warnings()