# Creating variable named cars
cars = 100

# Creating a variable named space_in_a_car and assigning value of a floating point number
space_in_a_car = 4.0

# Creating a variable named drivers
drivers = 30

# Creating a variable named passengers
passengers = 90

# Creating a variable that is dependent on the variables cars and drivers
cars_not_driven = cars - drivers

# Cars driven is equal to the number of drivers we have
cars_driven = drivers

# This variable is derived from cars_driven and space in the car which are defined above
carpool_capacity = cars_driven * space_in_a_car

# A little calculation of the average passengers in a car
average_passengers_per_car = passengers / cars_driven

# This seems like a list where we have a variable in between two text strings
print("There are", cars, "cars available.")

# Same setup here
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
