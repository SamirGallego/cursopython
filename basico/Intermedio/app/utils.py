def get_population():
    keys=['col','bol']
    values = [300,200]
    return keys, values

def population_by_country(data, country):
    result= list(filter(lambda item: item['Country']==country,data))
    return result