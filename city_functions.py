def city_name(city,country,population = ""):
    if population:
        city_country = city + ", " + country + " - population " + str(population)
    else:
        city_country = city + ", " + country + "- population "
    return city_country.title()
    
city_name('santiago','chile')