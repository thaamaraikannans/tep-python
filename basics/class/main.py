class Vehicle:
    wheels = 4
    def __init__(self, name, brand): # obj constructor 
        self.name = name
        self.brand = brand

    def show(self): # instance method
        print(self.name, self.brand, self.wheels)
    
    @classmethod
    def values(cls, number): # class method
        cls.wheels = number
        # print(cls.wheels)
    
    @staticmethod
    def message(): # static method
        print("static content")

vehicle1 = Vehicle("xuv400", "mahindra")
vehicle2 = Vehicle("Swift", "suzuki")
vehicle3 = Vehicle("Duster", "renault")


vehicle1.show()

Vehicle.values(5)

vehicle2.show()
vehicle3.show()

vehicle1.message()
vehicle2.message()