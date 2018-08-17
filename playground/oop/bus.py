from vechicle import Vechicle

class Bus(Vechicle):

    def __init__(self, pTop_speed=100):
        # this variables belongs to the object, the instance of the class (different from java)
        # self.top_speed = pTop_speed
        # self.__warnings = []
        super().__init__(pTop_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)

bus1 = Bus(200)
bus1.add_warning('New warning for the bus!')
bus1.add_group(['Ana', 'Magda', 'Gabriel'])
print(bus1.passengers)
bus1.drive()



   