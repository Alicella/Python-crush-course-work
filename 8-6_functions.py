def city_country(city, country):
    pair = city + ', ' + country
    return pair.title()

while True:
    print('\nEnter city and country names to get a pair.')
    print('Enter q at any time to quit.')    
     
    ct_name = input("City name: ")
    if ct_name == 'q':
        break
    cotr_name= input("Country name: ")
    if cotr_name == 'q':
        break 
    
    val = city_country(ct_name, cotr_name)
    print(val)