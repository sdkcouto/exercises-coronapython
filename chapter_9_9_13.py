#. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you used a standard dictionary to represent a glossary. Rewrite the program using the OrderedDict class and make sure the order of the output matches the order in which key-value pairs were added to the dictionary.
from collections import OrderedDict
programming_words = OrderedDict()
programming_words = {'print' : 'pra printar',
    'if' : 'para condicionais',
    'and' : 'conjuncao para condicionais',
    'or' : 'conjuncao para condicionais',
    'str' : 'para transformar em string'
    }

programming_words['#'] = 'para comentarios'
programming_words['range'] = 'para series de numeros'

for name in programming_words.items():
    print(name)
programming_words['#'] = 'para comentarios'