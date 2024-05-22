def get_city_country(city, country):
    ci_co = f'"{city}, {country}"'
    return ci_co.title()


city_country = get_city_country('madrid', 'spain')
print(city_country)
city_country = get_city_country('jeddah', 'saudi arabia')
print(city_country)
city_country = get_city_country('santiago', 'chile')
print(city_country)
