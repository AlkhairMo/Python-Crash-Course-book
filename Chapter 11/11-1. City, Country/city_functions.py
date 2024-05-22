def get_city(city, country, population=None):
    if population:
        city_country = f'{city}, {country} - population {population}'
    else:
        city_country = f'{city}, {country}'
    return city_country
