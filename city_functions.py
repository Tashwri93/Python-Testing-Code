def get_city_country(city, country, population = ''):
    ##Format a City and Country and Population as optional##
    if population:
        city_country = city + ', ' + country + ', population = ' + str(population)
    else:
        city_country = city + ', ' + country 
        
    return city_country.title()

