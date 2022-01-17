def car_info(mfc, model, **other_info):
    info = {}
    info['Manufacturer'] = mfc
    info['Car model'] = model
    for key, value in other_info.items():
        info[key.title()] = value.title()
    return info

car = car_info('subaru', 'outback', color='blue', tow_package='True')
print(car)