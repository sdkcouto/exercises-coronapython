#Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.

info={'info_0' : {'first_name' : ' Thales',
    'last_name' : 'Silva',
    'age' : '30',
    'city' : 'Rio de janeiro'
    },
'info_1' : {'first_name' : 'Pedro',
    'last_name' : 'Damasceno',
        'age' : '29',
        'city' : 'salvador'
    },
'info_2' : {'first_name' : 'Thais',
    'last_name' : 'Dantas',
    'age' : '28',
    'city' : 'Salvador'
    }
}

for name, infos in info.items():
    full_name = infos['first_name'] + " " + infos['last_name']
    age = infos['age']
    city = infos['city']
    print('Full name: ' + full_name.title() + ", age: " + age + ", city: " + city + ".")
