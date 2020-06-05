#Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:

#car = make_car('subaru', 'outback', color='blue', tow_package=True)

#Print the dictionary that’s returned to make sure all the information was stored correctly.

def build_car(manufacturer,model_name,**cars_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name
    for key, value in cars_info.items():
        car[key] = value
    
    return car
car_profile = build_car('ford', 'fiesta', color='red', feaature='hydraulic steering')
print(car_profile)