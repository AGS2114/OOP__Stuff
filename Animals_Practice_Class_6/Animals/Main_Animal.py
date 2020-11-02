import random

class animal:
    """An Animal"""

    #constructor
    def __init__(self,growth_rate, food_need, water_need):
        #set the attributes with an initial value

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Young"
        self._type = "Generic"

        #The above attributes are prefixed with an underscore to indicate
        #that they schoul be accessed directly from the outwith the class

    def needs(self):
        #returna dictionary containing the food and water needs
        return {'food need':self._food_need,'water needs':self._water_need}
    
    #method to report report the provide informaion about the current state of
    #crop
    def report(self):
        #return a dictionary containing type, status and growth and days growing
        return{'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}

    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Teenage"
        elif self._growth > 0 :
            self._status = "Young"
        elif self._growth == 0:
            self._status = "Newborn"
            

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._growth += self._growth_rate
        #increment days growing
        self._days_growing += 5
        #update the status
        self._update_status()

def auto_grow(animal,days):
    #grow the animal
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_grow(animal):
    #get the food and water values from the user
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")
    valid = False
    while not valid:
        water = 0
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")   
    #grow the animal
        animal.grow(food,water)

def display_menu():
    print("1. Grow manually over in 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exti test program")
    print()
    print("Please select an option from the above menu")
    
def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <=4:
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice


def manage_animal(animal):
    print("This is the animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the animal management program")
                            
def main():
    #instaniate the class
    new_animal = animal(1,4,3)
    manage_animal(new_animal)


if __name__ == "__main__":
    main()
