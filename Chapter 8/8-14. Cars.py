def cars(manufacturer, model_name, **car_information):
    car_information['manufacturer'] = manufacturer
    car_information['model name'] = model_name
    return car_information


car = cars('subaru', 'outback', color='blue', tow_package=True)
print(car)
