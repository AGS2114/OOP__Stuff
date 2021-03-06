class Crop:
    """A generic food crop"""

    #constructor
    def __init__(self,growth_rate, light_need, water_need):
        #set the attributes with an initial value

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

        #The above attributes are prefixed with an underscore to indicate
        #that they schoul be accessed directly from the outwith the class

def main():
    #instaniate the class
    new_crop = Crop(1,4,3)
    #test to see whether it works or not
    print(new_crop._status)
    print(new_crop._light_need)
    print(new_crop._water_need)
    new_crop2 = Crop(2,5,7)
    print(new_crop2._status)
    print(new_crop2._light_need)
    print(new_crop2._water_need)

if __name__ == "__main__":
    main()
