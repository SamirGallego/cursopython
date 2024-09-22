import utils


data=[
    {
    'Country':'Colombia',
    'Population':500
    },
    {
    'Country':'Bolivia',
    'Population':300
    }
]

result = utils.population_by_country(data,'Bolivia')
print(result)