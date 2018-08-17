class Vechicle:

    # this variables belongs to the class, not to instance (different from java)
    # top_speed = 100
    #warnings = []

    def __init__(self, pTop_speed=100):
        # this variables belongs to the object, the instance of the class (different from java)
        self.top_speed = pTop_speed
        self.__warnings = []
    
    def __repr__(self):
        print('Printing ...')
        return 'Top speed: {}, Warnings: {}'.format(self.top_speed, len(self.__warnings))

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)
    
    def get_warnings(self):
        return self.__warnings

    def drive(self):
        print('This car has a top speed of {}, Warnings {}'.format(self.top_speed, len(self.__warnings)))