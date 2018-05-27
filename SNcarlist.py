class Car:
    def __init__(self, brand, model, kms, servicedate):
        self.brand = brand
        self.model = model
        self.kms = kms
        self.servicedate = servicedate

    def get_brandplusmodel(self):
        return self.brand + " " + self.model


def carlist(cars):
    for index, car in enumerate(cars):
        print "Car ID: " + str(index)
        print car.get_brandplusmodel()
        print car.kms + " kms"
        print "Service date " + car.servicedate
        print ""

    if not cars:
        print "You don't have any cars in your car list."


def add_car(cars):
    brand = raw_input("Please enter the car's brand: ")
    model = raw_input("Please enter the car's model: ")
    kms = raw_input("Please enter the car's kms: ")
    servicedate = raw_input("Please enter the car's service date: ")

    new = Car(brand=brand, model=model, kms=kms, servicedate=servicedate)
    cars.append(new)

    print ""
    print new.get_brandplusmodel() + " was successfully added to your car list."


def edit_car(cars):
    print "Select the number of the car you'd like to edit:"

    for index, car in enumerate(cars):
        print str(index) + ") " + car.get_brandplusmodel()

    print ""
    selected_id = raw_input("What car would you like to edit? (enter ID number): ")
    selected_car = cars[int(selected_id)]

    new_servicedate = raw_input("Please enter a new service date for %s: " % selected_car.get_brandplusmodel())
    selected_car.servicedate = new_servicedate

    print ""
    print "Service date updated."


def delete_car(cars):
    print "Select the number of the car you'd like to delete:"

    for index, car in enumerate(cars):
        print str(index) + ") " + car.get_brandplusmodel()

    print ""
    selected_id = raw_input("What car would you like to delete? (enter ID number): ")
    selected_car = cars[int(selected_id)]
    car_name = car.get_brandplusmodel()
    cars.remove(selected_car)
    print ""
    print "The " + car_name + " was successfully removed from your car list."


def main():
    print "Welcome to your car list"

    fordfocus = Car(brand="Ford", model="Focus", kms="50000", servicedate="21/09/2018")
    renaultclio = Car(brand="Renault", model="Clio", kms="120000", servicedate="07/03/2019")
    vwpassat = Car(brand="Volswagen", model="Passat", kms="250000", servicedate="02/05/2019")
    cars = [fordfocus, renaultclio, vwpassat]

    while True:
        print ""
        print "Please choose one of these options:"
        print "a) See all your cars"
        print "b) Add a new car"
        print "c) Edit a car"
        print "d) Delete a car"
        print "e) Quit the program."
        print ""

        selection = raw_input("Enter your selection (a, b, c, d or e): ")
        print ""

        if selection.lower() == "a":
            carlist(cars)
        elif selection.lower() == "b":
            add_car(cars)
        elif selection.lower() == "c":
            edit_car(cars)
        elif selection.lower() == "d":
            delete_car(cars)
        elif selection.lower() == "e":
            print "Thank you for using Car List. Goodbye!"
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue

if __name__ == "__main__":
    main()