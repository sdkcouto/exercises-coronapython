#Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {'salvador' : {'country' : 'brazil',
    'population' : '2,6 million',
    'fact' : "it was Brazil's first capital"
    },
    'rio de janeiro' : {'country' : 'brazil',
        'population' : '6,3 million',
        'fact' : "it was Brazil's second capital"},
    'brasilia' : {'country' : 'brazil',
        'population' : '2,4 million',
        'fact' : "is the current capital of brazil"
        }
    }
for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(city.title() + ' is a city from ' + country + ', has a population of ' + population + ' and  ' + fact)