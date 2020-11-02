from Main_Animal import *

class Cow(animal):
    """A Cow"""

    #constructor
    def __init__(self):
        #call the parent class constructor with default values for potatos
        #growth rate = 1; food need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Cow"

    #override grow method for subclass
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Newborn" and water > self._water_need:
                self._growth += self._growth_rate * 2
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 3
            else:
                self._growth += self._growth_rate
        #increament day growing
        self._days_growing += 1
        #update the status
        self._update_status()

def main():
    #create a new animal_cow
    animal_cow = Cow()
    print(animal_cow.report())
    #manually grow the animal_cow
    manual_grow(animal_cow)
    print(animal_cow.report())
    manual_grow(animal_cow)
    print(animal_cow.report())

if __name__ == "__main__":
    main()
