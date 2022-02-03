def city_function(city, country, population=''):
    if population:
        pair = city + ', ' + country + ' - population ' + population
    else:
        pair = city + ', ' + country
    return pair.title()


print(city_function('beijing', 'china', '1000000'))
